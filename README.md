# Awesome Visual Coding

A curated research catalog on **visual inputs for code generation** and **visual feedback for programming**, centered on screenshot/design-to-code, UI reconstruction, visual editing, render-and-refine methods, and their evaluation.

**36 research entries** · **6 non-academic open-source projects** · **1 hosted system resource** · **Cutoff and latest review: 2026-10-14** · **English and Chinese research summaries**

[Table of contents](#table-of-contents) · [Scope and terminology](#scope-and-terminology) · [Source audit](docs/SOURCE_AUDIT.md) · [Validation report](docs/VALIDATION.md) · [Contributing](CONTRIBUTING.md)

## Scope and Terminology

An entry qualifies when a visual artifact (screenshot, design, sketch, rendered output or direct visual manipulation) materially informs the generation or modification of an executable program. HTML/CSS, JSX and UI-specific intermediate languages count as code representations here. Visual feedback can operate during inference, data construction or model training; these are different mechanisms.

The core is web/UI coding, with selected native-UI work on Android, SwiftUI and React Native. Sketch-n-Sketch, IR4RL and MaLiang-Harness provide bounded connections to direct source editing, rendering-based supervision and graphics harnesses. This is a selective research map, not a systematic review or a claim of exhaustive coverage through the cutoff.

**Excluded:** block-based educational programming; generic text-only coding assistants; GUI navigation or computer-use agents without code generation; screenshot understanding alone; pixel-only image generation; and broad CAD, robotics, chart, slide, game or SVG generation catalogs. Pure design-metadata-to-code tools without a meaningful visual input or feedback component are also outside the core. A method beginning with text remains eligible if rendered visual feedback actually guides coding.

In the implementation listings, a **tool** exposes operations such as element selection, screenshots or browser interaction. A **harness** coordinates tasks, code execution, observations, feedback and evaluation around an agent. Browser tools can be components of a harness without implementing that complete loop.

Visual similarity, code structure, successful rendering and interaction correctness are separate outcomes. A static screenshot does not uniquely specify responsive behavior, hidden UI states, accessibility or business logic. No entry is endorsed as production-ready.

## Reading the Entries

- The six-column layout follows the pinned Awesome-OPD template, with a new topic-specific taxonomy. Each paper appears once; related models, datasets and benchmark assets stay with their originating paper.
- **First submitted** comes from the arXiv submission history, not its identifier, acceptance date or latest revision. Only revisions dated on or before the cutoff are reviewed. Full titles, all listed authors and exact revisions are in the audit.
- Reviews are cumulative: per-entry dates in the registry distinguish the initial 2026-10-10 review from the 2026-10-14 additions. Moving the cutoff does not imply every earlier paper was reread.
- **A**: primary-source abstract, author/title metadata and submission history inspected. **M**: those checks plus the specific full-text method or task sections named in the audit. **D**: official system documentation inspected. Downloading a paper alone does not earn M.
- Types describe contributions: method/model papers, dataset papers, benchmark papers, surveys and system papers. An arXiv listing is not proof of peer review. Official product announcements are system documentation, not technical reports. No separately designated technical report was selected in this edition; future technical reports require the same bilingual format and evidence.
- English and Chinese summaries have matching mechanisms and scope qualifications. No experimental score, state-of-the-art ranking, package functionality or dataset release is independently certified.

## Table of Contents

- [Surveys](#surveys)
- [Foundations and Early UI Reconstruction](#foundations-and-early-ui-reconstruction)
- [Datasets and Multimodal Code Models](#datasets-and-multimodal-code-models)
- [Layout-Aware and Tool-Grounded Generation](#layout-aware-and-tool-grounded-generation)
- [Render-Feedback Optimization](#render-feedback-optimization)
- [Visual Editing and Interactive Reconstruction](#visual-editing-and-interactive-reconstruction)
- [Evaluation Benchmarks](#evaluation-benchmarks)
- [Adjacent Graphics Coding](#adjacent-graphics-coding)
- [Research Implementations and Harnesses](#research-implementations-and-harnesses)
- [Non-Academic Open-Source Projects](#non-academic-open-source-projects)
- [Official System Resources](#official-system-resources)
- [Reading Routes](#reading-routes)
- [Contributing](#contributing)

## Surveys

A broader map of the field; its full scope is wider than this catalog.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Beyond NL2Code**<br>Survey | 2026-06-14 | Organizes multimodal code intelligence by the role of code and by application domain, including UI generation, scientific visualization and structured graphics. Its discussion of semantic and interaction evidence provides a broader context than this UI-centered catalog. | 按代码的作用和应用领域梳理多模态代码智能，涵盖 UI 生成、科学可视化和结构化图形。其对语义与交互证据的讨论，为本目录以 UI 为中心的范围提供更广泛的背景。 | [arXiv 2606.15932](https://arxiv.org/abs/2606.15932) | [A · v3](docs/SOURCE_AUDIT.md#paper-2606-15932) |

## Foundations and Early UI Reconstruction

Early image-to-UI approaches and their restricted representations.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **pix2code**<br>Method paper | 2017-05-22 | Combines a CNN image encoder with recurrent language modeling to predict a lightweight GUI-specific language from a screenshot. The representation targets layout and component relationships and ignores actual label text, so it should not be read as unrestricted webpage reconstruction. | 结合 CNN 图像编码器与循环语言模型，从截图预测轻量的 GUI 专用语言。该表示关注布局与组件关系，并忽略标签的实际文本，因此不应将其视为不受限制的网页重建。 | [arXiv 1705.07962](https://arxiv.org/abs/1705.07962) | [M · v2](docs/SOURCE_AUDIT.md#paper-1705-07962) |
| **ReDraw**<br>System paper | 2018-02-07 | Detects GUI components from mockup metadata or images, classifies their types with a CNN trained on mined app data, and assembles a hierarchy using a nearest-neighbor approach. The implemented system targets Android GUI prototypes, rather than complete application behavior. | 从设计稿元数据或图像中检测 GUI 组件，用基于挖掘所得应用数据训练的 CNN 识别组件类型，再通过近邻方法组装层级结构。所实现系统面向 Android GUI 原型，而非完整应用行为。 | [arXiv 1802.02312](https://arxiv.org/abs/1802.02312) | [M · v2](docs/SOURCE_AUDIT.md#paper-1802-02312) |

## Datasets and Multimodal Code Models

Training resources and models that connect screenshots, rendered artifacts and source code.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **WebSight**<br>Dataset paper | 2024-03-14 | Builds screenshot–HTML training pairs by generating website concepts, synthesizing HTML with Tailwind CSS, filtering outputs and rendering pages. It demonstrates VLM fine-tuning on synthetic data; this is a training resource, not a real-world reconstruction benchmark. | 通过生成网站构想、合成带 Tailwind CSS 的 HTML、过滤输出并渲染页面，构建截图与 HTML 训练对。论文展示了在合成数据上微调 VLM；这是训练资源，而非真实网页重建基准。 | [arXiv 2403.09029](https://arxiv.org/abs/2403.09029) | [M · v1](docs/SOURCE_AUDIT.md#paper-2403-09029) |
| **WebCode2M / WebCoder**<br>Dataset paper | 2024-04-09 | Curates real-web screenshot, code and layout data through code purification, rendering and quality filtering. Introduces the WebCoder baseline and TreeBLEU for structural hierarchy recall; cleaned static pages do not preserve every behavior of the original websites. | 通过代码清理、渲染和质量过滤，整理真实网页的截图、代码及布局数据。提出 WebCoder 基线和用于结构层级召回的 TreeBLEU；清理后的静态页面并不保留原网站的全部行为。 | [arXiv 2404.06369](https://arxiv.org/abs/2404.06369) | [M · v2](docs/SOURCE_AUDIT.md#paper-2404-06369) |
| **Web2Code**<br>Dataset and benchmark paper | 2024-06-28 | Uses language models to expand webpage–code data and adds question–answer pairs about webpage content. Couples instruction-tuning data with evaluations of webpage understanding and screenshot-to-HTML generation, keeping these two capabilities distinct. | 利用语言模型扩充网页与代码数据，并加入关于网页内容的问答对。将指令微调数据与网页理解、截图到 HTML 生成评测结合，同时区分这两种能力。 | [arXiv 2406.20098](https://arxiv.org/abs/2406.20098) | [A · v2](docs/SOURCE_AUDIT.md#paper-2406-20098) |
| **Flame**<br>Model and dataset paper | 2025-03-03 | Synthesizes frontend training data by extracting self-contained components, rendering them and generating descriptions, with evolution, waterfall and additive synthesis strategies. Trains a vision-language model for image-and-instruction-to-React generation and studies interpretation before coding. | 通过提取自包含组件、渲染组件并生成描述来合成前端训练数据，并采用演化式、瀑布式和增量式合成策略。训练视觉语言模型完成图像与指令到 React 的生成，并研究先理解图像再编码的方式。 | [arXiv 2503.01619](https://arxiv.org/abs/2503.01619) | [A · v1](docs/SOURCE_AUDIT.md#paper-2503-01619) |
| **JanusCoder / JanusCoderV**<br>Model and dataset paper | 2025-10-27 | Introduces a multimodal code synthesis toolkit and corpus spanning charts, interactive web UIs and code-driven animation. The model family supports text and visual coding settings; this entry includes the visual branch and does not equate every model variant with a vision-capable model. | 提出多模态代码合成工具与语料，涵盖图表、交互式网页 UI 和代码驱动的动画。该模型系列支持文本与视觉编程场景；本条目收录其视觉分支，不将每个模型变体都视为具备视觉能力。 | [arXiv 2510.23538](https://arxiv.org/abs/2510.23538) | [A · v3](docs/SOURCE_AUDIT.md#paper-2510-23538) |

## Layout-Aware and Tool-Grounded Generation

Decomposition, explicit layout reasoning and visual evidence extraction before code synthesis.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **DCGen**<br>Method paper | 2024-06-24 | Recursively divides a screenshot along visual separation lines, generates code for the resulting segments, and assembles child implementations into the full page. The reviewed revision uses segment-level code generation, which differs from the descriptions-first account in earlier versions. | 沿视觉分隔线递归划分截图，为得到的子区域生成代码，再将子区域实现组装成完整页面。所核验版本采用子区域级代码生成，与早期版本先生成描述的表述不同。 | [arXiv 2406.16386](https://arxiv.org/abs/2406.16386) | [M · v3](docs/SOURCE_AUDIT.md#paper-2406-16386) |
| **DesignCoder**<br>Method paper | 2025-06-16 | Combines screenshots with design metadata to group UI regions, infer component hierarchies and generate React Native code. Uses Appium screenshots and component attributes for localized visual comparison and repair before merging components. Event-handler bodies are left unspecified, so visual reconstruction does not establish complete application behavior. | 结合截图与设计元数据划分 UI 区域、推断组件层级并生成 React Native 代码。利用 Appium 截图及组件属性进行局部视觉比较与修复，再合并组件。事件处理函数体未被具体实现，因此视觉重建不能证明完整的应用行为。 | [arXiv 2506.13663](https://arxiv.org/abs/2506.13663) | [M · v1](docs/SOURCE_AUDIT.md#paper-2506-13663) |
| **ScreenCoder**<br>Method and system paper | 2025-07-30 | Separates screenshot-to-code into visual grounding, layout planning and code generation using specialized agents. Also uses the pipeline to synthesize image–code pairs for supervised fine-tuning and reinforcement learning of an open model. | 借助专门的智能体，将截图到代码拆分为视觉定位、布局规划和代码生成。还利用该流程合成图像与代码对，以对开放模型进行监督微调和强化学习。 | [arXiv 2507.22827](https://arxiv.org/abs/2507.22827) | [A · v2](docs/SOURCE_AUDIT.md#paper-2507-22827) |
| **LaTCoder**<br>Method paper | 2025-08-05 | Divides webpage designs into image blocks and uses Layout-as-Thought prompting to generate their code. It compares absolute-position and model-based assembly through dynamic selection, and introduces CC-HARD to study complex layouts. | 将网页设计划分为图像块，并通过 Layout-as-Thought 提示生成各块代码。借助动态选择比较绝对定位与模型驱动的组装方式，并引入 CC-HARD 研究复杂布局。 | [arXiv 2508.03560](https://arxiv.org/abs/2508.03560) | [A · v1](docs/SOURCE_AUDIT.md#paper-2508-03560) |
| **WidgetGen**<br>Method paper | 2026-08-12 | Extracts visible text and color evidence, performs layout and optional chart reasoning, then directly generates JSX for individual widgets. Its focus is selective tool grounding at widget scale, rather than assuming a fixed component schema or full-site reconstruction. | 提取可见文本与颜色证据，进行布局及可选的图表推理，再直接为单个组件生成 JSX。其重点是在组件尺度上选择性地借助工具获取依据，而非假定固定组件模式或重建完整网站。 | [arXiv 2608.12611](https://arxiv.org/abs/2608.12611) | [A · v1](docs/SOURCE_AUDIT.md#paper-2608-12611) |

## Render-Feedback Optimization

Inference-time critique, learned refinement and reinforcement learning from rendered results.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **UICoder**<br>Method and model paper | 2024-06-11 | Improves text-to-SwiftUI generation by compiling and rendering self-generated candidates, then using visual scores and deduplication to filter training data and guide preference learning. The visual signal acts during data selection and model training; inference does not require a reference screenshot. | 通过编译和渲染自行生成的候选代码，再利用视觉评分和去重筛选训练数据、引导偏好学习，改进文本到 SwiftUI 的生成。视觉信号作用于数据选择与模型训练阶段；推理不要求输入参考截图。 | [arXiv 2406.07739](https://arxiv.org/abs/2406.07739) | [M · v1](docs/SOURCE_AUDIT.md#paper-2406-07739) |
| **ReLook**<br>Method paper | 2025-10-13 | Trains a coding agent with screenshot-based rewards and actionable feedback from a multimodal critic, rejecting non-improving revisions through Forced Optimization. The described inference procedure removes the critic and uses self-editing, so training-time visual feedback is not continuous inference-time critique. | 使用基于截图的奖励及多模态评审器提供的可执行反馈训练编程智能体，并通过 Forced Optimization 拒绝未带来改进的修订。所述推理流程移除评审器并采用自编辑，因此训练期视觉反馈不等同于推理期持续视觉评审。 | [arXiv 2510.11498](https://arxiv.org/abs/2510.11498) | [A · v1](docs/SOURCE_AUDIT.md#paper-2510-11498) |
| **WebGen-V Bench**<br>Benchmark and framework paper | 2025-10-17 | Decomposes webpages into sections and constructs grounded design instructions from page structure and visual evidence. Evaluates generated sections against those instructions with a multimodal judge and supports targeted refinement from low-scoring sections. This is instruction-grounded visual assessment, not pixel matching against a reference screenshot. | 将网页分解为区块，并根据页面结构与视觉证据构建设计指令。使用多模态评审器对照指令评估生成的区块，支持依据低分区块进行针对性修订。这属于基于指令的视觉评估，而非与参考截图逐像素匹配。 | [arXiv 2510.15306](https://arxiv.org/abs/2510.15306) | [M · v1](docs/SOURCE_AUDIT.md#paper-2510-15306) |
| **UI2Code^N**<br>Method and model paper | 2025-11-11 | Frames drafting, polishing and localized editing as code updates conditioned on visual execution feedback. The reviewed revision introduces Relative Visual Policy Optimization, learning from relative preferences between rendered candidates instead of relying on calibrated absolute visual scores. | 将初稿生成、润色和局部编辑建模为以视觉执行反馈为条件的代码更新。所核验版本提出相对视觉策略优化，从渲染候选之间的相对偏好学习，而非依赖经过校准的绝对视觉分数。 | [arXiv 2511.08195](https://arxiv.org/abs/2511.08195) | [M · v4](docs/SOURCE_AUDIT.md#paper-2511-08195) |
| **VisRefiner**<br>Method paper | 2026-02-05 | Aligns differences between target and rendered screenshots with corrective code through supervised refinement pairs. A subsequent reinforcement-learning stage uses visual improvement to learn self-refinement, connecting code changes to their rendered consequences during training. | 通过监督式修订样本，将目标截图与渲染截图之间的差异同纠正代码对齐。后续强化学习阶段利用视觉改进学习自修订，在训练中建立代码变化与其渲染结果之间的联系。 | [arXiv 2602.05998](https://arxiv.org/abs/2602.05998) | [M · v1](docs/SOURCE_AUDIT.md#paper-2602-05998) |
| **Vision-Guided Iterative Refinement**<br>Method paper | 2026-04-07 | Renders code from a natural-language request, obtains visual critique, translates that critique into code-level advice, and iteratively revises the implementation. Retains the best judged candidate and studies LoRA distillation; the visual signal is output feedback rather than a required reference screenshot. | 渲染根据自然语言请求生成的代码，获取视觉评审，将其转化为代码层面的建议，再迭代修改实现。保留评审得分最高的候选并研究 LoRA 蒸馏；视觉信号来自输出反馈，而非必须提供的参考截图。 | [arXiv 2604.05839](https://arxiv.org/abs/2604.05839) | [M · v1](docs/SOURCE_AUDIT.md#paper-2604-05839) |
| **RubSE**<br>Method paper | 2026-08-25 | Addresses visual repair coupling, where a local code edit can damage other rendered regions. Generates typed repair rubrics, selects one priority and records repair history to guide iterative UI refinement; rubric conditioning does not impose hard preservation guarantees. | 针对视觉修复耦合问题：局部代码编辑可能破坏其他渲染区域。生成带类型的修复准则、选择一个优先目标并记录修复历史，以引导 UI 迭代改进；以准则为条件并不构成严格的区域保留保证。 | [arXiv 2608.24138](https://arxiv.org/abs/2608.24138) | [M · v1](docs/SOURCE_AUDIT.md#paper-2608-24138) |

## Visual Editing and Interactive Reconstruction

Human visual edits and reconstruction of interfaces with multiple observable states.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Sketch-n-Sketch**<br>System paper | 2016-08-09 | Lets users draw, relate and group shapes while transforming an exposed general-purpose program that renders SVG. This foundational direct-manipulation workflow creates reusable abstractions and edits source programs; it is not a block-based programming language or a neural screenshot model. | 允许用户绘制、关联与分组形状，同时变换向用户开放、用于渲染 SVG 的通用程序。这一早期直接操控流程能创建可复用抽象并修改源程序；它不是积木式编程语言，也不是神经截图模型。 | [arXiv 1608.02829](https://arxiv.org/abs/1608.02829) | [M · v1](docs/SOURCE_AUDIT.md#paper-1608-02829) |
| **Code Shaping**<br>Interaction and system paper | 2025-02-06 | Uses free-form sketches over code and console or graphical output to communicate intended edits to an AI interpreter. Its design studies examine iterative reconciliation between sketches, model interpretations and source edits, rather than one-shot conversion of a UI mockup. | 使用覆盖在代码、控制台或图形输出上的自由形式草图，向 AI 解释器表达预期修改。其设计研究考察草图、模型解释与源码编辑之间的迭代协调，而非一次性地将 UI 设计稿转换为代码。 | [arXiv 2502.03719](https://arxiv.org/abs/2502.03719) | [M · v2](docs/SOURCE_AUDIT.md#paper-2502-03719) |
| **WebVIA**<br>System and model paper | 2025-11-09 | Explores rendered webpages with screenshot and DOM observations to collect UI states, generates interactive frontend code, and validates transitions. Its controlled synthetic environment and multi-state reconstruction distinguish it from single-screenshot static replication and general web-navigation benchmarks. | 利用截图与 DOM 观察探索渲染网页、收集 UI 状态，生成交互式前端代码并验证状态转换。其受控合成环境与多状态重建，有别于单截图静态复现及通用网页导航基准。 | [arXiv 2511.06251](https://arxiv.org/abs/2511.06251) | [M · v1](docs/SOURCE_AUDIT.md#paper-2511-06251) |

## Evaluation Benchmarks

Different inputs, outputs and success criteria; these benchmarks are not interchangeable.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **Design2Code**<br>Benchmark paper | 2024-03-05 | Evaluates screenshot-to-webpage reconstruction on curated real webpages using rendered visual similarity and element-level matching, complemented by human evaluation. Its metrics diagnose missing elements and layout errors; static visual fidelity does not establish interactive correctness. | 在整理后的真实网页上评测截图到网页重建，采用渲染视觉相似度与元素级匹配，并辅以人工评估。其指标用于诊断元素缺失和布局错误；静态视觉保真度并不能证明交互正确。 | [arXiv 2403.03163](https://arxiv.org/abs/2403.03163) | [M · v3](docs/SOURCE_AUDIT.md#paper-2403-03163) |
| **Sketch2Code**<br>Benchmark paper | 2024-10-21 | Tests conversion of rough sketches into webpage prototypes and supports multi-turn evaluation with a simulated user. Separates passive feedback following from proactive clarification questions, making it relevant to interactive design rather than only high-fidelity screenshot matching. | 测试将粗略草图转换为网页原型，并支持与模拟用户进行多轮评测。区分被动遵循反馈与主动提出澄清问题，因此适用于交互式设计，而不仅是高保真截图匹配。 | [arXiv 2410.16232](https://arxiv.org/abs/2410.16232) | [A · v1](docs/SOURCE_AUDIT.md#paper-2410-16232) |
| **Interaction2Code**<br>Benchmark paper | 2024-11-05 | Benchmarks interactive webpage generation from visual prototypes using automatic and human assessment. Studies interaction-specific failure modes and enhancement strategies such as element highlighting and combined visual–textual descriptions; static appearance alone is not its evaluation target. | 通过自动与人工评估，测试根据视觉原型生成交互式网页。研究交互特有的失效模式，以及元素高亮、视觉与文本描述结合等增强策略；其评测目标不限于静态外观。 | [arXiv 2411.03292](https://arxiv.org/abs/2411.03292) | [A · v3](docs/SOURCE_AUDIT.md#paper-2411-03292) |
| **DesignBench**<br>Benchmark paper | 2025-06-06 | Evaluates generation, instruction-driven editing and visual-issue repair across React, Vue, Angular and vanilla HTML/CSS. Task inputs differ: editing uses an existing image, code and instruction, whereas repair uses problematic code and its rendered image. | 在 React、Vue、Angular 和原生 HTML/CSS 上评测生成、指令驱动编辑及视觉问题修复。各任务输入不同：编辑使用已有图像、代码与指令，修复则使用有问题的代码及其渲染图像。 | [arXiv 2506.06251](https://arxiv.org/abs/2506.06251) | [M · v3](docs/SOURCE_AUDIT.md#paper-2506-06251) |
| **WebMMU**<br>Benchmark paper | 2025-08-22 | Benchmarks multilingual website understanding alongside mockup/sketch-to-HTML/CSS generation and instruction-driven code edits using screenshots and existing source. The code-generation tasks belong in this catalog; the accompanying visual question-answering tasks measure a separate capability and should not be treated as evidence of executable reconstruction. | 在评测多语言网站理解的同时，评测设计稿或草图到 HTML/CSS 的生成，以及基于截图和现有源码的指令式代码编辑。代码生成任务属于本目录范围；配套的视觉问答任务衡量另一种能力，不应被当作可执行重建的证据。 | [arXiv 2508.16763](https://arxiv.org/abs/2508.16763) | [M · v1](docs/SOURCE_AUDIT.md#paper-2508-16763) |
| **1D-Bench**<br>Benchmark paper | 2026-02-20 | Tests executable React projects from a reference rendering plus a potentially defective design intermediate representation under a fixed toolchain. Multi-round feedback includes renders, difference heatmaps or failure logs; evaluation separates rendering success from visual similarity. | 在固定工具链下，测试根据参考渲染图与可能含缺陷的设计中间表示生成可执行 React 项目。多轮反馈包含渲染图、差异热图或失败日志；评测区分渲染成功率与视觉相似度。 | [arXiv 2602.18548](https://arxiv.org/abs/2602.18548) | [M · v3](docs/SOURCE_AUDIT.md#paper-2602-18548) |
| **VISTA**<br>Benchmark paper | 2026-05-22 | Evaluates agents that build multi-page applications from visual design handoffs and specifications. The reviewed revision covers Web and Android, combining component localization with behavioral execution and a joint score. Screenshots, structured design metadata and text are distinct input conditions; visual similarity alone does not establish functioning applications. | 评测智能体根据视觉设计交付物与规格构建多页面应用的能力。所核验版本覆盖 Web 与 Android，将组件定位、行为执行及联合评分结合。截图、结构化设计元数据和文本是不同的输入条件；仅有视觉相似度不能证明应用能够正常运行。 | [arXiv 2605.26144](https://arxiv.org/abs/2605.26144) | [M · v4](docs/SOURCE_AUDIT.md#paper-2605-26144) |
| **MT-Web2Code**<br>Benchmark paper | 2026-08-04 | Constructs multi-turn regional reconstruction and localized modification tasks by corrupting golden webpages and reversing those trajectories. Evaluates target repair together with preservation of unaffected content, exposing cumulative editing errors; it is distinct from the earlier Web2Code dataset. | 通过破坏标准网页并逆转这些轨迹，构建多轮区域重建与局部修改任务。同时评测目标修复和未受影响内容的保留，以揭示累积编辑错误；它与较早的 Web2Code 数据集不同。 | [arXiv 2608.03474](https://arxiv.org/abs/2608.03474) | [M · v1](docs/SOURCE_AUDIT.md#paper-2608-03474) |
| **Pattern over Pixels / Pattern2Code**<br>Benchmark and analysis paper | 2026-08-04 | Perturbs individual elements in repeated webpage patterns and asks models to recover masked style values from screenshots, supplied HTML and a location description. Tests whether visual evidence overrides pattern-completion bias. This is constrained code completion with substantial source context, not unrestricted screenshot-to-page generation. | 对网页重复模式中的单个元素施加扰动，要求模型根据截图、给定 HTML 和位置描述恢复被遮蔽的样式值。测试视觉证据能否克服模式补全偏差。这是提供大量源码上下文的受限代码补全，而非不受限制的截图到页面生成。 | [arXiv 2608.03691](https://arxiv.org/abs/2608.03691) | [M · v1](docs/SOURCE_AUDIT.md#paper-2608-03691) |
| **WebUIProof**<br>Benchmark and training method paper | 2026-10-02 | Uses a UI-agent execution harness to test generated websites through interaction and assertions, observing both DOM and visual state. Its VisRL method combines build/runtime, visual-quality and interaction-test feedback to train a code generator. Generation starts from text specifications; inclusion rests on visual assessment and training feedback, not screenshot-conditioned input. | 使用 UI 智能体执行 harness，通过交互与断言测试生成的网站，同时观察 DOM 和视觉状态。其 VisRL 方法结合构建与运行、视觉质量及交互测试反馈来训练代码生成器。生成从文本规格开始；收录依据是视觉评估和训练反馈，而非以截图为条件的输入。 | [arXiv 2610.02617](https://arxiv.org/abs/2610.02617) | [M · v1](docs/SOURCE_AUDIT.md#paper-2610-02617) |
| **TaoD2C-Bench**<br>Benchmark paper | 2026-10-07 | Tests industrial UI generation from design images, layer metadata and target-library documentation. Separates end-to-end generation, requirement inference and requirement realization, evaluating implementation constraints separately from visual fidelity. | 测试根据设计图像、图层元数据与目标组件库文档生成工业级 UI。区分端到端生成、需求推断与需求实现，并将实现约束评测与视觉保真度评测分开。 | [arXiv 2610.10374](https://arxiv.org/abs/2610.10374) | [M · v1](docs/SOURCE_AUDIT.md#paper-2610-10374) |

<a id="adjacent-image-to-graphics-research"></a>

## Adjacent Graphics Coding

A bounded extension for rendering-based supervision and programmable graphics harnesses; no claim of comprehensive graphics coverage.

| Paper and type | First submitted | English | 中文 | Source | Checked |
| --- | --- | --- | --- | --- | --- |
| **MaLiang-Harness**<br>System paper | 2026-09-28 | Organizes image and animation generation around persistent executable programs, iterative rendering and visual feedback. Associates edits and verification artifacts with program revisions, supports restoration, and rechecks the current revision before delivery. Its graphics harness informs code-driven visual workflows; it does not establish frontend UI reconstruction results. | 以持久化可执行程序、迭代渲染和视觉反馈组织图像与动画生成。将编辑及验证产物关联到程序版本，支持恢复，并在交付前重新检查当前版本。其图形生成 harness 可为代码驱动的视觉工作流提供参考，但不能证明前端 UI 重建效果。 | [arXiv 2609.34309](https://arxiv.org/abs/2609.34309) | [M · v1](docs/SOURCE_AUDIT.md#paper-2609-34309) |
| **IR4RL**<br>Method paper | 2026-09-28 | Turns changes between intermediate rendered code prefixes into localized reinforcement-learning rewards and combines them with a final-output signal. Evaluated on image-to-SVG and image-to-TikZ; the rendering-supervision idea is relevant, but the paper does not establish frontend UI results. | 将代码前缀的中间渲染结果之间的变化转化为局部强化学习奖励，并与最终输出信号结合。评测面向图像到 SVG 和图像到 TikZ；其渲染监督思想具有相关性，但论文并未证明其前端 UI 效果。 | [arXiv 2609.34587](https://arxiv.org/abs/2609.34587) | [M · v1](docs/SOURCE_AUDIT.md#paper-2609-34587) |

## Research Implementations and Harnesses

Official code linked to papers already counted above. These are selected implementation entry points, not additional research entries or execution-tested reproductions. The linked README snapshots were inspected on 2026-10-14; paper evidence and code-release scope are distinct.

| Paper | Implementation role | Documented entry points and release limits | Pinned official source |
| --- | --- | --- | --- |
| [WebGen-V Bench](docs/SOURCE_AUDIT.md#paper-2510-15306) | Section-based visual evaluation and refinement | Documents `run_demo.py` and `pipeline/eval_run.py` for build, generation, evaluation and refinement. This snapshot defaults to Gemini; only a sample URL list ships, with the full list available on request. | [sony/web_gen_v_bench · cd13ad8](https://github.com/sony/web_gen_v_bench/blob/cd13ad84315375bc97238bd0b1db7b5420417079/README.md) |
| [VISTA](docs/SOURCE_AUDIT.md#paper-2605-26144) | Coding-agent execution and application evaluation | Documents `tasks/run_eval.sh`, per-CLI wrappers and Docker-based localization/behavior scoring. The reviewed README describes the Web runner; it does not establish release of the Android evaluation added in paper v4. | [kaboider/VISTA_Bench · dce2756](https://github.com/kaboider/VISTA_Bench/blob/dce2756fdeca450310af91034e78bd57203a001a/README.md) |
| [MaLiang-Harness](docs/SOURCE_AUDIT.md#paper-2609-34309) | Revision-aware graphics generation harness | Documents CLI/UI generation, render/inspect/revise tools and `python -m benchmarks`. The public release excludes the complete paper datasets, historical results and full visual-scoring pipeline. | [gulucaptain/MaLiang-Harness · c811b47](https://github.com/gulucaptain/MaLiang-Harness/blob/c811b47f63ff1748d85b2dc2e9c4169385d4b46f/README.md) |
| [WebUIProof](docs/SOURCE_AUDIT.md#paper-2610-02617) | UI-agent interaction testing harness | Documents generation, project building, hosting and VLM-driven UI tests under `src/ui_test_llama/`. The README describes the general-WebUI subset; it does not establish release of every paper task or the complete VisRL training pipeline. | [yunyuntsai/webuiproof-benchmark · fa59898](https://github.com/yunyuntsai/webuiproof-benchmark/blob/fa59898a5305672cdb28b29965cb87bca4204438/README.md) |

## Non-Academic Open-Source Projects

Documentation-led implementations, separate from the research count. No associated paper is used as the basis for these entries; paper-associated code belongs in the research implementation index. Each row records the reviewed commit and repository license. Hosted products and external model services may have different terms. D means documentation inspected, not installed or execution-tested.

The first three projects generate or edit source code. React Grab supplies visual-to-source context; the two browser servers provide infrastructure for rendering, observation and debugging. Their inclusion here does not broaden the research catalog to generic GUI navigation agents.

| Project and role | Documented workflow and boundary | Repository | License | Reviewed commit | Checked |
| --- | --- | --- | --- | --- | --- |
| **screenshot-to-code**<br>Generation and visual feedback | Converts screenshots, mockups and screen recordings into frontend code. Documents optional browser screenshot preview so the agent can render and visually inspect generated pages; model-provider keys are required. | [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | [MIT](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/LICENSE) | [a813977](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-screenshot-to-code) |
| **Onlook**<br>Visual editor | Maps rendered DOM elements to source locations and writes visual edits back to code, with an AI editing interface. The public editor targets Next.js and Tailwind; the README distinguishes it from the newer hosted product. | [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | [Apache-2.0](https://github.com/onlook-dev/onlook/blob/423e2e924366419e418ee049093872d535eea41a/LICENSE.md) | [423e2e9](https://github.com/onlook-dev/onlook/blob/423e2e924366419e418ee049093872d535eea41a/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-onlook) |
| **stagewise**<br>Browser-connected coding environment | Combines browsing with a coding agent that can inspect the tab console and debugger. Connecting a codebase enables permanent source edits; temporary browser changes alone do not constitute code generation. | [stagewise-io/stagewise](https://github.com/stagewise-io/stagewise) | [AGPL-3.0](https://github.com/stagewise-io/stagewise/blob/43c6b252bbded96f37dcec6d858bd346d17f545b/LICENSE) | [43c6b25](https://github.com/stagewise-io/stagewise/blob/43c6b252bbded96f37dcec6d858bd346d17f545b/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-stagewise) |
| **React Grab**<br>Visual selection to source context | Turns a selected visible UI element into element and component-stack context with source locations for a coding agent. Supplies grounding for edits; the selection tool itself does not generate or validate the resulting code. | [aidenybai/react-grab](https://github.com/aidenybai/react-grab) | [MIT](https://github.com/aidenybai/react-grab/blob/ea4bbec9e80f4802e8ae19ad18431edb9ddbb670/LICENSE) | [ea4bbec](https://github.com/aidenybai/react-grab/blob/ea4bbec9e80f4802e8ae19ad18431edb9ddbb670/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-react-grab) |
| **Playwright MCP**<br>Browser infrastructure | Exposes browser interaction, accessibility snapshots and screenshots to agents, with opt-in coordinate actions. Its default interaction uses accessibility data; screenshot capture can support a render-and-refine loop, while orchestration and visual scoring remain the caller's responsibility. | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | [Apache-2.0](https://github.com/microsoft/playwright-mcp/blob/b8b4183e099f136cbec0388a6088d4aa2f6b9685/LICENSE) | [b8b4183](https://github.com/microsoft/playwright-mcp/blob/b8b4183e099f136cbec0388a6088d4aa2f6b9685/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-playwright-mcp) |
| **Chrome DevTools MCP**<br>Browser debugging infrastructure | Connects coding agents to live Chrome for automation, screenshots, console/network inspection and performance traces. Supplies rendered evidence and runtime diagnostics for code repair; it does not prescribe a coding loop or visual-quality evaluator. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | [Apache-2.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/f827e067b0cea88bd99ae6de7f70f0a24aef00c5/LICENSE) | [f827e06](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/f827e067b0cea88bd99ae6de7f70f0a24aef00c5/README.md) | [D · 2026-10-14](docs/SOURCE_AUDIT.md#system-chrome-devtools-mcp) |

## Official System Resources

Hosted-system documentation retained separately from the open-source list. The date identifies the source publication, not current feature availability.

| System | Source date | Documented role | Source | Checked |
| --- | --- | --- | --- | --- |
| **Stitch**<br>Hosted system | Published 2025-05-20 | The launch announcement describes image/wireframe input, iterative UI design and frontend code export. This entry documents the launch workflow, not the current complete feature set or pricing. | [Official launch announcement](https://developers.googleblog.com/stitch-a-new-way-to-design-uis/) | [D · Announcement](docs/SOURCE_AUDIT.md#system-stitch) |

## Reading Routes

- **Start with reconstruction:** pix2code → ReDraw → DCGen → Design2Code.
- **Build training data:** WebSight → WebCode2M → Web2Code → Flame → JanusCoder.
- **Study feedback:** UICoder → ReLook → WebGen-V Bench → UI2Code^N → VisRefiner → RubSE; IR4RL provides a graphics-specific connection.
- **Study editing and behavior:** Sketch-n-Sketch → Code Shaping → Interaction2Code → WebVIA → DesignBench → MT-Web2Code.
- **Build a harness:** compare WebGen-V Bench, VISTA and WebUIProof for evaluation/feedback loops, and MaLiang-Harness for revision-aware graphics workflows; use the implementation index above.
- **Choose an evaluation:** use the [evaluation checklist](docs/EVALUATION.md) before comparing benchmark scores.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope decisions, bilingual templates, evidence requirements and validation commands. Taxonomy can evolve with the research scope; keep stable audit identifiers and one row per paper.

## Organization Reference

Entry layout, parallel summaries, source-audit conventions and standard-library validation were informed by the Awesome-OPD repository at commit `5d575fc`. Its topic categories and paper content were not reused. This is an independently maintained research catalog.
