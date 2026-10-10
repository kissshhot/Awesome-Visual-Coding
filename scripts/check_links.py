#!/usr/bin/env python3
"""Check catalog HTTPS links separately from offline content validation."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import re
import time
from urllib.error import HTTPError
from urllib.parse import urldefrag, unquote
from urllib.request import Request, urlopen
from validate_catalog import ROOT, external_targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='docs/link-check.json')
    parser.add_argument('--retry-failed', action='store_true', help='Retain successful observations in an existing report and retry only failures')
    args = parser.parse_args()
    groups = {}
    for target in external_targets():
        url, frag = urldefrag(target)
        groups.setdefault(url,set())
        if frag:
            groups[url].add(unquote(frag))
    previous = {}
    out = ROOT/args.output
    if args.retry_failed and out.exists():
        previous = {r['url']:r for r in json.loads(out.read_text())['results'] if r['ok'] and all(r.get('fragments',{}).values())}
    def check(url):
        if url in previous and set(previous[url].get('fragments',{})) == groups[url]:
            return previous[url]
        result={'url':url,'ok':False,'attempts':[]}
        for attempt in range(2):
            stamp=datetime.now(timezone.utc).isoformat(timespec='seconds')
            try:
                req=Request(url,headers={'User-Agent':'Awesome-Visual-Coding-source-check/1.0'})
                with urlopen(req, timeout=25) as response:
                    body=response.read(8_000_000)
                    status=response.status
                    content_type=response.headers.get('Content-Type','')
                    final=response.url
                ids=set(re.findall(r'(?:id|name)=["\']([^"\']+)["\']',body.decode('utf-8','replace')))
                result.update(ok=200<=status<300,status=status,final_url=final,content_type=content_type,bytes_read=len(body),sha256=hashlib.sha256(body).hexdigest(),checked_at=stamp,fragments={f:f in ids for f in sorted(groups[url])})
                result['attempts'].append({'at':stamp,'status':status})
                result.pop('error',None)
                break
            except Exception as exc:
                result['attempts'].append({'at':stamp,'error':str(exc)})
                result.update(error=str(exc),checked_at=stamp,status=exc.code if isinstance(exc,HTTPError) else None)
                if attempt == 0:
                    time.sleep(0.5)
        print(('OK ' if result['ok'] and all(result.get('fragments',{}).values()) else 'CHECK ')+url,flush=True)
        return result
    with ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(check,sorted(groups)))
    report={'generated_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'HTTPS GET; bounded body; timeout 25s; one retry; HTML fragment IDs checked; no authentication','results':results}
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    unresolved=sum(not r['ok'] or not all(r.get('fragments',{}).values()) for r in results)
    print(f'{len(results)} URLs; {unresolved} unresolved. Saved {out}')
    return bool(unresolved)


if __name__=='__main__':
    raise SystemExit(main())
