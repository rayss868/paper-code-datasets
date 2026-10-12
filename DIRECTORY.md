---
audience: humans-and-agents
last_reviewed: 2026-10-12
---

# Full directory

All 200 sources, grouped by **what kind of place it is**, with the workflow stage and field tags shown on every entry.
The original compilation's grouping letter (A to T) is kept as a provenance trace at the end of each block.

Raw data: [`data/sources.json`](../data/sources.json) | [`data/sources.csv`](../data/sources.csv)
Link status: [`audit/liveness.md`](../audit/liveness.md)

## What is in here

| Kind of source | Count |
|---|---:|
| Software directory | 24 |
| Benchmark & leaderboard | 23 |
| Dataset repository | 21 |
| Model & algorithm repository | 19 |
| Software journal | 14 |
| Artifact evaluation | 14 |
| Paper discovery | 13 |
| Proceedings & publisher | 11 |
| Reproducibility platform | 10 |
| Paper-to-code lookup | 10 |
| Lab & organization repository | 10 |
| Curated list | 9 |
| Metadata & knowledge graph | 8 |
| Package index | 7 |
| Code search & hosting | 5 |
| Workflow registry | 2 |

**Total: 200 entries** across 16 kinds of source, in 5 workflow stages.

## Entries

### Software directory (24)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [004] Research Software Directory
- **URL:** https://research-software-directory.org/
- **Type:** Software index
- **Field:** Academic software
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `code`
- **What to look for:** Directory of research software projects, contributors, and related publications.
- **How to use it:** Search by institution name, field, or software; then continue to the repo and paper references.
- **Limitation:** Coverage follows the institutions and communities that participate.

#### [007] Open Scientific Code Registry
- **URL:** https://openscicode.org/
- **Type:** Code index
- **Field:** Neuroscience
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Code referenced in neuroscience articles or research.
- **How to use it:** Search by paper title or method name, then follow the indexed code.
- **Limitation:** Coverage is mainly neuroscience; check how current the index is.

#### [008] bio.tools
- **URL:** https://bio.tools/
- **Type:** Software registry
- **Field:** Bioinformatics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** List of software, its function, publications, and code links.
- **How to use it:** Filter by bioinformatics function; open the publication and the repository URL.
- **Limitation:** Some entries are web tools rather than full source code.

#### [009] SciCrunch Resources
- **URL:** https://scicrunch.org/resources
- **Type:** Tool registry
- **Field:** Biomedicine and life sciences
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Research resources, software, identifiers, and tool information.
- **How to use it:** Search the tool name or its RRID, then find the vendor or project page and the related article.
- **Limitation:** It does not guarantee that source code is openly available.

#### [012] SciCodes
- **URL:** https://scicodes.net/
- **Type:** Registry network
- **Field:** Scientific software
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** List of registries and initiatives that index scientific code.
- **How to use it:** Start from the partner list; pick the registry that matches your research field.
- **Limitation:** A consortium portal, not a single code download engine.

<sub>originally group B: Research code repositories and executable papers</sub>

#### [015] AEA Data and Code Repository
- **URL:** https://www.icpsr.umich.edu/sites/aea/home
- **Type:** Replication
- **Field:** Empirical economics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `social` `dataset` `code` `licence`
- **What to look for:** Data packages, scripts, documentation, and replication materials for AEA articles.
- **How to use it:** Search by article title; download the replication package and follow the README.
- **Limitation:** Some data is licensed or restricted and is not distributed directly.

#### [018] NASA Open Source Software
- **URL:** https://code.nasa.gov/
- **Type:** Software catalog
- **Field:** Space, simulation, science
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `code`
- **What to look for:** NASA open-source projects and repository links.
- **How to use it:** Search by topic or software name, then continue to the official repository.
- **Limitation:** Not every piece of software maps directly to a single paper.

#### [019] DOE CODE
- **URL:** https://www.osti.gov/doecode
- **Type:** Software catalog
- **Field:** Energy, physics, computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `physics` `open science` `api` `code` `doi`
- **What to look for:** Research software from the US Department of Energy along with its metadata.
- **How to use it:** Search by project name or software DOI; follow the source or download links.
- **Limitation:** Licensing and source completeness depend on the individual item.

#### [020] CodaLab Worksheets
- **URL:** https://codalab.org/codalab-worksheets/
- **Type:** Experiments
- **Field:** ML and computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `dataset` `benchmark`
- **What to look for:** Worksheets that record commands, data, results, and experiments.
- **How to use it:** Find public worksheets tied to a benchmark; inspect the runs, inputs, and outputs.
- **Limitation:** Access to and availability of the execution environment depend on the project.

#### [021] Wolfram Notebook Archive
- **URL:** https://www.notebookarchive.org/
- **Type:** Notebook
- **Field:** Mathematics and computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `general`
- **What to look for:** Interactive notebooks you can read or run in Wolfram.
- **How to use it:** Search the mathematical concept or algorithm, then download the notebook.
- **Limitation:** Running it locally may need Wolfram Language or related products.

<sub>originally group C: Paper search engines you can trace back to code</sub>

#### [030] OpenReview
- **URL:** https://openreview.net/
- **Type:** Conference review
- **Field:** ML and AI
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `materials` `code`
- **What to look for:** Submissions, review comments, attachments, and code links when present.
- **How to use it:** Search by title or venue; open the PDF, the supplementary material, and the author response.
- **Limitation:** Code may be released only after acceptance, or may not exist at all.

<sub>originally group D: Direct source code implementations</sub>

#### [052] Hugging Face Models
- **URL:** https://huggingface.co/models
- **Type:** Model hub
- **Field:** Machine learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `dataset` `code`
- **What to look for:** Model weights, configs, model cards, and paper links.
- **How to use it:** Filter by task; read the model card, arXiv paper, and linked code.
- **Limitation:** Weights are not automatically the training code or a complete dataset.

#### [053] Hugging Face Spaces
- **URL:** https://huggingface.co/spaces
- **Type:** Demo and code
- **Field:** AI
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Interactive demos and the Git repository behind a public Space.
- **How to use it:** Find a demo for your method, then open Files and versions.
- **Limitation:** Demo code is often inference only, not the training implementation.

<sub>originally group G: Code journals and specialized scientific notebooks</sub>

#### [078] NeuroLibre
- **URL:** https://neurolibre.org/
- **Type:** Executable article
- **Field:** Neuroscience
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `biomedical` `earth` `dataset` `code`
- **What to look for:** Interactive articles built on notebooks, code, data, and environments.
- **How to use it:** Pick a paper and open the interactive notebook or the supporting repo.
- **Limitation:** The environment may need specialized compute resources.

#### [080] PhysioNet Software
- **URL:** https://physionet.org/software/
- **Type:** Code catalog
- **Field:** Medical and physiological signals
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `dataset` `code` `licence`
- **What to look for:** Software for ECG, ICU, biosignals, and clinical analysis.
- **How to use it:** Find a toolkit that matches your dataset or research; read its documentation and license.
- **Limitation:** Clinical data and its usage permissions may differ from the code license.

#### [082] Pangeo Gallery
- **URL:** https://gallery.pangeo.io/
- **Type:** Example notebook
- **Field:** Climate, geospatial
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `dataset` `code`
- **What to look for:** Python and Jupyter notebooks for earth data analysis.
- **How to use it:** Pick a notebook tied to a climate or satellite dataset, then find its source repo.
- **Limitation:** A data processing example is not always tied to a single paper.

<sub>originally group H: Paper, data, notebook, and software portals</sub>

#### [090] DANDI Notebooks
- **URL:** https://notebooks.dandiarchive.org/index.html
- **Type:** Notebook
- **Field:** Neuroscience
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `dataset`
- **What to look for:** Analysis notebooks for neuroscience datasets and papers.
- **How to use it:** Pick a DANDI dataset, open the notebook, and try Colab if it is offered.
- **Limitation:** The data and the notebook may be hosted in different places.

<sub>originally group N: Workflows, research code, and model directories</sub>

#### [144] Archive of Formal Proofs (AFP)
- **URL:** https://www.isa-afp.org/
- **Type:** Formal proof archive
- **Field:** Formal methods, algorithms, mathematics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Isabelle theories and proof code with supporting publications.
- **How to use it:** Search a concept or paper; download the formal proof entry and check its build session.
- **Limitation:** The code is formal proof artifact, not a conventional Python application.

#### [147] NITRC
- **URL:** https://www.nitrc.org/
- **Type:** Research software directory
- **Field:** Neuroimaging, neuroscience
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `biomedical` `open science` `dataset` `code` `licence`
- **What to look for:** Software, datasets, documentation, and projects for processing brain images.
- **How to use it:** Find the application for your method; look at the project files, code host, publications, and license.
- **Limitation:** Some tools are binary only, or the project requires registration.

