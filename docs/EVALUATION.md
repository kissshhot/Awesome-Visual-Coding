# Evaluation Checklist

Choose a benchmark by the task it measures. Do not aggregate its score with a different benchmark merely because both generate frontend code.

| Research question | Starting entries | Comparison controls |
| --- | --- | --- |
| Can a model reconstruct a static screenshot? | [Design2Code](SOURCE_AUDIT.md#paper-2403-03163), [WebCode2M](SOURCE_AUDIT.md#paper-2404-06369) | Same asset policy, reference images, viewport, browser and fonts; identify whether scripts were removed. |
| Can it interpret rough intent and ask useful questions? | [Sketch2Code](SOURCE_AUDIT.md#paper-2410-16232) | Same user simulator, question budget and feedback access; report direct and interactive settings separately. |
| Can it edit or repair an existing UI? | [DesignBench](SOURCE_AUDIT.md#paper-2506-06251), [MT-Web2Code](SOURCE_AUDIT.md#paper-2608-03474) | Existing code and screenshot availability, instruction specificity, target-region quality and preservation outside that region. |
| Can it produce a runnable project over several turns? | [1D-Bench](SOURCE_AUDIT.md#paper-2602-18548) | Same scaffold, dependencies, tools, failure handling, round limit and design-metadata access. |
| Does it recover interactive behavior? | [Interaction2Code](SOURCE_AUDIT.md#paper-2411-03292), [WebVIA](SOURCE_AUDIT.md#paper-2511-06251) | Same reachable states, transition tests, DOM access and exploration budget; a matching initial screenshot is insufficient. |
| Does code satisfy implementation constraints? | [TaoD2C-Bench](SOURCE_AUDIT.md#paper-2610-10374) | Same library documentation, metadata and supplied requirements; separate requirement inference from realization. |

These are editorial selection questions, not new benchmark results. The linked audit entries identify the source evidence for each task family.

## Before Reporting a Comparison

Record the model/version, prompt, visual inputs, code context, available tools, generation budget and renderer. Disclose whether feedback comes from a human, a model critic, reference-image metrics or runtime errors. A training-only critic is different from a critic available at inference.

Measure at least the outcomes relevant to the task: build/render success, visual fidelity, structure, instruction compliance, preservation of unaffected regions, and interaction tests. A code similarity metric may punish visually equivalent implementations; an image similarity metric may reward nonfunctional replicas. Judge-based assessments require calibration and uncertainty reporting.

For iterative methods, report the initial, final and best-selected candidate separately and explain who can observe the selection signal. Include failed renders rather than dropping them silently. Match rendering calls, token budget or cost when comparing an iterative system with one-shot generation. Claims of improved quality do not automatically imply lower cost or latency.

Check overlap among training corpora, scraped webpages and benchmark sources. Synthetic and real-web data answer different generalization questions. Component-library metadata, ground-truth code, viewport-specific CSS and external assets can change task difficulty substantially.

## Catalog Boundaries

The catalog summarizes source-supported mechanisms; it supplies no unified leaderboard and runs no experiments. Its M status certifies inspection of named passages only. Dataset downloadability, license suitability, reproducibility, security, accessibility, responsive behavior and production readiness remain separate questions.
