# Paper, code, data, reproduction

A directory of **200 sources** for the work that sits between "I found an interesting paper" and "I have its implementation running on my machine."

Finding the paper is the easy part. Finding the code the authors actually wrote, the dataset they trained it on, the environment that makes the numbers come out the same, and a citation for each of those as a separate object, that is where the hours go. This repo collects the places that shorten the search.

```
find the paper  →  find the code  →  find the data  →  reproduce  →  automate
      01               02                03               04           05
```

## What is different here

Three things, and they matter more than the size of the list.

1. **It is sorted by what you are trying to do.** The original compilation grouped sources into alphabetical sections A through T. That grouping served whoever assembled it, not the reader. Here everything sits in five workflow stages, so a concrete question ("where is the code for this paper?") points at one section instead of the whole list.
2. **The links were actually checked.** [`scripts/audit_links.py`](scripts/audit_links.py) probes all 200 URLs and classifies each one. The results carry a date and live in [`audit/liveness.md`](audit/liveness.md). Anyone can rerun it and get the same picture, and a GitHub Action does exactly that every Monday so the list does not quietly rot.
3. **The content is data, not just prose.** [`data/sources.json`](data/sources.json) and the CSV beside it hold everything the markdown pages hold, plus audit fields, so you can filter it, load it into another tool, or hand it to an agent. A list you cannot query is a list you read once and forget.

## Audit status

<!-- AUDIT-TABLE-START -->
**Last audit: 2026-10-12.** All 200 URLs probed by `scripts/audit_links.py`, 15s timeout, 24 workers.

| Status | Count | Meaning |
|---|---:|---|
| `alive` | 171 | Reachable and serving content |
| `redirected` | 3 | Has moved to another host, so the listed URL is stale |
| `bot_walled` | 17 | Refuses automated clients; **normal in a browser** |
| `rate_limited` | 6 | HTTP 429 during the audit; retry later |
| `timeout` | 3 | Not reachable from the audit host |
| `dead` | 0 | Not applicable |
| `error` | 0 | Not applicable |

Read that table with two things in mind, because the raw counts mislead on their own.

**Twenty-five sources did not fail, they resisted the probe.** `bot_walled` means a Cloudflare-style wall, or a 403 aimed at scripts, and the page opens fine for a person. `timeout` usually means the audit host is filtered out rather than the site being gone. *Journal of Open Research Software* times out from here and is plainly alive, with articles published in September 2026.

**Four links were corrected** once the probe found them broken. Each fix is recorded in the `correction` field of `data/sources.json` instead of being silently swapped, so you can see what changed and when. Bioconductor and CSDMS had both moved to new paths, Wizwand now redirects to sota2.com, and the MICCAI open access index moved within miccai.org. Separately, `paperswithcode.com` redirects to Hugging Face, which confirms Meta shut the site down in July 2025; use the archived dataset (entry 138) rather than the old portal.

**Status legend**, worth reading before you conclude something is broken:

- `alive`: reachable, serves content, same host as listed.
- `redirected`: reachable but on a different host. The listed URL is stale. Real example: `paperswithcode.com` to `huggingface.co`.
- `bot_walled`: refuses automated clients, whether by 401/403 or a challenge page. **Not dead.** Almost always fine in a normal browser, and should not be reported as a broken link.
- `rate_limited`: HTTP 429, temporarily throttling. Check again later.
- `dead`: HTTP 404 or 410, the resource is gone.
- `error` / `timeout`: transport failure: DNS, TLS, refused connection, or no answer in time.

## Contents