#### [149] Brainlife.io
- **URL:** https://brainlife.io/
- **Type:** Analysis platform
- **Field:** Neuroscience, neuroinformatics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `dataset` `code`
- **What to look for:** Data, analysis apps, workflows, and tools used in publications.
- **How to use it:** Browse apps and pipelines, then read the docs and the linked repository.
- **Limitation:** Some functions run as hosted services and need an account.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [154] MATLAB File Exchange
- **URL:** https://www.mathworks.com/matlabcentral/fileexchange/
- **Type:** Source code sharing
- **Field:** Numerical computing, signal processing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code` `licence`
- **What to look for:** MATLAB scripts and packages for numerical methods, modeling, and simulation.
- **How to use it:** Search by algorithm or paper title; check the license, dependencies, and usage examples.
- **Limitation:** Not every project comes from a peer-reviewed paper, and MATLAB may be required.

<sub>originally group Q: Journals, ML benchmarks, and paper code</sub>

#### [173] aeon Time Series Toolkit
- **URL:** https://github.com/aeon-toolkit/aeon
- **Type:** Research implementation library
- **Field:** Time series ML, anomaly detection
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** Python code for classification, regression, forecasting, and clustering methods, along with the source papers.
- **How to use it:** Find the estimator in the docs, then follow the citation and a usage example.
- **Limitation:** An integrated library can differ from the original paper script.

<sub>originally group S: Materials science, energy, and research software</sub>

#### [188] PyPSA
- **URL:** https://github.com/PyPSA/PyPSA
- **Type:** Research software + paper
- **Field:** Energy systems, electrical engineering
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `open science` `dataset` `code` `benchmark`
- **What to look for:** Power system optimization code, benchmarks, examples, and reference papers.
- **How to use it:** Find PyPSA case study models, replicate the scenario, and check the solver version.
- **Limitation:** The core software tool needs case study data to replicate a specific paper.

#### [189] Pangeo Forge Recipes
- **URL:** https://github.com/pangeo-forge/pangeo-forge-recipes
- **Type:** Scientific data pipeline
- **Field:** Climate, geospatial, earth data
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `api` `dataset` `code`
- **What to look for:** Pipeline code that converts datasets into cloud-optimized analysis formats.
- **How to use it:** Find a relevant recipe or feed, then check the source data reference and the published metadata.
- **Limitation:** The repository states it is no longer under active development, and it is not a paper-code index.

### Benchmark & leaderboard (23)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [010] OpenML
- **URL:** https://www.openml.org/
- **Type:** Benchmark/data
- **Field:** Machine learning
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `ml` `api` `dataset` `code` `benchmark`
- **What to look for:** Datasets, tasks, runs, algorithm evaluations, and experiment metadata.
- **How to use it:** Pick a task, browse the runs and baselines, then match the method to a Python or R package.
- **Limitation:** Experiment runs do not always ship a complete paper repository.

<sub>originally group D: Direct source code implementations</sub>

#### [054] Kaggle Code
- **URL:** https://www.kaggle.com/code
- **Type:** Notebook
- **Field:** Data science
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `dataset` `code`
- **What to look for:** Python and R notebooks for data and algorithms.
- **How to use it:** Search by paper, method, or dataset, and filter for notebooks with clear outputs.
- **Limitation:** Community notebooks do not always match the paper they claim.

<sub>originally group E: Benchmarks, competitions, baselines, and model zoos</sub>

#### [058] MLCommons / MLPerf
- **URL:** https://mlcommons.org/benchmarks/
- **Type:** Benchmark
- **Field:** AI/ML
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** Benchmark suites, results, evaluation rules, and reference implementations.
- **How to use it:** Pick a benchmark; follow its reference implementation and run configuration.
- **Limitation:** A benchmark is not a substitute for the code of any specific paper method.

#### [059] Codabench
- **URL:** https://www.codabench.org/
- **Type:** Benchmark
- **Field:** AI, data science
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `dataset` `code` `benchmark`
- **What to look for:** Benchmarks, evaluation packages, and algorithm submissions.
- **How to use it:** Search for academic competitions; download the starter kit where one exists.
- **Limitation:** Access to the code participants submit varies.

#### [060] AIcrowd Challenges
- **URL:** https://www.aicrowd.com/challenges
- **Type:** Competitions
- **Field:** AI and ML
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `dataset` `code`
- **What to look for:** Datasets, baselines, and starter scripts for a given challenge.
- **How to use it:** Open the challenge; check its resources, baseline repository, and forum.
- **Limitation:** Many challenges run in phases or restrict access.

#### [061] EvalAI
- **URL:** https://eval.ai/
- **Type:** AI evaluation
- **Field:** AI
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `open science` `benchmark`
- **What to look for:** Challenges, model evaluation, and leaderboards.
- **How to use it:** Find a challenge tied to a paper, then check the baseline and the submission docs.
- **Limitation:** Not every participant's solution is open source.

#### [062] Grand Challenge
- **URL:** https://grand-challenge.org/challenges/
- **Type:** Medical benchmark
- **Field:** Medical image analysis
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `biomedical` `dataset` `code` `benchmark`
- **What to look for:** Medical datasets and benchmarks with evaluation protocols.
- **How to use it:** Pick a challenge; read the dataset policy and the starter code.
- **Limitation:** Medical data may require registration or a data use agreement.

#### [063] DrivenData Competitions
- **URL:** https://www.drivendata.org/competitions/
- **Type:** Competition
- **Field:** Data science for social impact
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `social` `dataset` `code` `benchmark`
- **What to look for:** Competition data, problem statements, and baselines from several events.
- **How to use it:** Search by topic; open Benchmarks, Resources, or community solutions.
- **Limitation:** Code for the top solutions is not always published.

#### [066] Kaggle Competitions
- **URL:** https://www.kaggle.com/competitions
- **Type:** Competition/benchmark
- **Field:** AI and data science
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `dataset` `code` `benchmark`
- **What to look for:** Datasets, evaluation metrics, discussions, and notebooks.
- **How to use it:** Open the competition; look at the Code tab and the write-ups from winning teams.
- **Limitation:** A competition solution is not automatically an implementation of a published paper.

<sub>originally group L: Paper-to-repository knowledge graphs</sub>

#### [124] Wizwand
- **URL:** https://www.wizwand.com/
- **Type:** Benchmark discovery
- **Field:** Machine learning
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `dataset` `code` `benchmark`
- **What to look for:** An index of papers, benchmarks, and related state-of-the-art results.
- **How to use it:** Search a task or model, then follow the paper and code links if present.
- **Limitation:** Check whether the pages and data are still live and up to date.
- **Correction:** 2026-10-12: wizwand.com now redirects to sota2.com/research, possibly a rebrand. The URL still works as an entry point.

<sub>originally group N: Earlier sources plus duplicate markers</sub>

#### [135] HyperAI Papers
- **URL:** https://hyper.ai/en/papers
- **Type:** Paper/benchmark discovery
- **Field:** AI and ML
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `api` `code` `benchmark`
- **What to look for:** Articles and metadata for AI-related models and benchmarks.
- **How to use it:** Search by method or topic; continue to the paper and its code resources.
- **Limitation:** Check that the links are live and note the update dates.

#### [137] CodeSOTA
- **URL:** https://www.codesota.com/
- **Type:** Paper and benchmark discovery
- **Field:** Machine learning
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `code` `benchmark`
- **What to look for:** Model search, benchmark results, and implementations where available.
- **How to use it:** Search a task or model, then follow the paper references and code links.
- **Limitation:** Check whether the site is still maintained and the leaderboard current.

<sub>originally group Q: Journals, ML benchmarks, and paper code</sub>

#### [169] Open Graph Benchmark (OGB)
- **URL:** https://ogb.stanford.edu/
- **Type:** Benchmark and evaluator
- **Field:** Graph machine learning
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `dataset` `benchmark`
- **What to look for:** Graph datasets, baselines, data loaders, evaluators, and leaderboards.
- **How to use it:** Pick a graph, node, or link task, then run the baseline scripts and the official evaluation.
- **Limitation:** A benchmark, not one specific implementation of every GNN paper.

#### [170] NeurIPS 2026 Evaluations & Datasets Track
- **URL:** https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets
- **Type:** Benchmark paper venue
- **Field:** Machine learning evaluation
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `materials` `dataset` `code` `benchmark`
- **What to look for:** 2026 dataset and evaluation papers, plus the code and dataset disclosure rules for camera-ready versions.
- **How to use it:** Find accepted papers through the proceedings or OpenReview; check the supplementary material and the source.
- **Limitation:** This link is the track or call page, not a direct paper download catalog.

#### [171] NLP Progress
- **URL:** https://nlpprogress.com/
- **Type:** Benchmark index
- **Field:** Natural language processing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** A list of NLP tasks, benchmarks, methods, and publications, with code links where available.
- **How to use it:** Pick an NLP task; check the Code column and the paper for the official implementation.
- **Limitation:** Maintenance is not always current, and some tasks have no code link.

#### [172] Time Series Classification Website
- **URL:** https://www.timeseriesclassification.com/
- **Type:** Benchmark and code
- **Field:** Time series ML
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `dataset` `code` `benchmark`
- **What to look for:** The UCR/UEA archive, benchmark results, and links to the aeon/tsml toolkits and baselines.
- **How to use it:** Pick classification, clustering, or regression, then compare the paper against the results and code.
- **Limitation:** Datasets and baselines come from different years; match the split and protocol.

<sub>originally group R: Deep learning and NLP implementations</sub>

#### [182] EleutherAI Language Model Evaluation Harness
- **URL:** https://github.com/EleutherAI/lm-evaluation-harness
- **Type:** Benchmark evaluation code
- **Field:** LLM, NLP
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** Benchmark frameworks, task configs, evaluators, and citations for experiment results.
- **How to use it:** Find the benchmark used in the paper; match the few-shot setup, metric, and model.
- **Limitation:** An evaluation tool, not a training implementation for every LLM.

<sub>originally group S: Materials science, energy, and research software</sub>

#### [183] Open Catalyst Project
- **URL:** https://opencatalystproject.org/
- **Type:** Benchmark+source
- **Field:** AI for materials, catalysis
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `materials` `dataset` `code` `benchmark`
- **What to look for:** The OC20/OC22 datasets, ML baselines, open-source code, leaderboards, and papers.
- **How to use it:** Open the dataset paper, then the baseline GitHub repo and the documentation of the experiment metrics.
- **Limitation:** Large datasets that require substantial compute and storage.

#### [184] Matbench
- **URL:** https://github.com/materialsproject/matbench
- **Type:** Source code benchmark
- **Field:** ML for materials
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `materials` `dataset` `code` `benchmark`
- **What to look for:** Material property prediction tasks, dataset loader code, benchmarks, and papers.
- **How to use it:** Open the source and documentation, run the baseline, and compare against the leaderboard.
- **Limitation:** Focused on material properties; the splits and metrics must follow the benchmark.

<sub>originally group T: Benchmarks, datasets, and paper implementation research</sub>

#### [190] MLCommons DataPerf
- **URL:** https://github.com/mlcommons/dataperf
- **Type:** Code benchmark
- **Field:** Data-centric machine learning
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `dataset` `code` `benchmark`
- **What to look for:** Benchmark tasks, baseline code, and dataset development evaluation.
- **How to use it:** Open the challenge or the DataPerf paper; run the reference baseline and the evaluator.
- **Limitation:** Challenge-specific implementations, not paper source code for every field.

#### [192] Monash Time Series Forecasting Archive
- **URL:** https://forecastingdata.org/
- **Type:** Forecasting benchmark
- **Field:** Forecasting, time series
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `api` `dataset` `code` `benchmark`
- **What to look for:** Forecasting datasets, R/Python reader code, baselines, evaluation, and related NeurIPS papers.
- **How to use it:** Open the Results or Software/GitHub tab on the official site; match the horizon and metric.
- **Limitation:** Its main strength is datasets and metadata, not every model script from the papers.

#### [197] Numenta Anomaly Benchmark (NAB)
- **URL:** https://github.com/numenta/NAB
- **Type:** Benchmark and source
- **Field:** Time-series anomaly detection
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `earth` `dataset` `code` `benchmark`
- **What to look for:** Labelled time-series datasets, scoring, a runner, baselines, and the related publication.
- **How to use it:** Clone the repository, run the detector evaluation, and compare the scores against the paper.
- **Limitation:** An older release, so expect to adjust the Python environment and the benchmark metrics.

#### [200] TimeEval Research Benchmark
- **URL:** https://github.com/TimeEval/TimeEval
- **Type:** Reproducibility benchmark
- **Field:** Time-series anomaly detection
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `open science` `dataset` `benchmark`
- **What to look for:** An evaluation toolkit, hundreds of datasets, containerized algorithms, and PVLDB paper links.
- **How to use it:** Use the TimeEval algorithms and benchmark manager; replicate the protocol from the paper.
- **Limitation:** Docker and Linux/WSL may be required; check the runtime version.

### Dataset repository (21)

<sub>originally group B: Research code repositories and executable papers</sub>

#### [016] openICPSR
- **URL:** https://www.openicpsr.org/
- **Type:** Repository
- **Field:** Social sciences and economics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `social` `dataset` `code` `doi`
- **What to look for:** Datasets, code, syntax files, and research project packages.
- **How to use it:** Search by author, title, or DOI; filter by file type, then check the code attachments.
- **Limitation:** How complete the materials are varies from depositor to depositor.

#### [017] Open Science Framework (OSF)
- **URL:** https://osf.io/
- **Type:** Project repository
- **Field:** Cross-disciplinary
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `dataset` `code`
- **What to look for:** Projects, preregistrations, data, code, protocols, and research materials.
- **How to use it:** Search public projects, then check Components, Files, Wiki, and any linked repositories.
- **Limitation:** Some projects are private, embargoed, or hold only data and protocols.

<sub>originally group H: Paper, data, notebook, and software portals</sub>

#### [088] GigaDB
- **URL:** https://gigadb.org/
- **Type:** Data + software
- **Field:** Bioinformatics, data science
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `biomedical` `dataset` `code` `doi`
- **What to look for:** Large datasets, software, and workflows supporting a publication.
- **How to use it:** Find the dataset or study; check its Files/Tools/Code section and DOI.
- **Limitation:** Not every record includes code.

#### [091] Dryad
- **URL:** https://datadryad.org/
- **Type:** Supporting data
- **Field:** Cross-disciplinary
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `api` `dataset` `code` `doi`
- **What to look for:** Scientific datasets and citable research materials.
- **How to use it:** Search by DOI or title; check the metadata and the Zenodo link for software.
- **Limitation:** The focus is data; source code is not always included.

#### [093] CERN Open Data
- **URL:** https://opendata.cern.ch/
- **Type:** Open data and examples
- **Field:** High-energy physics
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `earth` `physics` `dataset` `code`
- **What to look for:** Experimental data, example software, analysis, and documentation.
- **How to use it:** Pick a dataset and its notebook, run the analysis, and note the software version.
- **Limitation:** Physics data and environments can require serious storage.

#### [094] Mendeley Data
- **URL:** https://data.mendeley.com/
- **Type:** Data repository
- **Field:** Cross-disciplinary
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `dataset` `code`
- **What to look for:** Datasets and supplementary files that sometimes include source scripts.
- **How to use it:** Search by paper title; check for .py, .R, or .m files and a README.
- **Limitation:** Data-oriented, so code is not always available.

<sub>originally group N: Earlier sources plus duplicate markers</sub>

#### [134] Zenodo
- **URL:** https://zenodo.org/
- **Type:** DOI repository
- **Field:** Cross-disciplinary
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `dataset` `code` `doi` `licence`
- **What to look for:** Code releases, replication packages, data, reports, and DOIs.
- **How to use it:** Search by title, DOI, author, or "replication package"; filter for Software.
- **Limitation:** Licenses and file types vary, and not every record contains source.

#### [136] Figshare
- **URL:** https://figshare.com/
- **Type:** Research repository
- **Field:** Cross-disciplinary
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `dataset` `code` `doi`
- **What to look for:** Datasets, software, supporting files, and research materials.
- **How to use it:** Search by paper title, DOI, or "source code"; check the downloadable files.
- **Limitation:** Many records are data or figures, not source code.

#### [139] Harvard Dataverse
- **URL:** https://dataverse.harvard.edu/
- **Type:** Data repository
- **Field:** Cross-disciplinary
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `open science` `api` `dataset` `code` `doi`
- **What to look for:** Research datasets, supporting files, and code when the depositor includes it.
- **How to use it:** Search by paper title or DOI; look at Files and metadata, then pick out the script files.
- **Limitation:** The focus is datasets; source code availability differs from record to record.

<sub>originally group P: Academic repositories and data networks</sub>

#### [157] 4TU.ResearchData
- **URL:** https://data.4tu.nl/
- **Type:** Data and software repository
- **Field:** Engineering and geoscience
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `earth` `api` `dataset` `code`
- **What to look for:** Datasets, models, scripts, and computational artifacts with DOIs.
- **How to use it:** Search the paper or title, filter by record type, then download the files and metadata.
- **Limitation:** Not every record holds code, and some are dataset only.

#### [158] DataverseNO
- **URL:** https://dataverse.no/
- **Type:** Dataverse repository
- **Field:** Cross-disciplinary research
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `open science` `api` `dataset` `code`
- **What to look for:** Datasets, R or Python scripts, replication packages, metadata, and DOIs.
- **How to use it:** Search by keyword or publication title; check the Files tab for scripts and data.
- **Limitation:** As with Harvard Dataverse, code availability depends on what was deposited.

#### [159] Borealis Canadian Dataverse Repository
- **URL:** https://borealisdata.ca/
- **Type:** Dataverse repository
- **Field:** Cross-disciplinary research
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `open science` `dataset` `code` `doi` `licence`
- **What to look for:** Canadian research datasets plus supporting scripts or documents where available.
- **How to use it:** Browse by paper title and the file list in the record; keep the DOI and the license.
- **Limitation:** Geared more toward data than toward complete source code.

#### [160] EMBL-EBI BioStudies
- **URL:** https://www.ebi.ac.uk/biostudies/
- **Type:** Scientific study archive
- **Field:** Biology, bioinformatics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `dataset` `code` `doi`
- **What to look for:** Study data, supplementary attachments, and code or links where included.
- **How to use it:** Search by accession or DOI, then look at the study files and software links.
- **Limitation:** Attachment formats vary, and access to the data may be restricted.

#### [161] PANGAEA
- **URL:** https://www.pangaea.de/
- **Type:** Data repository
- **Field:** Earth science, geoscience
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `earth` `api` `dataset` `code`
- **What to look for:** Datasets with strong metadata, DOIs, paper references, and supporting material.
- **How to use it:** Search the publication or parameter, then follow the references and external links.
- **Limitation:** A data source, so lower priority if source code is what you need.

#### [165] DataLad Public Dataset Registry
- **URL:** https://github.com/datalad/datasets.datalad.org
- **Type:** Versioned dataset registry
- **Field:** Neuroinformatics and computational science
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `biomedical` `dataset`
- **What to look for:** Versioned dataset collections with provenance and storage pointers.
- **How to use it:** Find a dataset, read the README and access notes, then match it to the paper implementation.
- **Limitation:** Focused on data management, and not every dataset ships the publication scripts.

<sub>originally group Q: Journals, ML benchmarks, and paper code</sub>

#### [168] Materials Cloud Archive
- **URL:** https://archive.materialscloud.org/
- **Type:** Data/simulation archive
- **Field:** Computational materials science
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `physics` `open science` `dataset` `code` `doi`
- **What to look for:** Calculation data, AiiDA workflows, inputs and outputs, and sometimes code to reproduce the paper.
- **How to use it:** Search a material name, paper title, or DOI; open the supporting files and provenance.
- **Limitation:** Depends on computational physics software, and not every deposit contains code.

<sub>originally group R: Deep learning and NLP implementations</sub>

#### [174] Hugging Face Datasets
- **URL:** https://huggingface.co/datasets
- **Type:** Dataset and card catalog
- **Field:** AI, NLP, vision, audio
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `ml` `dataset` `code` `licence`
- **What to look for:** Dataset Hub entries, dataset cards, licenses, splits, and paper references when the authors list them.
- **How to use it:** Search for the dataset named in the paper; check the Dataset Card, then follow the code repository.
- **Limitation:** A dataset portal, so training scripts are not guaranteed.

<sub>originally group S: Materials science, energy, and research software</sub>

#### [185] NOMAD Laboratory
- **URL:** https://nomad-lab.eu/
- **Type:** Data and workflow archive
- **Field:** Materials informatics
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `api` `dataset` `code`
- **What to look for:** Materials simulation and experiment data, plus metadata that links to workflows.
- **How to use it:** Find a record by material name or publication, then check the input and output files and any code link.
- **Limitation:** Mostly computational data, and source code is not always there.

<sub>originally group T: Benchmarks, datasets, and paper implementation research</sub>

#### [191] UCI Machine Learning Repository
- **URL:** https://archive.ics.uci.edu/
- **Type:** Dataset repository
- **Field:** General machine learning
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `ml` `dataset` `code`
- **What to look for:** Classic and new datasets with task descriptions and citations.
- **How to use it:** Find the dataset in the paper, then track the implementation down through the GitHub article.
- **Limitation:** It contains data; it does not promise the implementation code for a paper.

#### [193] Nature Scientific Data
- **URL:** https://www.nature.com/sdata/
- **Type:** Dataset and code journal
- **Field:** Cross-disciplinary computational work
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `dataset` `code`
- **What to look for:** Data descriptors and code availability statements for custom processing code.
- **How to use it:** Search a topic in the journal, then open Code availability and access the software or data.
- **Limitation:** Not all papers use custom code, and some access is restricted.

#### [195] HEPData
- **URL:** https://www.hepdata.net/
- **Type:** Research data + auxiliary files
- **Field:** High-energy physics
- **Stage:** Find the data (`03-datasets`)
- **Tags:** `materials` `physics` `open science` `api` `dataset` `code`
- **What to look for:** Physics paper data tables, metadata, extra resource files, API, and DOI.
- **How to use it:** Search for the INSPIRE paper or collaboration; look at the record's resources and downloads.
- **Limitation:** Code is present only if it is included as an auxiliary file or a link.

### Model & algorithm repository (19)

<sub>originally group E: Benchmarks, competitions, baselines, and model zoos</sub>

#### [064] OpenMMLab GitHub
- **URL:** https://github.com/open-mmlab
- **Type:** Research framework
- **Field:** Computer vision
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml`
- **What to look for:** Model implementations, training configs, and model zoos.
- **How to use it:** Search by architecture name; check the config, model checkpoint, and paper reference.
- **Limitation:** Large frameworks need matching CUDA and PyTorch versions.

