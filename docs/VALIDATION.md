# Validation Report

Catalog cutoff and latest review: **2026-10-14**. Research entries span **2016-08-09 to 2026-10-07** by first submission date. Reviewed revisions do not exceed the cutoff. Reviews are cumulative; the registry retains individual review dates.

## Inventory and Source Review

| Category | Research entries |
| --- | --- |
| Surveys | 1 |
| Foundations and Early UI Reconstruction | 2 |
| Datasets and Multimodal Code Models | 5 |
| Layout-Aware and Tool-Grounded Generation | 5 |
| Render-Feedback Optimization | 7 |
| Visual Editing and Interactive Reconstruction | 3 |
| Evaluation Benchmarks | 11 |
| Adjacent Graphics Coding | 2 |
| **Total** | **36** |

The research inventory grew from 28 to **36**: UICoder, DesignCoder, WebMMU, WebGen-V Bench, VISTA, Pattern over Pixels / Pattern2Code, MaLiang-Harness and WebUIProof were added after primary-record and selected-section review. The source audit now records **26 M** and **10 A** research entries. Previous A records have not been upgraded without method review.

The new non-academic section contains **6 open-source projects**: screenshot-to-code (moved from the former system list and repinned), Onlook, stagewise, React Grab, Playwright MCP and Chrome DevTools MCP. All have commit-pinned README/license sources and retrieval hashes. Stitch remains **1 hosted system resource**, for **7 D system resources** in total. Four paper-associated implementation READMEs are separately indexed under their existing research entries; they do not increase either count.

The bilingual additions were reviewed side by side for matching inputs, mechanisms and qualifications. Checks covered native versus Web UI scope, screenshot input versus training feedback, design metadata, constrained code completion, visual judges versus execution tests, and graphics-only harnesses. VISTA's title and author metadata conflict was resolved against its v4 title block. No quantitative performance claims were added. No separate translation reviewer was used.

## Automated Results

See the saved [validator output](validation-output.txt). The checks cover:

- Unique research IDs and normalized titles, with matching JSON registry, README rows and audit records.
- Complete listed authors, matching submission/revision dates, review dates and cutoff consistency.
- Evidence status/version agreement, pinned method URLs and retrieval-hash formats.
- Research table shape, bilingual language presence and numeric parity.
- System inventory and description parity, source revisions, README/license URLs and hash formats.
- Paper implementation documentation, scope-note parity and pinned sources.
- Local files, anchors, navigation, category and displayed totals.
- Python syntax compilation and Git whitespace checks.

The public [link-check report](link-check.json), finalized at **2026-10-14T13:56:15+00:00**, records **86 unique external HTTPS URLs**, all returning HTTP 200, and **26 cited HTML fragments**, all present. There are **0 unresolved links** and **0 redirects**. Four arXiv HTML requests failed with transient connection closures in the initial pass and succeeded in a targeted retry; successful first-pass observations retain their original timestamps.

HTTP and fragment checks are separate from content review. They do not prove source truth, executable behavior or future uptime; bounded GET requests do not download models or datasets.

## Reproduction Commands

Run from the repository root with Python 3:

```sh
python3 scripts/validate_catalog.py --links docs/link-check.json
python3 scripts/check_links.py --output docs/link-check.json
python3 -m py_compile scripts/validate_catalog.py scripts/check_links.py
git diff --check
```

The first command validates the saved link report offline. The second makes new network requests and updates observations; `--retry-failed` retains successful observations with their original timestamps. Commands do not install projects, call model APIs or publish repository changes.

## Review Limits

This is a selective expansion, not an exhaustive survey. M certifies inspection of named passages, not full-paper or experimental verification. Public code availability does not establish complete release of paper datasets, training pipelines, scores or platform support; the implementation index records observed gaps. No model, benchmark, dataset or listed system was installed or run. Repository license labels describe reviewed files, not a dependency or hosted-service license audit.
