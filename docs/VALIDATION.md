# Validation Report

Catalog cutoff and review date: **2026-10-10**. Initial research range: **2016-08-09 to 2026-10-07** by first submission date. Reviewed revisions can be newer than their first submissions but do not exceed the cutoff.

## Inventory and Source Review

| Category | Research entries |
| --- | --- |
| Surveys | 1 |
| Foundations and Early UI Reconstruction | 2 |
| Datasets and Multimodal Code Models | 5 |
| Layout-Aware and Tool-Grounded Generation | 4 |
| Render-Feedback Optimization | 5 |
| Visual Editing and Interactive Reconstruction | 3 |
| Evaluation Benchmarks | 7 |
| Adjacent Image-to-Graphics Research | 1 |
| **Total** | **28** |

There are also **2 official system resources**, excluded from the research count. The [source audit](SOURCE_AUDIT.md) records **18 M**, **10 A** and **2 D** checks. All research entries have primary-source identity, author, abstract and date checks. M adds selected original method/task passages; no entry represents an experimental reproduction or whole-paper certification.

The bilingual cells were reviewed side by side for matching inputs, mechanisms and scope. Particular checks covered synthetic versus real-web data, restricted DSLs, text-started visual refinement, training versus inference feedback, metadata-assisted benchmarks, localized-edit preservation and graphics-only evaluation. No quantitative performance claims were retained. A separate translation reviewer was not used.

## Automated Results

The following checks passed; see the saved [validator output](validation-output.txt):

- **28 unique research IDs and normalized titles**, with matching JSON registry, README rows and audit records.
- Complete listed authors, matching first submission and revision dates, valid calendar dates, and no reviewed revision beyond the cutoff.
- Evidence status/version agreement, pinned method URLs and retrieval-hash formats.
- Six-column research tables, consistent remaining table widths, bilingual language presence and numeric parity.
- Local files, explicit and generated anchors, navigation, category counts and displayed totals.
- Python syntax compilation of both scripts and staged Git whitespace checking.

The public [link-check report](link-check.json), finalized at **2026-10-10 10:54:39 UTC**, records **48 unique external HTTPS URLs**, all returning HTTP 200, and **18 cited HTML fragments**, all present. There were **0 unresolved links** and **0 redirects**. One request in the initial pass needed its built-in retry. Successful observations from that pass were retained when checking the added Interaction2Code URL; each observation retains its own timestamp.

These are GET/fragment checks, not proof of source truth, dataset availability, executable project behavior or future uptime. The checker reads a bounded response body and does not follow links to datasets or model weights.

## Reproduction Commands

Run from the repository root with Python 3:

```sh
python3 scripts/validate_catalog.py --links docs/link-check.json
python3 scripts/check_links.py --output docs/link-check.json
git diff --check
git diff --cached --check
```

The saved report can be validated offline. The second command performs a new network check and updates timestamps. Neither command creates a remote or uploads repository content.

## Delivery and Limits

The repository was initialized independently on `main`. The initial local delivery was subsequently approved for publication as the public GitHub repository `kissshhot/Awesome-Visual-Coding`. Publication preparation included a tracked-file privacy review and replacement of the unpublished commit's work-email identity with the owner's GitHub noreply identity. The Awesome-OPD reference was accessed through read-only commands at `5d575fc3709c341310e93573daeea9ccdf746425`; its files were not edited. No PR, deployment or user-memory update is part of this delivery.

No delivery blocker remains. The screenshot-to-code official README is a mutable default-branch source; the attempted public commit lookup did not yield an immutable revision. That limitation is visible in both the entry and audit. Ten A papers still lack method-level review; M papers have the explicitly named selected-section review only. No model, benchmark, dataset or system was installed or run, and no security, license, accessibility or production-readiness assurance is implied.