#### [065] MONAI Model Zoo
- **URL:** https://github.com/Project-MONAI/model-zoo
- **Type:** Model zoo
- **Field:** Medical imaging AI
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `biomedical` `api` `dataset`
- **What to look for:** Model bundles and experiment configuration.
- **How to use it:** Find a model bundle, then read its metadata, dataset, and training or inference workflow.
- **Limitation:** A bundle does not necessarily include the original medical data.

<sub>originally group G: Code journals and specialized scientific notebooks</sub>

#### [079] Astrophysics Source Code Library (ASCL)
- **URL:** https://ascl.net/
- **Type:** Code registry
- **Field:** Astronomy and astrophysics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `physics` `code`
- **What to look for:** Code used or cited in astronomy publications.
- **How to use it:** Find the code by software name or paper; follow the source URL and the citation.
- **Limitation:** Not every entry offers a modern installer.

<sub>originally group K: Algorithm and computational model archives</sub>

#### [112] ACM Collected Algorithms (CALGO/Netlib)
- **URL:** https://www.netlib.org/toms/
- **Type:** Algorithm archive
- **Field:** Numerical computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Mathematical and numerical algorithm code tied to ACM TOMS publications.
- **How to use it:** Search by algorithm number or method name, download the source, and read the reference.
- **Limitation:** Much of the historical code uses old Fortran or C.

