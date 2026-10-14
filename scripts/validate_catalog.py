#!/usr/bin/env python3
"""Offline structural validation for the bilingual visual-coding catalog."""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit, urldefrag

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]]*\]\(([^\s)]+)\)')
CJK = re.compile(r'[\u3400-\u9fff]')


def body_lines(text):
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, line
    if fence:
        raise ValueError('Unclosed Markdown fence')


def cells(line):
    return [x.strip() for x in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def anchors(text):
    result, counts = [], Counter()
    for _, line in body_lines(text):
        result.extend(re.findall(r'<a\s+(?:id|name)="([^"]+)"', line))
        if re.match(r'^#{1,6} ', line):
            heading = re.sub(r'^#+\s+', '', line).strip()
            heading = re.sub(r'<[^>]+>', '', heading)
            key = re.sub(r'[^\w -]', '', heading.lower()).replace(' ', '-')
            result.append(key + (f'-{counts[key]}' if counts[key] else ''))
            counts[key] += 1
    return result


def external_targets():
    return sorted({target for path in ROOT.rglob('*.md')
                   for _, line in body_lines(path.read_text())
                   for target in LINK.findall(line)
                   if urlsplit(target).scheme == 'https'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--links', help='Also validate a saved check_links.py report')
    args = parser.parse_args()
    errors = []
    def check(ok, msg):
        if not ok:
            errors.append(msg)
    data = json.loads((ROOT/'data/catalog.json').read_text())
    cutoff, reviewed = date.fromisoformat(data['cutoff']), date.fromisoformat(data['review_date'])
    check(reviewed >= cutoff, 'Review predates cutoff')
    entries = data['entries']
    systems = data['systems']
    categories = [x['name'] for x in data['categories']]
    docs = {p: p.read_text() for p in ROOT.rglob('*.md') if '.git' not in p.parts}
    amap = {p: anchors(t) for p, t in docs.items()}
    for path, text in docs.items():
        check(len(amap[path]) == len(set(amap[path])), f'Duplicate anchors: {path.name}')
        previous_width = None
        for n, line in body_lines(text):
            if line.startswith('|'):
                width = len(cells(line))
                check(previous_width in (None, width), f'{path.name}:{n}: table width mismatch')
                previous_width = width
            else:
                previous_width = None
            for target in LINK.findall(line):
                u = urlsplit(target)
                if u.scheme or u.netloc:
                    check(u.scheme == 'https', f'Non-HTTPS link: {target}')
                    continue
                dest = (path.parent/unquote(u.path)).resolve() if u.path else path
                check(dest.is_file(), f'{path.name}:{n}: missing local file {target}')
                if u.fragment:
                    check(dest in amap and unquote(u.fragment) in amap.get(dest, []), f'Missing anchor: {target}')

    readme = docs[ROOT/'README.md']
    audit = docs[ROOT/'docs/SOURCE_AUDIT.md']
    read_rows, audit_rows = {}, {}
    current = None
    for n, line in body_lines(readme):
        if line.startswith('## '):
            current = line[3:]
        if line.startswith('| **') and 'https://arxiv.org/abs/' in line:
            r = cells(line)
            check(len(r) == 6, f'Entry at line {n} requires six columns')
            m = re.search(r'arxiv.org/abs/(\d{4}\.\d{4,5})\)', line)
            check(bool(m), f'Noncanonical arXiv link at line {n}')
            if not m or len(r) != 6:
                continue
            aid = m[1]
            check(aid not in read_rows, f'Duplicate README ID {aid}')
            read_rows[aid] = (current, r)
            check(bool(re.search('[A-Za-z]', r[2])) and not CJK.search(r[2]), f'English missing: {aid}')
            check(bool(CJK.search(r[3])), f'Chinese missing: {aid}')
            check(not CJK.search(' '.join(r[:3]+r[4:])), f'Chinese outside summary: {aid}')
            nums = lambda s: re.findall(r'\d+(?:\.\d+)?', s)
            check(nums(r[2]) == nums(r[3]), f'Numeric parity mismatch: {aid}')
        elif CJK.search(line):
            check(line == '| Paper and type | First submitted | English | 中文 | Source | Checked |', f'Chinese outside research summaries: README:{n}')
    for _, line in body_lines(audit):
        if line.startswith('| <a id="paper-'):
            r = cells(line)
            m = re.search(r'arxiv.org/abs/(\d{4}\.\d{4,5})\)', r[0])
            check(len(r) == 5 and bool(m), 'Malformed audit row')
            if m:
                check(m[1] not in audit_rows, f'Duplicate audit ID {m[1]}')
                audit_rows[m[1]] = r
    ids = [e['id'] for e in entries]
    check(len(ids) == len(set(ids)), 'Duplicate registry IDs')
    titles = [re.sub(r'\W', '', e['title'].lower()) for e in entries]
    check(len(titles) == len(set(titles)), 'Duplicate normalized titles')
    check(set(ids) == set(read_rows) == set(audit_rows), 'Inventory differs between registry, README and audit')
    counts = Counter()
    for e in entries:
        aid = e['id']; counts[e['status']] += 1
        check(re.fullmatch(r'\d{4}\.\d{4,5}', aid), f'Invalid identifier {aid}')
        check(e['category'] in categories, f'Unknown category: {aid}')
        check(e['status'] in ('A','M'), f'Invalid evidence status: {aid}')
        check(bool(e['authors']) and len(e['authors']) == len(set(e['authors'])), f'Missing/duplicate authors: {aid}')
        try:
            first, revised = date.fromisoformat(e['first_submitted']), date.fromisoformat(e['revised'])
            check(first <= revised <= cutoff, f'Date/cutoff conflict: {aid}')
            entry_review = date.fromisoformat(e['review_date'])
            check(revised <= entry_review <= reviewed, f'Entry review date conflict: {aid}')
        except ValueError:
            check(False, f'Invalid calendar date: {aid}')
        check(re.fullmatch(r'v[1-9]\d*',e['version']), f'Invalid revision: {aid}')
        check(e['source'] == f'https://arxiv.org/abs/{aid}', f'Noncanonical source: {aid}')
        check(re.fullmatch(r'[a-f0-9]{64}',e['metadata_sha256']), f'Missing retrieval hash: {aid}')
        if e['status'] == 'M':
            check(e.get('sections') and f'/{aid}{e["version"]}#' in e.get('evidence_url',''), f'Unpinned method evidence: {aid}')
            check(re.fullmatch(r'[a-f0-9]{64}',e.get('full_text_sha256','')), f'Missing full-text hash: {aid}')
        if aid not in read_rows or aid not in audit_rows:
            continue
        cat, r = read_rows[aid]; ar = audit_rows[aid]
        check(cat == e['category'], f'Category mismatch: {aid}')
        expected = [f'**{e["label"]}**<br>{e["kind"]}',e['first_submitted'],e['english'],e['chinese'],f'[{"arXiv " + aid}]({e["source"]})',f'[{e["status"]} · {e["version"]}](docs/SOURCE_AUDIT.md#paper-{aid.replace(".","-")})']
        check(r == [x.replace('|',r'\|') for x in expected], f'README/registry mismatch: {aid}')
        check(ar[1] == e['title']+'<br>'+'; '.join(e['authors']), f'Audit title/authors mismatch: {aid}')
        check(ar[2:4] == [e['first_submitted'],e['version']+' · '+e['revised']], f'Audit date/revision mismatch: {aid}')
        check(ar[4].startswith(e['status']+' —'), f'Audit status mismatch: {aid}')
        if e['status'] == 'M':
            check(e['evidence_url'] in ar[4], f'Audit evidence URL mismatch: {aid}')
    for p,t in docs.items():
        if p.name not in ('README.md',):
            check(not any(CJK.search(line) for _,line in body_lines(t)), f'Non-English guidance: {p.name}')
    check(f'**{len(entries)} research entries**' in readme,'Displayed total mismatch')
    check(f'{counts["M"]} M and {counts["A"]} A' in audit,'Audit evidence counts stale')
    system_rows = {}
    current = None
    for _, line in body_lines(readme):
        if line.startswith('## '):
            current = line[3:]
        if line.startswith('| **') and 'docs/SOURCE_AUDIT.md#system-' in line:
            sid = re.search(r'#system-([a-z0-9-]+)\)', line)[1]
            check(sid not in system_rows, f'Duplicate system row: {sid}')
            system_rows[sid] = (current, cells(line))
    system_ids = [s['id'] for s in systems]
    audit_system_ids = re.findall(r'<a id="system-([a-z0-9-]+)">', audit)
    check(len(system_ids) == len(set(system_ids)), 'Duplicate system registry IDs')
    check(set(system_ids) == set(system_rows) == set(audit_system_ids), 'System inventory differs between registry, README and audit')
    check(f'{len(systems)} D system resources' in audit, 'Audit system count stale')
    groups = Counter(s['group'] for s in systems)
    check(f'**{groups["open-source"]} non-academic open-source projects**' in readme, 'Open-source total mismatch')
    check(f'**{groups["hosted"]} hosted system resource' in readme, 'Hosted total mismatch')
    for s in systems:
        sid = s['id']
        check(s['status'] == 'D', f'Invalid system evidence status: {sid}')
        check(s['group'] in ('open-source', 'hosted'), f'Unknown system group: {sid}')
        check(date.fromisoformat(s['review_date']) <= reviewed, f'System review date conflict: {sid}')
        audit_part = audit.split(f'<a id="system-{sid}"></a>', 1)[-1].split('\n### ', 2)
        audit_part = '\n### '.join(audit_part[:2])
        check(s['evidence_note'] in audit_part, f'System evidence note missing: {sid}')
        if s['group'] == 'open-source':
            prefix = f'https://github.com/{s["repository"]}/blob/{s["commit"]}/'
            check(s['source'] == f'https://github.com/{s["repository"]}', f'System repository mismatch: {sid}')
            check(re.fullmatch(r'[a-f0-9]{40}', s['commit']), f'Unpinned source revision: {sid}')
            check(s['readme_url'] == prefix+'README.md', f'Unpinned README: {sid}')
            check(s['license_url'].startswith(prefix) and s['license'], f'Unpinned license: {sid}')
            for field in ('readme_sha256', 'license_sha256'):
                check(re.fullmatch(r'[a-f0-9]{64}', s[field]), f'Missing {field}: {sid}')
            check(s['readme_url'] in audit_part and s['license_url'] in audit_part, f'System audit sources mismatch: {sid}')
            expected = [f'**{s["label"]}**<br>{s["role"]}', s['description'],
                        f'[{s["repository"]}]({s["source"]})', f'[{s["license"]}]({s["license_url"]})',
                        f'[{s["commit"][:7]}]({s["readme_url"]})', f'[D · {s["review_date"]}](docs/SOURCE_AUDIT.md#system-{sid})']
            section = 'Non-Academic Open-Source Projects'
        else:
            check(date.fromisoformat(s['source_date']) <= date.fromisoformat(s['review_date']), f'System source date conflict: {sid}')
            check(s['source'] in audit_part, f'Hosted audit source mismatch: {sid}')
            expected = [f'**{s["label"]}**<br>{s["role"]}', 'Published '+s['source_date'], s['description'],
                        f'[Official launch announcement]({s["source"]})', f'[D · Announcement](docs/SOURCE_AUDIT.md#system-{sid})']
            section = 'Official System Resources'
        if sid in system_rows:
            check(system_rows[sid] == (section, [x.replace('|', r'\|') for x in expected]), f'System README/registry mismatch: {sid}')
    for e in entries:
        if 'implementation' not in e:
            continue
        imp = e['implementation']
        check(date.fromisoformat(imp['review_date']) <= reviewed, f'Implementation review date conflict: {e["id"]}')
        prefix = f'https://github.com/{imp["repo"]}/blob/{imp["commit"]}/'
        check(re.fullmatch(r'[a-f0-9]{40}', imp['commit']), f'Unpinned implementation: {e["id"]}')
        check(imp['readme_url'] == prefix+'README.md', f'Implementation source mismatch: {e["id"]}')
        check(re.fullmatch(r'[a-f0-9]{64}', imp['readme_sha256']), f'Missing implementation hash: {e["id"]}')
        check(imp['readme_url'] in readme and imp['readme_url'] in audit, f'Implementation documentation missing: {e["id"]}')
        check(imp['evidence_note'] in readme and imp['evidence_note'] in audit, f'Implementation scope mismatch: {e["id"]}')
    for c in categories:
        slug = re.sub(r'[^\w -]','',c.lower()).replace(' ','-')
        check(f'## {c}\n' in readme and f'[{c}](#{slug})' in readme, f'Missing category/navigation {c}')
    if args.links:
        report = json.loads((ROOT/args.links).read_text())
        targets = {urldefrag(u)[0] for u in external_targets()}
        check(set(r['url'] for r in report['results']) == targets, 'Link report inventory stale')
        for r in report['results']:
            check(r['ok'], f'Unresolved external URL: {r["url"]}: {r.get("error",r.get("status"))}')
            check(all(r.get('fragments',{}).values()), f'External fragment missing: {r["url"]}')
    if errors:
        print('\n'.join('FAIL: '+x for x in errors),file=sys.stderr)
        return 1
    print(f'PASS: {len(entries)} unique bilingual research entries; {len(categories)} categories; {groups["open-source"]} open-source projects and {groups["hosted"]} hosted resource(s)')
    print(f'PASS: {len(audit_rows)} audit records; {counts["M"]} M / {counts["A"]} A; authors, dates, cutoff, versions and registry parity')
    print(f'PASS: {len(systems)} system records; README/audit parity, review dates and pinned open-source documentation/licenses')
    print(f'PASS: {len(docs)} Markdown files; table shapes, summary languages/numbers, local links, anchors and navigation')
    if args.links:
        print(f'PASS: {len(report["results"])} external URLs and all cited remote fragments in saved report')
    print('Limits: scientific truth, semantic translation and executable behavior require separate review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