- [01 · Find the paper](#01--find-the-paper-31-sources), 31 sources
- [02 · Find the code](#02--find-the-code-100-sources), 100 sources
- [03 · Find the data](#03--find-the-data-17-sources), 17 sources
- [04 · Reproduce the experiment](#04--reproduce-the-experiment-43-sources), 43 sources
- [05 · For agents and automation](#05--for-agents-and-automation-9-sources), 9 sources
- [Where to start](#where-to-start)
- [The six-step workflow](#the-six-step-workflow)
- [Supporting files](#supporting-files)
- [Contributing](#contributing)
- [What is verified, and what is not](#what-is-verified-and-what-is-not)

Full detail on all 200 entries, each with its type, field, what to look for, how to use it, and where it falls short, is in **[DIRECTORY.md](DIRECTORY.md)**.

## 01 · Find the paper (31 sources)

Preprints, proceedings, search engines, and the citation-graph tools that let you work backwards from one good paper.

This is where you start, nearly always. arXiv covers CS, ML, math, and physics. OpenReview shows you the reviews next to the submission, which is often more informative than the paper. PMLR, NeurIPS Proceedings, CVF Open Access, and ACL Anthology are the canonical venues for ML, vision, and NLP in that order. For security, USENIX Security and NDSS matter, and both run artifact policies that make code more likely to exist at all.

Biomedical work routes through PubMed Central and Europe PMC. If you need to know what a venue or funder expects before you commit, PLOS Computational Biology publishes its code availability policy and Nature Scientific Data does the same for data.

For graph exploration rather than keyword search, Connected Papers and ResearchRabbit both let you seed a collection from one paper and see what it cites and what cites it.

## 02 · Find the code (100 sources)

The largest group by far, and where you will spend most of your time. It splits into a few kinds of place, and they are not equally trustworthy.

**Software journals**, where the code is the publication rather than an appendix: JOSS, JMLR MLOSS, Journal of Statistical Software, The R Journal, SoftwareX, Journal of Open Research Software, SciPost Physics Codebases, IPOL, and JOSE. If the paper you care about appeared in one of these, the repository link is on the article page by construction. These are the highest-confidence sources in the directory.

**Paper-to-code lookups**: CatalyzeX (paste a title, get a repository), Code Ocean Capsules (code plus the execution environment), and the Papers With Code data archive. That last one deserves a note. The site is gone, but the data dump is not, and it is the only remaining way to do a bulk offline lookup of paper-to-repository links.

**Code and model hubs**: GitHub code search, GitLab, Codeberg, Hugging Face models and Spaces, PyPI, CRAN, Bioconductor, R-universe, Zenodo. Check `created_at` and `pushed_at` before you commit to anything here. Star counts mean almost nothing on their own.

**Official lab repositories**, when you want the implementation the authors released themselves: Google Research, Google DeepMind, Meta Research, TensorFlow Model Garden, PyTorch Examples, timm, Detectron2, MMDetection, OpenMMLab, fairseq, OpenNMT. Watch the age. Several carry papers from years back and pin old framework versions.

**Curated lists**, ten of them, mostly "Awesome X" collections and conference-specific paper-with-code indexes for CVPR, MICCAI, and AI security. Useful for a first pass, unreliable as a final answer, because a "code available" badge often points at a project page or a demo rather than training code.

## 03 · Find the data (17 sources)

DOI-bearing repositories first: Harvard Dataverse, Zenodo, Figshare, Dryad, Mendeley Data, OSF, and the UCI Machine Learning Repository. The regional Dataverse instances (DataverseNO, Borealis, 4TU.ResearchData) hold a lot that never surfaces in a general search.

Then the field-specific ones, which is usually where the real data lives: PANGAEA for earth and environmental science, CERN Open Data and HEPData for high-energy physics, GigaDB for bioinformatics, Materials Cloud and NOMAD for materials. OpenML is worth knowing for tabular ML benchmarks with published task definitions, and Hugging Face Datasets has become the default for NLP and multimodal data.

A caution that applies to this whole section: a dataset with a DOI is citable research output, which is not the same as a dataset you are permitted to use the way you plan to. Read the license before you build on it.

## 04 · Reproduce the experiment (43 sources)

This is the section that separates a working reproduction from a promising repository, and the one most link lists skip entirely.

**Conference artifact evaluation** is the strongest signal available: Security Research Artifacts, SIGMOD Reproducibility, and the 2026 artifact tracks at ICSE, ISSTA, POPL, PLDI, ICFP, EuroSys, CCS, and ISCA. A paper that passed artifact evaluation had an independent reviewer run the code.

**DARTS** goes a step further. Dagstuhl publishes artifacts as reviewed publications in their own right, with DOIs, so a release there has been examined the way a paper is.

**Replication platforms**: ReScience C, Renku, Whole Tale, WorkflowHub, Dockstore, nf-core. These package code, data, and environment together, which is the part that normally breaks.

**Benchmarks and leaderboards**: MLCommons/MLPerf, Codabench, AIcrowd, EvalAI, Grand Challenge, DrivenData, Kaggle, Open Graph Benchmark, DataPerf, NAB, TimeEval, and the Monash forecasting archive. These give you a baseline to compare against, which is what you need before claiming an improvement.

**Model zoos**: MONAI, BioImage Model Zoo, MMDetection. And for language models, the EleutherAI evaluation harness, which is what a great many published numbers were actually produced with.

## 05 · For agents and automation (9 sources)

The smallest group, and the one almost every list like this omits. If you want to search a thousand papers instead of five, you need metadata endpoints, not web pages.

OpenAlex gives you a full bibliographic API across disciplines. SemRepo is a knowledge graph of research repositories, roughly 190,000 of them, queryable over SPARQL. Linked Papers With Code carries the historical paper-to-repository relations. DataCite Commons resolves the links between a paper's DOI and the DOIs of its software and data. re3data and FAIRsharing help you find repositories you did not know existed.

What that looks like in practice:

```bash
# Paper metadata by title
curl -s "https://api.openalex.org/works?search=graph%20neural%20networks&per-page=5"

# Software registered with a DOI
curl -s "https://api.datacite.org/dois?query=replication%20package&resource-type-id=software"
```

## Where to start

If you read nothing else, these ten carry most of the weight.

| # | Source | Why it earns the slot |
|---|---|---|
| 1 | [**CatalyzeX**](https://www.catalyzex.com/) | Paste a paper title, get a code link. Fastest single move. |
| 2 | [**Papers With Code Data Archive**](https://github.com/paperswithcode/paperswithcode-data) | The site died in July 2025, the data dump did not, and it is queryable in bulk. |
| 3 | [**JOSS**](https://joss.theoj.org/papers) | Papers about software, so the code is the subject of publication. |
| 4 | [**Journal of Statistical Software**](https://www.jstatsoft.org/) | Paper, package, and replication scripts on one page. |
| 5 | [**Zenodo**](https://zenodo.org/) | DOI repository; filter to `Software` for citable releases. |
| 6 | [**Code Ocean**](https://codeocean.com/explore/capsules/) | Not just the code, the execution environment with it. |
| 7 | [**Security Research Artifacts**](https://secartifacts.github.io/) | In security, artifacts are effectively mandatory, so coverage is unusually good. |
| 8 | [**DARTS**](https://drops.dagstuhl.de/entities/journal/DARTS) | Artifacts that were **evaluated**, not merely uploaded. |
| 9 | [**OpenAlex**](https://openalex.org/) | For when you want to automate rather than click. |
| 10 | [**SemRepo**](https://semrepo.org/) | SPARQL queries against a graph of research repositories. |

## The six-step workflow

[CHECKLIST.md](CHECKLIST.md) and [QUERIES.md](QUERIES.md) expand each step.

1. **Start from one paper** with a DOI or arXiv ID. Write down the exact title, the authors, the year, the DOI, what kind of experiment it reports, and which datasets it used.
2. **Find an implementation you can audit.** In order: the paper's own code availability statement, then the authors' or lab's site, then a lookup service, then code hosting, then artifact indexes. Confirm that the README, the paper title, the DOI, and the author identity actually match.
3. **Look for a full reproduction package**, not just a repository. An artifact badge, a DARTS entry, a Code Ocean capsule, or a software journal article is worth more than a promising README. See [CHECKLIST.md](CHECKLIST.md).
4. **Compare the artifact against the paper.** Dataset completeness, preprocessing, the train/validation/test split, random seeds, dependency versions, hyperparameters, hardware, metrics, and whether the scripts can regenerate the paper's tables and figures.
5. **Run the baseline before changing anything.** Use the release or commit that matches the paper. Keep the logs, the environment lockfile, the actual numbers, and the gap between them and the published ones.
6. **Only then modify.** Document what you changed, run ablations, test significance, and cite the paper, the code, and the dataset as three separate objects if all three have identifiers.

## Supporting files

| File | What is in it |
|---|---|
| [`DIRECTORY.md`](DIRECTORY.md) | All 200 entries, sorted by workflow stage |
| [`data/sources.json`](data/sources.json) | Structured data with audit results |
| [`data/sources.csv`](data/sources.csv) | The same, for spreadsheets |
| [`audit/liveness.md`](audit/liveness.md) | Per-link audit output, newest run |
| [`CHECKLIST.md`](CHECKLIST.md) | 16-point checklist for judging a research repository |
| [`QUERIES.md`](QUERIES.md) | 20 ready-to-paste search queries |
| [`scripts/audit_links.py`](scripts/audit_links.py) | The auditor, standard library only |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add or fix an entry |

Loading it from code:

```python
import json, urllib.request
src = json.load(urllib.request.urlopen(
    "https://raw.githubusercontent.com/rayss868/paper-code-datasets/main/data/sources.json"))
cyber = [e for e in src["entries"]
         if "security" in e["bidang"].lower() and e["status"] == "alive"]
print(len(cyber), "live security sources")
```

## Contributing

New sources, corrected URLs, and fixed classifications are all welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first, because the format is strict on purpose: the data files are meant to be processed by machines, not only read.

## What is verified, and what is not

Being precise about this is the difference between a useful directory and a plausible-looking one.

**Verified:**

- The structure of the list: 200 numbered entries in sequence, 199 unique URLs, and exactly one duplicate, where entries 48 and 133 point at the same GitHub topic. The duplicate is kept and labelled rather than quietly removed, since it is evidence of how the list was assembled.
- Host concentration: 200 entries spread over 149 distinct hosts, with `github.com` holding 46 of them, or 23%. Many of those are topic and tag pages rather than independent sources, so the honest count of distinct providers sits well below 200.
- Link liveness, as of the date in the audit table above.

**Not verified:**

- Quantitative claims that appear in some entry descriptions, such as a project's repository count. Those come from whoever compiled the original list, and should be treated as claims until you check the source.
- The quality, license, and completeness of any repository you find through this directory.
- Whether a project is actively maintained rather than abandoned.

**Warnings worth keeping in mind:**

1. A link existing does not mean code exists there. Plenty of these are bibliographic indexes, data archives, or conference program pages.
2. "Official implementation" has to be checked against the author, the lab, and the paper. Plenty of repositories are third-party reimplementations.
3. "Artifact available" and "results reproduced" are different claims, and both differ from "the numbers came out the same on my machine."
4. Software with a DOI is citable, not necessarily correct or bug-free.
5. Older releases often need specific toolchains. Work in a container or VM, and do not run scripts you have not looked at.
6. Most of these catalogs change. Recheck a link when you actually use it.

**A note on history:** Papers With Code (entry 140) was shut down by Meta in July 2025, and the domain now points at Hugging Face Trending Papers. The historical data is still reachable through the archive (entry 138).

## License

The compilation is released under [CC0 1.0 Universal](LICENSE), which places it in the public domain. Use it, change it, redistribute it, no conditions.

Third-party sites and repositories linked from here keep their own licenses.