#### [113] ModelDB
- **URL:** https://modeldb.science/
- **Type:** Model repository
- **Field:** Computational neuroscience
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Neuron and network simulation models tied to papers.
- **How to use it:** Search the paper or neuron type, then download the model files and parameters.
- **Limitation:** Running the simulation may need NEURON, GENESIS, or a similar tool.

#### [114] Physiome Model Repository
- **URL:** https://models.physiomeproject.org/
- **Type:** Model repository
- **Field:** Biology/physiology
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Biological and mathematical models, CellML format, and supporting code.
- **How to use it:** Search for a model by its article, then check the version and the runnable format.
- **Limitation:** Runnable models are not always plain Python.

#### [115] CoMSES Computational Model Library
- **URL:** https://www.comses.net/codebases/
- **Type:** Model repository
- **Field:** Agent-based simulation
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `social` `api` `code`
- **What to look for:** Models, source code, paper metadata, and model reviews.
- **How to use it:** Search the social or environmental domain; look at the Codebase and the related publications.
- **Limitation:** Worth checking which version of the simulator software was used.

#### [116] NetLogo Models Library
- **URL:** https://ccl.northwestern.edu/netlogo/models/
- **Type:** Models/examples
- **Field:** Agent-based modeling
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** NetLogo model code and interactive simulation examples.
- **How to use it:** Search a phenomenon or method; run the model and inspect its source.
- **Limitation:** An educational model is not automatically a faithful representation of the original paper.

#### [117] Open Source Brain
- **URL:** https://www.opensourcebrain.org/
- **Type:** Model repository
- **Field:** Neuroscience
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `biomedical` `open science` `dataset` `code`
- **What to look for:** Brain models, simulation scripts, and research data.
- **How to use it:** Search the publication or neural model, then follow the Git repository and workflow.
- **Limitation:** Some models depend on specialized simulators.

#### [118] BioModels
- **URL:** https://www.ebi.ac.uk/biomodels/
- **Type:** Model repository
- **Field:** Systems biology
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code` `doi`
- **What to look for:** Mathematical models linked to publications, often in SBML format.
- **How to use it:** Search by paper title or DOI; download the model and run it with a compatible tool.
- **Limitation:** An equation model is different from a complete source code package.

<sub>originally group N: Workflows, research code, and model directories</sub>

#### [145] CSDMS Model Download Portal
- **URL:** https://csdms.colorado.edu/wiki/Model_portal
- **Type:** Model catalog
- **Field:** Geoscience, hydrology, environment
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `api` `code` `licence`
- **What to look for:** Simulation models, scientific software, article references, and download links.
- **How to use it:** Search the model name, then check its metadata, code page, and the papers that used it.
- **Limitation:** License, language, and access vary by model owner.
- **Correction:** 2026-10-12: /wiki/Model_download_portal returned 404. Changed to /wiki/Model_portal (the official model download page).

#### [146] USGS Model Catalog
- **URL:** https://data.usgs.gov/modelcatalog/
- **Type:** Model catalog
- **Field:** Geoscience, environment, hydrology
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `api` `code`
- **What to look for:** Government model metadata, documentation, and possible software links.
- **How to use it:** Search by phenomenon or algorithm keyword; continue to the source code or technical report.
- **Limitation:** Model metadata does not always mean a public implementation exists.

#### [148] BioImage Model Zoo
- **URL:** https://bioimage.io/
- **Type:** Model zoo
- **Field:** Bioimaging, microscopy AI
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `biomedical` `code`
- **What to look for:** Biomedical DL models, model formats, usage examples, weights, and paper references.
- **How to use it:** Search a task or model, open the resource, and identify the implementation or notebook.
- **Limitation:** Model weights are not the same as source training code; validate each item.

<sub>originally group R: Deep learning and NLP implementations</sub>

#### [178] Detectron2
- **URL:** https://github.com/facebookresearch/detectron2
- **Type:** Research model framework
- **Field:** Object detection, segmentation
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `benchmark`
- **What to look for:** Model zoos, baselines, configs, checkpoints, and vision method implementations.
- **How to use it:** Match the paper to the configs or projects, then run training and evaluation.
- **Limitation:** Several tasks require a GPU and compatible dependencies.

#### [179] MMDetection
- **URL:** https://github.com/open-mmlab/mmdetection
- **Type:** Model zoo and framework
- **Field:** Object detection, segmentation
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** Paper architecture code, training configs, weights, COCO benchmarks, and evaluation.
- **How to use it:** Find the model name in the model zoo, check the paper's README, and run the baseline config.
- **Limitation:** Part of OpenMMLab [64]; it has a different entry point from the organization list.

<sub>originally group S: Materials science, energy, and research software</sub>

#### [186] Materials Project Software
- **URL:** https://github.com/materialsproject
- **Type:** Research code organization
- **Field:** Computational materials
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `api` `dataset` `code`
- **What to look for:** Python packages, APIs, and materials analysis tools with documentation and publications.
- **How to use it:** Find the library for your method, then check the pymatgen or mp-api repository and the paper citation.
- **Limitation:** Toolkit code does not automatically include all the data or training scripts from a paper.

<sub>originally group T: Benchmarks, datasets, and paper implementation research</sub>

#### [196] openmod Open Models Directory
- **URL:** https://wiki.openmod-initiative.org/wiki/Open_Models
- **Type:** Modeling code catalog
- **Field:** Energy system modelling
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `code` `licence`
- **What to look for:** List of open-source energy models, programming languages, licenses, and code links.
- **How to use it:** Filter energy models; continue to the repository, then the method paper it cites.
- **Limitation:** A community catalog may include outdated entries or duplicates of the same framework.

#### [198] PyTorch Geometric (PyG)
- **URL:** https://github.com/pyg-team/pytorch_geometric
- **Type:** Paper method code
- **Field:** Graph neural networks
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `earth` `dataset` `code` `benchmark`
- **What to look for:** GNN layers from various papers, datasets, train and eval examples, and models.
- **How to use it:** Search for the method name in the docs and examples; follow the paper reference on the layer.
- **Limitation:** A framework implementation is not identical to every paper pipeline.

#### [199] Deep Graph Library (DGL) Examples
- **URL:** https://github.com/dmlc/dgl/tree/master/examples
- **Type:** GNN paper code collection
- **Field:** Graph ML, knowledge graphs
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `ml` `code`
- **What to look for:** Example implementations of GNN papers, including traffic forecasting, link prediction, and node classification.
- **How to use it:** Find the Official DGL Examples list; open the paper link and run the relevant example.
- **Limitation:** DGL notes that some examples are compatible only with specific versions.

### Software journal (14)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [001] Journal of Open Source Software (JOSS)
- **URL:** https://joss.theoj.org/papers
- **Type:** Software journal
- **Field:** Scientific software across fields
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `code`
- **What to look for:** Software articles, DOIs, and the linked implementation repositories.
- **How to use it:** Search by field keyword, open the paper, then follow the repository link and the install documentation.
- **Limitation:** It publishes software papers, not every kind of experimental paper.

#### [002] JMLR Machine Learning Open Source Software (MLOSS)
- **URL:** https://www.jmlr.org/mloss/
- **Type:** Software journal
- **Field:** Machine learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `open science` `code`
- **What to look for:** ML software papers and links to packages or source code.
- **How to use it:** Search an algorithm name in the MLOSS archive, then check the code link and the library version.
- **Limitation:** Articles may rely on older dependency versions.

<sub>originally group B: Research code repositories and executable papers</sub>

#### [013] Journal of Statistical Software
- **URL:** https://www.jstatsoft.org/
- **Type:** Software journal
- **Field:** Statistics, R and Python
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `social` `api` `code`
- **What to look for:** Method implementation papers, software packages, and replication material.
- **How to use it:** Search the statistical method, then open the article and the supplementary code, CRAN, or GitHub link.
- **Limitation:** Watch the package version and any API changes since publication.

#### [014] The R Journal
- **URL:** https://journal.r-project.org/
- **Type:** Software journal
- **Field:** Statistics with R
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `social` `code`
- **What to look for:** Articles on using and developing R packages, plus example code.
- **How to use it:** Search the algorithm name; open the paper, the R examples, and the related package repo.
- **Limitation:** Mostly the R ecosystem, not Python.

<sub>originally group G: Code journals and specialized scientific notebooks</sub>

#### [077] SciPost Physics Codebases
- **URL:** https://scipost.org/journals/SciPostPhysCodeb
- **Type:** Code journal
- **Field:** Computational physics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `physics` `code`
- **What to look for:** Codebase articles with a publication identity and archived source.
- **How to use it:** Search the simulation type, then open the article and the cited code release.
- **Limitation:** Mostly physics, not every discipline.

<sub>originally group H: Paper, data, notebook, and software portals</sub>

#### [083] Image Processing On Line (IPOL)
- **URL:** https://www.ipol.im/
- **Type:** Algorithms journal
- **Field:** Image processing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** Algorithm articles with source code and an online demo.
- **How to use it:** Search for an image technique, read the explanation, access the code, and run the example.
- **Limitation:** A good fit for classic image processing; coverage of certain ML areas is limited.

#### [084] Journal of Open Research Software
- **URL:** https://openresearchsoftware.metajnl.com/
- **Type:** Software journal
- **Field:** Research software across disciplines
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `api` `code`
- **What to look for:** Software metapapers with code availability metadata.
- **How to use it:** Find the paper or software; follow the availability statement to the repository.
- **Limitation:** Software articles only, not every applied paper.
- **Correction:** 2026-10-12: not reachable (timeout) from the audit host, but the site is ACTIVE (articles published Sep 2026). Likely IP or geo filtering rather than a dead link.

#### [085] Journal of Open Source Education (JOSE)
- **URL:** https://jose.theoj.org/papers
- **Type:** Education journal
- **Field:** Computing and education
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `open science` `code`
- **What to look for:** Open educational software and materials with repositories.
- **How to use it:** Search for technical teaching material, then look at the repo and the notebooks.
- **Limitation:** Not designed for reproducing cutting-edge research results.

#### [092] F1000Research
- **URL:** https://f1000research.com/
- **Type:** Open research journal
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `open science` `code`
- **What to look for:** Software Tool articles that include code availability information.
- **How to use it:** Filter by the Software Tool article type; follow the source code availability statement.
- **Limitation:** Note the peer review stage of each article.

<sub>originally group J: DARTS, software journals, and further code curation</sub>

#### [106] SoftwareX
- **URL:** https://www.sciencedirect.com/journal/softwarex
- **Type:** Software journal
- **Field:** Scientific computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code` `licence`
- **What to look for:** Software articles, availability statements, and repo links.
- **How to use it:** Search by tool name or topic; follow the source code availability statement.
- **Limitation:** Full text access and the article or software license are separate things.

