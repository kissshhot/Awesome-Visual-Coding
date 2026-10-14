# Contributing

Prefer a useful, source-backed addition or correction over increasing the count. Keep all guidance, headings, metadata and system descriptions in English. Paper and technical-report summaries must have parallel English and Chinese cells.

## Scope and Classification

Apply the [scope criteria](README.md#scope-and-terminology). Identify the visual input or feedback, the code artifact, and where the visual signal affects generation or editing. A generic coding model, screenshot-understanding model or GUI navigation agent is not sufficient by itself.

Place each paper once in its most useful reading category. Keep a paper's model, dataset and benchmark assets in the same entry unless a genuinely separate publication warrants its own record. Deduplicate arXiv versions, title changes and conference versions of the same work. Check names carefully: WebSight, Sketch2Code and Web2Code have namesakes or related but distinct works.

The taxonomy may change when the scope changes. Explain the reason and update navigation, counts and registry categories together. Preserve stable `paper-YYMM-NNNNN` audit anchors. Do not inherit the OPD template's topical labels or its inventory-preservation rule.

## Primary Sources and Evidence

1. Open the original paper record or official author/publisher source. Verify the exact title, complete author list and first submission or publication date. Never infer a day from an identifier or a search engine's crawl date.
2. Select an explicit revision dated on or before the catalog cutoff. Record the revision and its date. Check the full-text heading when title metadata conflicts with the paper.
3. Use **A** only after reading primary abstract, metadata and history. Use **M** only after reading the original method/task passages supporting the description, recording the exact sections and versioned link. A search snippet or successful download is neither A nor M.
4. Describe the method, contribution and boundary. Distinguish inference-time critique, offline data construction, supervised refinement and reinforcement-learning rewards. Identify privileged inputs such as DOM, design metadata, reference code or component-library documentation.
5. Label a formal technical report as such only when the source supports that type. A product announcement is **system documentation**, with **D** status and English-only description; do not inflate the paper count with it. An arXiv preprint does not automatically establish peer-review status.
6. Avoid unverified superlatives and isolated leaderboard scores. Any retained number needs the evaluated model, dataset/version, metric, comparison and source table. Distinguish percentage points from relative improvements.
7. If identity or relevance cannot be verified, do not add a counted row. Record the unresolved candidate in a contribution discussion or clearly separated working notes. Be precise about blocked access rather than calling a link dead.

## Entry and Audit Format

Keep the six-column README format. Escape a literal pipe as `\|`; keep one physical line per row and use `<br>` only within cells. Use concise summaries with the same mechanism and qualifications in both languages. The label can be a familiar method name; the audit must contain the full reviewed title and all authors.

```markdown
| Paper and type | First submitted | English | Chinese summary | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Method name**<br>Method paper | YYYY-MM-DD | Mechanism and scope. | Matching Chinese translation. | [arXiv YYMM.NNNNN](https://arxiv.org/abs/YYMM.NNNNN) | [M · v1](docs/SOURCE_AUDIT.md#paper-YYMM-NNNNN) |
```

Use the existing Chinese-summary header in the actual README. Add the matching record to [data/catalog.json](data/catalog.json) and the [source audit](docs/SOURCE_AUDIT.md). The JSON registry stores dates, types, authors, bilingual summaries, evidence locations and retrieval hashes. Hashes record downloaded bytes and must not be invented or interpreted as source-truth certification. A non-arXiv addition requires a stable identifier, an explicit date policy and a corresponding validator update; never fabricate an arXiv ID for format convenience.

For M, cite only the sections actually read. If only a subsection or overview was inspected, say so. For systems, provide official ownership, a source publication or review date, and an immutable revision when obtainable; otherwise disclose a mutable source.

## Open-Source Projects and Research Implementations

Keep documentation-led projects in **Non-Academic Open-Source Projects**, separate from counted papers and hosted products. Explain the actual visual-to-code connection and classify the role: generation/editing, visual selection to source context, or supporting browser infrastructure. A screenshot tool alone is not a complete coding harness.

Inspect the official README and repository license at the same full commit SHA. Add a `systems` registry record with the repository, role, description, review date, pinned README/license URLs and SHA-256 hashes of the downloaded bytes, plus a matching D audit entry. Source availability alone is insufficient for this open-source list; do not place restrictive source-available licenses here without clearly changing the section's scope. Repository license labels do not cover every dependency or hosted service.

Keep paper-associated code in **Research Implementations and Harnesses**, linked to its existing paper record rather than counted again. Store its pinned README and retrieval hash under that entry's `implementation` field. Explain any release/version gap: a public runner does not establish that all paper datasets, scores or models are released. Documentation inspection is not execution validation.

Reviews are cumulative. Record each entry's actual `review_date`; moving the global cutoff must not silently update old review dates or evidence statuses.

## Local Validation

Python 3 standard library is sufficient. Run from the repository root:

```sh
python3 scripts/validate_catalog.py
git diff --check
```

The offline validator checks duplicate IDs/titles, registry–README–audit consistency, category and count totals, calendar dates and cutoff, evidence versions/statuses, table widths, summary language and numeric parity, local links and anchors. It also checks system inventory parity, pinned README/license references and research implementation metadata. It does not prove scientific truth or translation equivalence.

For changed external links, run the separate network check:

```sh
python3 scripts/check_links.py --output docs/link-check.json
python3 scripts/validate_catalog.py --links docs/link-check.json
```

The checker uses bounded public HTTPS GET requests, records HTTP status and redirects, and checks cited HTML fragment IDs when present. It makes no authenticated request and does not download models or datasets. It retries failures once; access errors remain explicit. Link success does not establish correctness of a paper or executable functionality of a project.

Read both language cells side by side, inspect Markdown table formatting, review all changes and update [VALIDATION.md](docs/VALIDATION.md). Do not silently mark unreviewed text as verified. Publishing repository changes requires authorization from the repository owner; this catalog does not require deployment.