#### [107] ElsevierSoftwareX GitHub
- **URL:** https://github.com/ElsevierSoftwareX
- **Type:** Organization repository
- **Field:** Research software
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `code` `doi`
- **What to look for:** Repositories associated with some SoftwareX publications.
- **How to use it:** Search the organization's repos for the paper name; check the version and the paper DOI.
- **Limitation:** It does not necessarily cover every article in the journal.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [150] Geoscientific Model Development (GMD)
- **URL:** https://gmd.copernicus.org/
- **Type:** Journal with a code policy
- **Field:** Climate, atmosphere, modeling
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `dataset` `code`
- **What to look for:** Computational model papers with a code and data availability section and artifact versioning.
- **How to use it:** Search by model name; open the Code and data availability section for the archive and repository.
- **Limitation:** Availability may be restricted, or the code may depend on a specific scientific stack.

<sub>originally group Q: Journals, ML benchmarks, and paper code</sub>

#### [166] PLOS Computational Biology - Code Availability
- **URL:** https://journals.plos.org/ploscompbiol/s/code-availability
- **Type:** Journal with a source code policy
- **Field:** Computational biology, biomedical ML
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `biomedical` `dataset` `code` `doi`
- **What to look for:** Papers required to state where the authors' own code supporting the results can be found, with certain exceptions.
- **How to use it:** Search for a paper in the journal; check the Data and Code Availability statements, the DOI, and the repository.
- **Limitation:** Not every paper ships a complete training package, and code exceptions do apply.

#### [167] Bioinformatics (Oxford Academic) - Application Notes
- **URL:** https://academic.oup.com/bioinformatics
- **Type:** Software/algorithms journal
- **Field:** Bioinformatics, genomics ML
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Articles on new algorithm and software applications, usually with an availability statement and a code URL.
- **How to use it:** Search for an Application Note or Software paper; check the Availability and Implementation section.
- **Limitation:** Access policies may include a non-commercial use requirement.

### Artifact evaluation (14)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [003] ReScience C
- **URL:** https://rescience.github.io/read/
- **Type:** Reproducibility
- **Field:** Scientific computing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `open science` `code`
- **What to look for:** Replication articles together with the code that supports the experiments.
- **How to use it:** Start from the paper's reproduction results; open the Code link; compare the original method with its reproduction.
- **Limitation:** A replication may report differing results, which the article itself discusses.

<sub>originally group I: Conferences and artifact evaluation</sub>

#### [095] Security Research Artifacts
- **URL:** https://secartifacts.github.io/
- **Type:** Artifact index
- **Field:** Cybersecurity
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `security` `code`
- **What to look for:** Links to research artifacts from security conferences.
- **How to use it:** Search by conference and year, or by paper; follow the artifact repository or archive.
- **Limitation:** The index does not guarantee that every artifact stays online.

#### [096] SIGMOD Reproducibility
- **URL:** https://reproducibility.sigmod.org/
- **Type:** Conference reproducibility
- **Field:** Database systems
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `open science` `benchmark`
- **What to look for:** Artifacts, experiment scripts, and reproducibility reports.
- **How to use it:** Find SIGMOD papers; look at the artifact evaluation and the reproduction results.
- **Limitation:** Some artifacts require substantial server resources.

#### [097] ICSE 2026 Artifact Evaluation
- **URL:** https://conf.researchr.org/track/icse-2026/icse-2026-artifact-evaluation
- **Type:** Conference program
- **Field:** Software engineering
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** Guidelines and the papers taking part in ICSE artifact evaluation.
- **How to use it:** Find accepted artifacts, then open the related paper archive.
- **Limitation:** A program page, not always a downloadable code directory.

#### [098] ISSTA 2026 Artifact Evaluation
- **URL:** https://conf.researchr.org/track/issta-2026/issta-2026-artifact-evaluation
- **Type:** Conference program
- **Field:** Software testing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark` `licence`
- **What to look for:** Experiment packages for static and dynamic analysis and testing.
- **How to use it:** Search for papers that carry an artifact badge, then check the repo.
- **Limitation:** Some artifacts come with license or hardware restrictions.

#### [099] POPL 2026 Artifact Evaluation
- **URL:** https://popl26.sigplan.org/track/POPL-2026-artifact-evaluation
- **Type:** Conference program
- **Field:** Programming languages
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code` `benchmark`
- **What to look for:** Compilers, interpreters, proof artifacts, and research implementations.
- **How to use it:** Browse POPL papers and their artifact appendices.
- **Limitation:** An evaluation program is not the same thing as an open code repository.

#### [100] PLDI 2026 Research Artifacts
- **URL:** https://pldi26.sigplan.org/track/pldi-2026-pldi-research-artifacts
- **Type:** Conference program
- **Field:** Compilers/programming languages
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `code`
- **What to look for:** Experiment code for compilers, languages, and optimization.
- **How to use it:** Look for the artifact badge; inspect the shared container, VM, or code.
- **Limitation:** May require an older or specialized toolchain.

#### [101] ICFP 2026 Artifact Evaluation
- **URL:** https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation
- **Type:** Conference program
- **Field:** Functional programming
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `benchmark`
- **What to look for:** Implementations of functional languages plus proofs or experiments.
- **How to use it:** Start from accepted papers and look for the artifact link.
- **Limitation:** Completeness depends on the authors and the evaluation.

#### [102] EuroSys 2026 Artifacts
- **URL:** https://sysartifacts.github.io/eurosys2026/index
- **Type:** Conference program
- **Field:** Distributed systems
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `general`
- **What to look for:** Experiment artifacts for operating systems, cloud, and distributed systems.
- **How to use it:** Search for articles with an artifact badge; check the deployment instructions.
- **Limitation:** Cluster resources and custom kernels may be required.

#### [103] ACM CCS 2026 Artifacts
- **URL:** https://www.sigsac.org/ccs/CCS2026/call-for/call-for-artifacts.html
- **Type:** Conference program
- **Field:** Cybersecurity
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `security` `code`
- **What to look for:** Guidelines for releasing and evaluating artifacts from security papers.
- **How to use it:** Browse the accepted papers that submitted artifacts; check GitHub or Zenodo.
- **Limitation:** The link is a call for artifacts, not a list of all the code.

#### [104] ISCA 2026 Artifact Evaluation
- **URL:** https://iscaconf.org/isca2026/submit/artifactevaluation.php
- **Type:** Conference program
- **Field:** Computer architecture
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `earth` `open science` `benchmark`
- **What to look for:** Artifacts from hardware, compiler, and performance experiments.
- **How to use it:** Find accepted artifacts; read the toolchain and environment instructions.
- **Limitation:** Specialized hardware can limit reproducibility.

<sub>originally group J: DARTS, software journals, and further code curation</sub>

#### [105] Dagstuhl Artifacts Series (DARTS)
- **URL:** https://drops.dagstuhl.de/entities/journal/DARTS
- **Type:** Artifact journal
- **Field:** Computer science
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `dataset` `code` `benchmark`
- **What to look for:** Artifact publications: code, VMs, datasets, and scripts.
- **How to use it:** Find the related paper, download the artifact package, and read the evaluation README.
- **Limitation:** Some packages are large or depend on specialized tooling.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [152] Graphics Replicability Stamp Initiative (GRSI)
- **URL:** https://www.replicabilitystamp.org/
- **Type:** Artifact evaluation initiative
- **Field:** Computer graphics, visualization
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `materials` `open science` `dataset` `code` `benchmark`
- **What to look for:** Papers that earned a replicability rating, along with their code and data links.
- **How to use it:** Pick a year and a certified paper; inspect the materials and the reproduction instructions.
- **Limitation:** The rating follows the GRSI protocol; it is not a guarantee that the experiments run easily.

#### [153] Graphics Replicability Database
- **URL:** https://graphicsreplicability.github.io/replicability.graphics/
- **Type:** Replication database
- **Field:** Computer graphics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `dataset`
- **What to look for:** A mapping from graphics papers to artifacts and replication status.
- **How to use it:** Look up the paper and follow the source or data links it cites, verifying each one.
- **Limitation:** Coverage and freshness of the records can be limited.

### Paper discovery (13)

<sub>originally group C: Paper search engines you can trace back to code</sub>

#### [027] arXiv
- **URL:** https://arxiv.org/
- **Type:** Preprint
- **Field:** CS, ML, mathematics, physics
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `physics` `code`
- **What to look for:** Manuscripts and the GitHub or project links the authors list.
- **How to use it:** Search by paper title; check the abstract, the HTML page, the PDF, and the appendix.
- **Limitation:** Preprints have not necessarily been peer reviewed; code is optional.

#### [028] alphaXiv
- **URL:** https://www.alphaxiv.org/
- **Type:** Paper explorer
- **Field:** AI and arXiv
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `general`
- **What to look for:** arXiv papers, discussion, and research exploration features.
- **How to use it:** Search by arXiv ID; check the project links and the replication discussion.
- **Limitation:** Feature and link availability can change.

#### [029] Cool Papers
- **URL:** https://papers.cool/
- **Type:** Paper curation
- **Field:** AI and ML
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** A browsable feed of popular papers and AI topics.
- **How to use it:** Use the topic or conference filter to shortlist papers, then find the repo on the authors' site.
- **Limitation:** A discovery platform, not a guarantee that a repository is complete.

#### [037] Semantic Scholar
- **URL:** https://www.semanticscholar.org/
- **Type:** Paper search engine
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `api` `code` `doi`
- **What to look for:** Metadata, citations, paper versions, and external links.
- **How to use it:** Search the exact title or DOI, then move on to the author page and the code availability statement.
- **Limitation:** Not a primary host for source code.

#### [038] Google Scholar
- **URL:** https://scholar.google.com/
- **Type:** Paper search engine
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Citations, PDF versions, and publication pages.
- **How to use it:** Search by title plus "github", or plus "supplementary code".
- **Limitation:** Results need verification; not every link is free or still valid.

#### [039] Connected Papers
- **URL:** https://www.connectedpapers.com/
- **Type:** Literature map
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `ml` `code` `doi`
- **What to look for:** A network graph of related papers.
- **How to use it:** Enter the DOI of a reference paper; find the predecessor and successor methods, then check the code for each.
- **Limitation:** The goal is mapping the literature, not downloading code.

#### [040] ResearchRabbit
- **URL:** https://www.researchrabbit.ai/
- **Type:** Literature map
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Paper collections and citation relationships for exploring a topic.
- **How to use it:** Build a collection of relevant papers, then trace their project sites and GitHub repos.
- **Limitation:** Usually the code has to be found outside the platform.

#### [041] PubMed Central
- **URL:** https://pmc.ncbi.nlm.nih.gov/
- **Type:** Full text archive
- **Field:** Biomedicine
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `biomedical` `code`
- **What to look for:** Full text articles and supplementary files.
- **How to use it:** Search the method, then look for "Code availability" or "Data and code".
- **Limitation:** Source code availability varies by article.

#### [042] Europe PMC
- **URL:** https://europepmc.org/
- **Type:** Paper archive
- **Field:** Biomedical
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `biomedical` `materials` `api` `dataset` `code` `doi`
- **What to look for:** Publications, metadata, and supplementary material.
- **How to use it:** Search by title and DOI; follow the software and data links and the availability statements.
- **Limitation:** Not all of them have a source repository.

#### [044] CORE
- **URL:** https://core.ac.uk/
- **Type:** Open access aggregator
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `materials` `open science` `code`
- **What to look for:** Open access manuscripts from institutional repositories.
- **How to use it:** Find the paper; review its Availability section and supplementary material.
- **Limitation:** An open access paper does not imply open-source code.

<sub>originally group J: DARTS, software journals, and further code curation</sub>

#### [110] Papers We Love
- **URL:** https://github.com/papers-we-love/papers-we-love
- **Type:** Paper curation
- **Field:** Computer science
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Classic and modern papers for studying algorithm ideas.
- **How to use it:** Pick a topic, read the paper, then look for the implementation separately.
- **Limitation:** Not a repository of paper code itself.

<sub>originally group N: Earlier sources plus duplicate markers</sub>

#### [132] Hugging Face Papers
- **URL:** https://huggingface.co/papers
- **Type:** Paper discovery
- **Field:** AI and ML
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `dataset` `code`
- **What to look for:** Papers, arXiv links, models, and related code or dataset resources.
- **How to use it:** Search by title or task; check the related Code/Models/Datasets.
- **Limitation:** Not every paper has open-source training code.

<sub>originally group T: Benchmarks, datasets, and paper implementation research</sub>

#### [194] INSPIRE-HEP
- **URL:** https://inspirehep.net/
- **Type:** Paper discovery plus resources
- **Field:** High-energy physics
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `materials` `physics` `api` `dataset` `code` `doi`
- **What to look for:** High-energy physics paper metadata, identifiers, experiments, and related data or software links.
- **How to use it:** Search by HEP DOI or arXiv ID; follow the related resources to datasets or code when available.
- **Limitation:** A literature index, not a direct code portal.

### Proceedings & publisher (11)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [011] MICCAI Open Access
- **URL:** https://papers.miccai.org/
- **Type:** Proceedings
- **Field:** Medical imaging AI
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `biomedical` `materials` `open science` `dataset` `code`
- **What to look for:** Conference papers plus code or data links when the authors share them.
- **How to use it:** Search by MICCAI title or year; check the resources section, the supplementary material, and GitHub.
- **Limitation:** Code availability differs from article to article.
- **Correction:** 2026-10-12: papers.miccai.org redirects to miccai.org/publications/miccai-open-access-reviews/. The destination page is valid.

<sub>originally group C: Paper search engines you can trace back to code</sub>

#### [031] CVF Open Access
- **URL:** https://openaccess.thecvf.com/
- **Type:** Proceedings
- **Field:** Computer vision
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `ml` `materials` `open science`
- **What to look for:** CVPR/ICCV/WACV papers and supplementary materials.
- **How to use it:** Search by year and title; follow the project page, PDF, and GitHub.
- **Limitation:** Not every paper ships an implementation release.

#### [032] ACL Anthology
- **URL:** https://aclanthology.org/
- **Type:** Proceedings
- **Field:** NLP
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** ACL, EMNLP, and other language conference articles.
- **How to use it:** Find the paper; check its Code/Data Availability section and project site.
- **Limitation:** Publication attachments are not always source code.

#### [033] PMLR
- **URL:** https://proceedings.mlr.press/
- **Type:** Proceedings
- **Field:** Machine learning
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `ml` `materials` `code`
- **What to look for:** Proceedings papers and supplemental material where it is provided.
- **How to use it:** Search the method or conference, then follow author links and the appendix.
- **Limitation:** Code depends entirely on the paper and the venue policy.

#### [034] NeurIPS Proceedings
- **URL:** https://proceedings.neurips.cc/
- **Type:** Proceedings
- **Field:** AI, deep learning
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `ml` `materials` `code`
- **What to look for:** NeurIPS papers and supplementary material.
- **How to use it:** Search for a paper; open the supplementary files and any project or code links.
- **Limitation:** Not every submission releases public code.

#### [035] USENIX Security
- **URL:** https://www.usenix.org/conferences/byname/108
- **Type:** Security proceedings
- **Field:** Cybersecurity
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `security` `licence`
- **What to look for:** Papers, appendices, and artifacts for selected studies.
- **How to use it:** Search by topic or venue per year, then look for an artifact badge or GitHub.
- **Limitation:** Some artifacts are restricted for security, privacy, or licensing reasons.

#### [036] NDSS Symposium
- **URL:** https://www.ndss-symposium.org/
- **Type:** Security proceedings
- **Field:** Network and system security
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `security` `code`
- **What to look for:** Papers and references to the authors' project or code.
- **How to use it:** Browse by conference year; open the paper and the artifacts it mentions.
- **Limitation:** Code is not guaranteed to be available for every paper.

#### [045] IEEE Xplore
- **URL:** https://ieeexplore.ieee.org/
- **Type:** Publisher and proceedings
- **Field:** Engineering, cybersecurity, AI
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `security` `materials`
- **What to look for:** Technical articles, DOIs, and supplementary material where it exists.
- **How to use it:** Find the paper, then check the supplemental material and the authors' project site.
- **Limitation:** Much of the content requires an institutional subscription.

#### [046] ACM Digital Library
- **URL:** https://dl.acm.org/
- **Type:** Publisher/proceedings
- **Field:** Computer science
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `materials` `open science`
- **What to look for:** Papers, artifact badges, supplementary files, and DOIs.
- **How to use it:** Search for a paper and the Artifacts Available, Artifacts Evaluated, or Results Reproduced badges.
- **Limitation:** Access to the paper or its material may be restricted.

<sub>originally group J: DARTS, software journals, and further code curation</sub>

#### [108] SciPy Proceedings
- **URL:** https://proceedings.scipy.org/
- **Type:** Proceedings
- **Field:** Scientific Python
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Papers on the SciPy ecosystem, packages, and notebooks.
- **How to use it:** Search a Python topic; follow the software repo and the article notebook.
- **Limitation:** Papers and implementations are often spread across several repos.

#### [109] SciPy Proceedings Source
- **URL:** https://github.com/scipy-conference/scipy_proceedings
- **Type:** Proceedings repository
- **Field:** Scientific Python
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** The proceedings source, paper assets, and review process.
- **How to use it:** Search for an article by name and match the source against the author's external repo.
- **Limitation:** Mainly proceedings source, not a catalog of application code.

### Reproducibility platform (10)

<sub>originally group B: Research code repositories and executable papers</sub>

#### [025] Renku
- **URL:** https://renkulab.io/
- **Type:** Reproducibility platform
- **Field:** Data science
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `earth` `open science` `api` `dataset` `code`
- **What to look for:** Collaborative compute projects, workflows, and research environments.
- **How to use it:** Search public projects and study their metadata, repository, and workflow.
- **Limitation:** Depends heavily on the project's publication settings and access.

#### [026] Binder
- **URL:** https://mybinder.org/
- **Type:** Notebook execution
- **Field:** Jupyter and data science
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `dataset` `code`
- **What to look for:** Running notebook repositories as temporary environments.
- **How to use it:** Take the GitHub or GitLab repo from the paper and try launching it through Binder.
- **Limitation:** Binder itself is not a paper index; environments can fail on dependency issues.

<sub>originally group G: Code journals and specialized scientific notebooks</sub>

#### [081] Whole Tale
- **URL:** https://wholetale.readthedocs.io/en/stable/
- **Type:** Reproducibility platform
- **Field:** Scientific computing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `earth` `open science` `dataset` `code`
- **What to look for:** Background on reproducible packaging and workflow documentation.
- **How to use it:** Learn how to export a tale, which bundles code, data, and environment together.
- **Limitation:** This link is documentation, not a publication catalog.

<sub>originally group K: Algorithm and computational model archives</sub>

#### [119] CERN REANA
- **URL:** https://github.com/reanahub/reana
- **Type:** Framework
- **Field:** HEP reproducibility
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `open science`
- **What to look for:** A platform for running reproducible computational workflows.
- **How to use it:** Learn the orchestrator; look for analysis examples you can rebuild.
- **Limitation:** This is infrastructure, not a database of every paper.

#### [120] REANA Demo BSM Search
- **URL:** https://github.com/reanahub/reana-demo-bsm-search
- **Type:** Example workflow
- **Field:** High-energy physics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `physics`
- **What to look for:** Analysis demo repositories with scripts and workflows.
- **How to use it:** Read the workflow YAML and the input, processing, and output stages.
- **Limitation:** A single example project, not a general-purpose search directory.

<sub>originally group N: Earlier sources plus duplicate markers</sub>

#### [131] Code Ocean Capsules
- **URL:** https://codeocean.com/explore/capsules/
- **Type:** Executable research
- **Field:** Cross-disciplinary
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `dataset` `code`
- **What to look for:** Code, data, environment, and run packages for a paper's results.
- **How to use it:** Search by title or article; open the Compute Capsule and the run procedure.
- **Limitation:** Some capsules or resources require particular access or a specific environment.

<sub>originally group N: Workflows, research code, and model directories</sub>

#### [141] WorkflowHub
- **URL:** https://workflowhub.eu/
- **Type:** Workflow registry
- **Field:** Bioinformatics, cross-disciplinary computing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `biomedical` `api` `dataset`
- **What to look for:** Scientific workflows, workflow files, author metadata, and publication links.
- **How to use it:** Search the method title or a keyword, then open the workflow and check its files and paper references.
- **Limitation:** Not every workflow ships a full dataset, and engine formats vary.

#### [142] Dockstore
- **URL:** https://dockstore.org/
- **Type:** Workflow registry
- **Field:** Bioinformatics and reproducible computing
- **Stage:** Reproduce the experiment (`04-reproduce`)
- **Tags:** `ml` `biomedical` `open science` `dataset` `code`
- **What to look for:** Containerized workflows and CWL, WDL, Nextflow, or Galaxy descriptors tied to research.
- **How to use it:** Search for a workflow and check its source repository, container image, test files, and version.
- **Limitation:** Running a workflow may require compute or cloud resources, containers, or data access.

#### [143] nf-core Pipelines
- **URL:** https://nf-co.re/pipelines/
- **Type:** Open-source pipeline
- **Field:** Bioinformatics, genomics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Nextflow pipelines complete with source code, documentation, parameters, and literature.
- **How to use it:** Pick a pipeline by type of analysis; open its GitHub repo and usage guide.
- **Limitation:** The focus is bioinformatics, and the pipeline version has to be matched to the paper.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [156] Galaxy Tool Shed
- **URL:** https://toolshed.g2.bx.psu.edu/
- **Type:** Workflow tool repository
- **Field:** Bioinformatics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Analysis tools, wrappers, dependencies, workflows, and scientific references.
- **How to use it:** Search a package name, then check the install info and the developer repository.
- **Limitation:** Many items are wrappers around external tools, not the full algorithm code.

### Paper-to-code lookup (10)

<sub>originally group D: Direct source code implementations</sub>

#### [048] GitHub Topic: paper-implementations
- **URL:** https://github.com/topics/paper-implementations
- **Type:** Curated repos
- **Field:** AI and other fields
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Repositories tagged as paper implementations.
- **How to use it:** Sort by recently updated; check the citation, README, and training scripts.
- **Limitation:** Tags are managed by the repo owner and are not proof of completeness.

#### [049] GitHub Topic: paper-implementation
- **URL:** https://github.com/topics/paper-implementation
- **Type:** Curated repositories
- **Field:** AI and adjacent fields
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code` `doi`
- **What to look for:** Repositories implementing methods from papers.
- **How to use it:** Use topic search, then match the DOI or title against the repository.
- **Limitation:** The label does not prove the experiments match the paper.

#### [050] GitHub Topic: research-paper-implementation
- **URL:** https://github.com/topics/research-paper-implementation
- **Type:** Repo curation
- **Field:** Computer science
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Implementations of methods from papers, flagged by the community.
- **How to use it:** Filter by Python, activity level, and how well the repo matches the paper.
- **Limitation:** The repository may be a third-party implementation.

<sub>originally group F: Curated GitHub lists for papers and code</sub>

#### [067] amusi CVPR2026 Papers with Code
- **URL:** https://github.com/amusi/CVPR2026-Papers-with-Code
- **Type:** Curated GitHub list
- **Field:** Computer vision
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** A list of CVPR 2026 papers with code resources where available.
- **How to use it:** Search the README for a task or model name; follow the GitHub or project links.
- **Limitation:** A community-curated repository, so the links may not always be kept up to date.

<sub>originally group J: DARTS, software journals, and further code curation</sub>

#### [111] GitHub Topic: reproducible-paper
- **URL:** https://github.com/topics/reproducible-paper
- **Type:** Curated repos
- **Field:** Scientific computing
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `open science` `code`
- **What to look for:** Repositories tagged as paper replication packages.
- **How to use it:** Find repositories with scripts and an environment, and match them to the publication.
- **Limitation:** The topics are assigned by the repo owners themselves.

<sub>originally group L: Paper-to-repository knowledge graphs</sub>

#### [121] Linked Papers With Code
- **URL:** https://linkedpaperswithcode.com/
- **Type:** Knowledge graph
- **Field:** Machine learning
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `ml` `dataset` `code`
- **What to look for:** Relations among papers, methods, datasets, and code links drawn from PWC data.
- **How to use it:** Search the title or method and follow the repository and dataset entries.
- **Limitation:** Some sources are historical; check the refresh date.

<sub>originally group N: Earlier sources plus duplicate markers</sub>

#### [130] CatalyzeX
- **URL:** https://www.catalyzex.com/
- **Type:** Paper-to-code search
- **Field:** AI and ML
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Search for GitHub implementations linked to a paper.
- **How to use it:** Enter the paper title or arXiv ID, then open the "Code" tab or the linked repository.
- **Limitation:** Links may point to third-party implementations, so check that they are valid.

#### [133] GitHub Topic: paper-implementations (duplikat no. 48)
- **URL:** https://github.com/topics/paper-implementations
- **Type:** Curated repositories
- **Field:** AI and adjacent fields
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `general`
- **What to look for:** The exact same link as entry 48.
- **How to use it:** Use the search guidance in entry 48.
- **Limitation:** DUPLICATE URL, kept as a trace of the first list rather than counted as a unique site.

#### [138] Papers With Code Data Archive
- **URL:** https://github.com/paperswithcode/paperswithcode-data
- **Type:** Metadata archive
- **Field:** Machine learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `api` `dataset` `code` `benchmark`
- **What to look for:** Historical data on papers, repos, tasks, and benchmark relationships.
- **How to use it:** Use the metadata dump for bulk or offline search, then validate the repo URLs.
- **Limitation:** A historical source; do not treat it as a current index.

#### [140] Papers With Code (situs historis)
- **URL:** https://paperswithcode.com/
- **Type:** Historical portal
- **Field:** Machine learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code` `benchmark`
- **What to look for:** Once linked papers, code, and leaderboards.
- **How to use it:** Use archive entry 138 or a newer alternative; do not rely on the old site.
- **Limitation:** Service status has changed or shut down; this is a historical entry, not an active recommendation.
- **Correction:** 2026-10-12: redirect to huggingface.co/papers/trending confirmed, consistent with the historical note. Use the archive in entry 138 for data.

### Lab & organization repository (10)

<sub>originally group M: Official AI lab repositories</sub>

#### [125] Google Research Code
- **URL:** https://github.com/google-research/google-research
- **Type:** Lab repository
- **Field:** AI and ML
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `code`
- **What to look for:** Official implementations and companions to Google Research papers.
- **How to use it:** Search the paper name in the subfolders, then read the README and the experiment commands.
- **Limitation:** Many projects are old, and environment setup varies.

#### [126] Google DeepMind Research
- **URL:** https://github.com/google-deepmind/deepmind-research
- **Type:** Lab repository
- **Field:** AI and ML
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `dataset` `code` `benchmark` `licence`
- **What to look for:** Code released alongside DeepMind papers.
- **How to use it:** Search by paper name; look at the training and evaluation code and the license.
- **Limitation:** Not every research model, weight set, or dataset is released.

#### [127] Meta Research GitHub
- **URL:** https://github.com/facebookresearch
- **Type:** Organization repository
- **Field:** AI and ML
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Meta research source code and related libraries.
- **How to use it:** Search for a research name or architecture; pick the official repository.
- **Limitation:** A large organization account; not all of its code maps to a paper.

#### [128] Ai2 Research Papers
- **URL:** https://allenai.org/papers
- **Type:** Lab catalog
- **Field:** NLP, AI, and agents
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Ai2 publications and project or code links where available.
- **How to use it:** Search a paper or model; check the links on its publication page.
- **Limitation:** Publication pages may point to external repos.

#### [129] Google Research Publications
- **URL:** https://research.google/pubs/
- **Type:** Publication catalog
- **Field:** AI and computational science
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `code`
- **What to look for:** Google research articles to match against a repository.
- **How to use it:** Search the title, then match it against the google-research or DeepMind repository.
- **Limitation:** Does not host source code directly.

<sub>originally group R: Deep learning and NLP implementations</sub>

#### [175] TensorFlow Model Garden
- **URL:** https://github.com/tensorflow/models
- **Type:** Model code repository
- **Field:** Vision, NLP, speech, reinforcement learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `open science` `code`
- **What to look for:** Research model code from published papers, training scripts, models, and documentation.
- **How to use it:** Open research/ or official/; pick a paper and match the TensorFlow version.
- **Limitation:** Some older models use TensorFlow 1 and need adjustment.

#### [176] PyTorch Examples
- **URL:** https://github.com/pytorch/examples
- **Type:** Code and baseline examples
- **Field:** Deep learning across tasks
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `open science` `code`
- **What to look for:** Examples of CNN, Transformer, VAE, GAN, and RL models plus simple training scripts.
- **How to use it:** Find the model or task folder; run the baseline, then trace the algorithm reference.
- **Limitation:** Educational examples do not always reproduce a paper's configuration in full.

#### [177] timm / PyTorch Image Models
- **URL:** https://github.com/huggingface/pytorch-image-models
- **Type:** Architecture implementations
- **Field:** Computer vision
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `benchmark`
- **What to look for:** Implementations of many paper architectures, pretrained weights, and training or evaluation scripts.
- **How to use it:** Search the architecture or paper in the model docs, run the script, and check the weights.
- **Limitation:** Weights and variants differ, so check the citation and the exact configuration.

#### [180] OpenNMT
- **URL:** https://opennmt.net/
- **Type:** NLP model toolkit
- **Field:** Machine translation, sequence modeling
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `general`
- **What to look for:** Seq2seq and Transformer implementations, training documentation, and paper references.
- **How to use it:** Pick the PyTorch or TensorFlow toolkit and follow the training and validation scripts.
- **Limitation:** The framework is not a universal paper index; check the version and tokenization.

#### [181] fairseq
- **URL:** https://github.com/facebookresearch/fairseq
- **Type:** NLP paper implementation
- **Field:** Machine translation, speech, language modeling
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** A seq-to-seq repository plus a list of the research it implements.
- **How to use it:** Start from the list of implemented papers, then follow the examples folder and the configuration.
- **Limitation:** Some papers rely on old dependencies or models, so check maintenance status.

### Curated list (9)

<sub>originally group F: Curated GitHub lists for papers and code</sub>

#### [068] firetix Awesome CVPR 2026 Papers
- **URL:** https://github.com/firetix/awesome-cvpr-2026-papers
- **Type:** Curated GitHub
- **Field:** Computer vision
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** Collection of CVPR 2026 papers by topic, plus resources.
- **How to use it:** Filter by category; check whether a code label means source or just a project page.
- **Limitation:** Do not equate a demo or model with full training code.

#### [069] MICCAI OpenSourcePapers
- **URL:** https://github.com/JunMa11/MICCAI-OpenSourcePapers
- **Type:** Curated GitHub list
- **Field:** Medical AI
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** MICCAI papers with source and resource links.
- **How to use it:** Search the method name, paper, or year, then follow the authors' repository.
- **Limitation:** Some links move or change version.

#### [070] Awesome MICCAI 2026
- **URL:** https://github.com/ambicuity/Awesome-MICCAI-2026
- **Type:** GitHub curation
- **Field:** Medical AI
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `biomedical` `dataset` `code`
- **What to look for:** Lists of MICCAI 2026 papers and their public repositories.
- **How to use it:** Search by medical image task and check the code URL for each paper.
- **Limitation:** Data and replication completeness still needs verification.

#### [071] Awesome AI for Cybersecurity Papers
- **URL:** https://github.com/BaichengDanny/awesome-ai-for-cybersecurity-papers
- **Type:** Curated GitHub list
- **Field:** AI for cybersecurity
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `security` `dataset` `code` `benchmark`
- **What to look for:** Papers, benchmarks, and some implementation links.
- **How to use it:** Pick a subarea such as intrusion, malware, or vulnerability; open the original code and data.
- **Limitation:** Some entries may be literature references only.

#### [072] Awesome ML for Cybersecurity
- **URL:** https://github.com/jivoi/awesome-ml-for-cybersecurity
- **Type:** Curated GitHub
- **Field:** Cybersecurity
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `security` `dataset`
- **What to look for:** Lists of papers, tools, datasets, and security ML resources.
- **How to use it:** Find dataset sources or baselines that match a given attack or scenario.
- **Limitation:** Entries vary in quality and freshness.

#### [073] Machine Learning for Cyber Security
- **URL:** https://github.com/wtsxDev/Machine-Learning-for-Cyber-Security
- **Type:** Curated GitHub list
- **Field:** Cybersecurity
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `security` `materials` `dataset` `code`
- **What to look for:** Method material, datasets, and reading for ML security.
- **How to use it:** Pick a method category, then continue to the original source and GitHub.
- **Limitation:** Do not assume every resource has complete code.

#### [074] OpenSci Awesome ML Cybersecurity
- **URL:** https://github.com/opensci-hub/Awesome-ML-Cybersecurity
- **Type:** GitHub curation
- **Field:** Cybersecurity
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `security`
- **What to look for:** Collections of literature and security ML tools.
- **How to use it:** Search by detection or classification technique and compare the active repositories.
- **Limitation:** A community index is not an assessment of method performance.

#### [075] Awesome AI Papers
- **URL:** https://github.com/songqiang321/Awesome-AI-Papers
- **Type:** Curated GitHub list
- **Field:** AI
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code` `doi`
- **What to look for:** A list of AI publications and supporting links.
- **How to use it:** Search for a research term; note the arXiv ID or DOI, then look for the implementation.
- **Limitation:** The share of entries that come with code can differ by topic.

#### [076] Awesome CV MasterHub
- **URL:** https://github.com/cuixing158/Awesome-CV-MasterHub
- **Type:** Curated GitHub
- **Field:** Computer vision
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** Collections of models, papers, and related code information.
- **How to use it:** Search detection, segmentation, or classification, then check the source link.
- **Limitation:** Check whether the paper and code links still work.

### Metadata & knowledge graph (8)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [005] OpenAIRE Explore
- **URL:** https://explore.openaire.eu/
- **Type:** Scholarly discovery
- **Field:** Cross-disciplinary
- **Stage:** Find the paper (`01-discover`)
- **Tags:** `open science` `api` `dataset` `code`
- **What to look for:** Publication, data, and software metadata, plus the links between them.
- **How to use it:** Find a publication, then use the research output relations to reach the software or dataset.
- **Limitation:** Not every metadata link points at code you can actually download.

<sub>originally group C: Paper search engines you can trace back to code</sub>

#### [043] OpenAlex
- **URL:** https://openalex.org/
- **Type:** Metadata/API
- **Field:** Cross-disciplinary
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `api` `code`
- **What to look for:** An index of papers, DOIs, topics, institutions, and citation relations.
- **How to use it:** Use the web interface or API to find works, then enrich them with GitHub or Zenodo.
- **Limitation:** It does not specifically provide a complete index of code repositories.

<sub>originally group L: Paper-to-repository knowledge graphs</sub>

#### [122] SemRepo
- **URL:** https://semrepo.org/
- **Type:** Knowledge graph
- **Field:** Research software
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `ml` `open science` `api` `code`
- **What to look for:** Metadata on scholarly repositories and their links to publications.
- **How to use it:** Search for a repo or paper; explore the graph, dependencies, and code links.
- **Limitation:** Coverage and snapshot freshness need validation.

#### [123] SemRepo Source
- **URL:** https://github.com/faerber-lab/semrepo
- **Type:** Source platform
- **Field:** Scientific metadata
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `api` `code`
- **What to look for:** The code and pipeline that build the SemRepo knowledge graph.
- **How to use it:** Read the docs and the schema to integrate it into your own search system.
- **Limitation:** It is the source of the indexer, not a collection of the implementation behind each paper.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [151] zbMATH Open (swMATH records)
- **URL:** https://zbmath.org/
- **Type:** Mathematical software index
- **Field:** Computational mathematics
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `ml` `open science` `api` `code`
- **What to look for:** Links between mathematical software and its citations and scholarly literature.
- **How to use it:** Search by software or algorithm name; follow the metadata and the implementation references.
- **Limitation:** A bibliographic index; you still have to track down the publisher site or a separate repository.

<sub>originally group P: Academic repositories and data networks</sub>

#### [162] DataCite Commons
- **URL:** https://commons.datacite.org/
- **Type:** DOI/metadata search
- **Field:** Cross-disciplinary
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `api` `dataset` `code` `doi`
- **What to look for:** DOI relationships between publications, datasets, software, and contributors.
- **How to use it:** Search by paper title or DOI; follow the related identifiers, especially software and data.
- **Limitation:** Metadata is not the code file; you still need to visit the target repository.

#### [163] re3data
- **URL:** https://www.re3data.org/
- **Type:** Repository directory
- **Field:** Cross-disciplinary
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `open science` `code`
- **What to look for:** A catalog of scholarly repositories with information on type, access, and policy.
- **How to use it:** Filter by discipline or content type to find new repositories that accept software.
- **Limitation:** A directory of platforms, not a place to download software directly.

#### [164] FAIRsharing
- **URL:** https://fairsharing.org/
- **Type:** Data/standards registry
- **Field:** Life sciences, cross-disciplinary
- **Stage:** For agents and automation (`05-agents`)
- **Tags:** `biomedical` `open science` `api` `dataset` `code`
- **What to look for:** Research databases, metadata standards, and repository policies.
- **How to use it:** Search a field or method; pick a linked database, then check its resources.
- **Limitation:** Usually does not index paper source code directly.

### Package index (7)

<sub>originally group B: Research code repositories and executable papers</sub>

#### [022] Bioconductor
- **URL:** https://bioconductor.org/packages/release/bioc/
- **Type:** Software package
- **Field:** R bioinformatics
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `biomedical` `code`
- **What to look for:** Open-source packages, source tarballs, vignettes, and citations.
- **How to use it:** Search for a package or an analysis task; read the vignette and its citation article.
- **Limitation:** Focused on R/Bioconductor, not papers across every field.
- **Correction:** 2026-10-12: /packages/ returned 404. Changed to /packages/release/bioc/ (verified 200).

#### [023] CRAN Packages
- **URL:** https://cran.r-project.org/web/packages/
- **Type:** Software package
- **Field:** R, statistics and data mining
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `social` `dataset` `code`
- **What to look for:** Source code of R packages, documentation, and method references.
- **How to use it:** Search by method name; open the Reference manual, the source, and DESCRIPTION.
- **Limitation:** A package is not a substitute for reading the paper behind the method.

#### [024] PyPI
- **URL:** https://pypi.org/
- **Type:** Software package
- **Field:** Python
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Libraries plus links to source or publication pages when listed.
- **How to use it:** Search for packages related to an algorithm; follow the project links to the source and paper.
- **Limitation:** A PyPI upload has not automatically gone through scientific peer review.

<sub>originally group D: Direct source code implementations</sub>

#### [055] R-universe
- **URL:** https://r-universe.dev/
- **Type:** Scientific packages
- **Field:** R
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** R packages, binaries, and source links from various communities.
- **How to use it:** Search for a package of analysis functions, then continue to its repository and the article to cite.
- **Limitation:** Not a comprehensive index of paper code.

<sub>originally group H: Paper, data, notebook, and software portals</sub>

#### [086] pyOpenSci Packages
- **URL:** https://www.pyopensci.org/python-packages/
- **Type:** Software review
- **Field:** Scientific Python
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `dataset` `code`
- **What to look for:** Curated Python packages with open reviews.
- **How to use it:** Search by data processing task; open the source, the review, and the documentation.
- **Limitation:** A software quality review is not validation of every claim in a paper.

#### [087] rOpenSci Packages
- **URL:** https://ropensci.org/packages/
- **Type:** Software review
- **Field:** R and open science
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `materials` `code`
- **What to look for:** Research R packages, documentation, source, and some reviews.
- **How to use it:** Filter by package category and study the reference material and the source repository.
- **Limitation:** Better suited to the R ecosystem.

<sub>originally group O: Algorithms, software journals, and reproducibility</sub>

#### [155] Julia Packages
- **URL:** https://juliapackages.com/packages
- **Type:** Package index
- **Field:** Mathematics, optimization, machine learning
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `code`
- **What to look for:** Julia packages with repositories, some of which have an academic paper.
- **How to use it:** Search by algorithm or field, then continue to the source link and the article to cite.
- **Limitation:** A package directory, not an index of papers that always contain experiment code.

### Code search & hosting (5)

<sub>originally group A: Research code and reproducibility platforms</sub>

#### [006] Software Heritage
- **URL:** https://archive.softwareheritage.org/
- **Type:** Code archive
- **Field:** Cross-disciplinary
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `dataset` `code`
- **What to look for:** Source code snapshots and archived software history.
- **How to use it:** Look up the repo URL or identifier from the paper; check whether the code revision was archived.
- **Limitation:** A code archive does not automatically include datasets or execution instructions.

<sub>originally group D: Direct source code implementations</sub>

#### [047] GitHub Code Search
- **URL:** https://github.com/search?type=code
- **Type:** Code search
- **Field:** Cross-domain
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `dataset` `code` `doi` `licence`
- **What to look for:** Source files and repositories matching specific terms.
- **How to use it:** Search for an exact paper title, method name, DOI, function name, or dataset.
- **Limitation:** Check the license, the commits, and the authenticity of the authors; results are not peer reviewed.

#### [051] GitLab Explore
- **URL:** https://gitlab.com/explore
- **Type:** Code hosting
- **Field:** Cross-domain
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `code`
- **What to look for:** Repositories and software projects that have been made public.
- **How to use it:** Search GitLab for an algorithm name or a paper title.
- **Limitation:** Not everything is tied to a publication, and some projects are private.

#### [056] Codeberg Explore
- **URL:** https://codeberg.org/explore/repos
- **Type:** Code hosting
- **Field:** Open-source
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `api` `code`
- **What to look for:** Alternative open-source repositories.
- **How to use it:** Use the method name, the paper, and author names as keywords.
- **Limitation:** Academic metadata coverage is inconsistent.

#### [057] SourceForge Directory
- **URL:** https://sourceforge.net/directory/
- **Type:** Software directory
- **Field:** Cross-disciplinary
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `open science` `code`
- **What to look for:** Software, releases, and downloads for technical projects.
- **How to use it:** Search for scientific computing tools, then check the source, documentation, and publications.
- **Limitation:** Many tools are not reproductions of a specific paper.

### Workflow registry (2)

<sub>originally group H: Paper, data, notebook, and software portals</sub>

#### [089] ESA EarthCODE Workflows
- **URL:** https://earthcode.esa.int/workflows
- **Type:** Research workflow
- **Field:** Earth observation
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `earth` `api` `code`
- **What to look for:** Compute workflows, metadata, and geospatial research output.
- **How to use it:** Search workflows by sensor or method, then trace the code artifact.
- **Limitation:** Some work is tied to specific cloud or vendor services.

<sub>originally group S: Materials science, energy, and research software</sub>

#### [187] AiiDA
- **URL:** https://aiida.net/
- **Type:** Workflow reproducibility
- **Field:** Scientific computing, materials simulation
- **Stage:** Find the code (`02-find-code`)
- **Tags:** `ml` `materials` `open science` `code`
- **What to look for:** A Python workflow framework, provenance graph, and plugins that connect to simulation software.
- **How to use it:** Find the AiiDA workflow or plugin the authors used; import it and run the process.
- **Limitation:** AiiDA is infrastructure, not a complete catalog of every paper.
