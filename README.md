# Paper, code, data, reproduction

**200 sources** for the work between "I found an interesting paper" and "I have its implementation running."

Most directories like this hand you a wall of links and wish you luck. This one is built so you can see the inside before you click anything: every source has a category, a field, tags, and a checked status, and all of it is queryable.

```
find the paper  →  find the code  →  find the data  →  reproduce  →  automate
      01               02                03               04           05
```

## What is inside

| Kind of source | Count | What it gives you |
|---|---:|---|
| Software directory | 24 | Broad software catalogs and indexes |
| Benchmark & leaderboard | 23 | Baselines, evaluation harnesses, leaderboards |
| Dataset repository | 21 | Datasets with DOIs and citable metadata |
| Model & algorithm repository | 19 | Model zoos, simulation models, classic algorithms |
| Software journal | 14 | Papers where the code *is* the publication |
| Artifact evaluation | 14 | Artifacts an independent reviewer actually ran |
| Paper discovery | 13 | Preprints, proceedings, citation graphs |
| Proceedings & publisher | 11 | Venue archives and publisher platforms |
| Reproducibility platform | 10 | Code, data, and environment packaged together |
| Paper-to-code lookup | 10 | Paste a paper, get a repository |
| Lab & organization repository | 10 | Official code from research groups |
| Curated list | 9 | Community-maintained paper-with-code collections |
| Metadata & knowledge graph | 8 | APIs and graphs for automated search |
| Package index | 7 | Package registries across languages |
| Code search & hosting | 5 | Where the code physically lives |
| Workflow registry | 2 | Scientific pipelines as reusable artifacts |

Tagged across fields, with counts: `code` 172, `dataset` 82, `ml` 46, `open science` 41, `benchmark` 39, `api` 34, `materials` 34, `biomedical` 31, `doi` 21, `earth` 21, `licence` 14, `physics` 9, `security` 9, `social` 7.

Filter it yourself:

```bash
# Everything tagged security, still alive
jq -r '.entries[] | select(.tags | index("security")) | select(.status=="alive") | "\(.id)\t\(.name)"' data/sources.json

# Benchmark sources in machine learning
jq -r '.entries[] | select(.kategori=="Benchmark & leaderboard") | select(.tags | index("ml")) | .name' data/sources.json

# Anything where an artifact was independently evaluated
jq -r '.entries[] | select(.kategori=="Artifact evaluation") | .name' data/sources.json
```

## Sources worth opening first

**When you want code that was reviewed as code.** Software journals put the implementation at the centre of the publication, so the repository link is on the article page by construction.

| Source | Why |
|---|---|
| [Journal of Open Source Software](https://joss.theoj.org/papers) | Software articles with DOIs and linked repositories |
| [Journal of Statistical Software](https://www.jstatsoft.org/) | Paper, package, and replication scripts on one page |
| [IPOL](https://www.ipol.im/) | Algorithm articles that must ship runnable code and a demo |
| [SciPost Physics Codebases](https://scipost.org/journals/SciPostPhysCodeb) | Each codebase gets its own DOI, separate from the article |

**When you need to trust the numbers.** Artifact evaluation means someone independent built and ran the thing, which is a stronger signal than a promising README.

| Source | Why |
|---|---|
| [DARTS](https://drops.dagstuhl.de/entities/journal/DARTS) | Reviewed artifacts published as first-class objects, with DOIs |
| [Security Research Artifacts](https://secartifacts.github.io/) | Cross-conference index of security artifacts |
| [SIGMOD Reproducibility](https://reproducibility.sigmod.org/) | Database papers with experiment scripts and reproduction reports |
| [ReScience C](https://rescience.github.io/read/) | Published replications, including the ones that failed |

**When you have a paper title and want the repository in one move.**

| Source | Why |
|---|---|
| [CatalyzeX](https://www.catalyzex.com/) | Paste a title, get a code link |
| [Linked Papers With Code](https://linkedpaperswithcode.com/) | Historical paper to repository relations |
| [Papers With Code data archive](https://github.com/paperswithcode/paperswithcode-data) | The site died in July 2025, the dump did not, and it queries in bulk |
| [Code Ocean Capsules](https://codeocean.com/explore/capsules/) | Code plus the environment that runs it |

**When the data is the hard part.**

| Source | Why |
|---|---|
| [Harvard Dataverse](https://dataverse.harvard.edu/) | Datasets with DOIs, citable as research output |
| [Zenodo](https://zenodo.org/) | Filter to Software for citable code releases |
| [PANGAEA](https://www.pangaea.de/) | Earth and environmental data with strong metadata |
| [CERN Open Data](https://opendata.cern.ch/) | Physics data with worked analysis examples |

**When you want to search a thousand papers instead of five.**

| Source | Why |
|---|---|
| [OpenAlex](https://openalex.org/) | Full bibliographic API, cross-disciplinary |
| [SemRepo](https://semrepo.org/) | SPARQL over a graph of research repositories |
| [DataCite Commons](https://commons.datacite.org/) | Resolves the DOI links between papers, software, and data |
| [re3data](https://www.re3data.org/) | Find repositories you did not know existed |

**When you want to see an algorithm rather than read it.** These archives keep the implementations that predate GitHub.

| Source | Why |
|---|---|
| [ACM Collected Algorithms](https://www.netlib.org/toms/) | Numerical algorithms tied to ACM TOMS articles |
| [ModelDB](https://modeldb.science/) | Neuron and network models behind published papers |
| [ASCL](https://ascl.net/) | Astronomy code cited directly in the literature |
| [CoMSES](https://www.comses.net/codebases/) | Agent-based models, peer reviewed |

## Audit status

<!-- AUDIT-TABLE-START -->
**Last audit: 2026-10-12.** All 200 URLs probed by [`scripts/audit_links.py`](scripts/audit_links.py), 15s timeout, 24 workers.

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

Five categories came back completely green, which is worth noting because they are the ones you can lean on without checking first: Artifact evaluation, Package index, Curated list, Workflow registry, and Lab & organization repository.

**Status legend**, worth reading before you conclude something is broken:

- `alive`: reachable, serves content, same host as listed.
- `redirected`: reachable but on a different host. The listed URL is stale. Real example: `paperswithcode.com` to `huggingface.co`.
- `bot_walled`: refuses automated clients, whether by 401/403 or a challenge page. **Not dead.** Almost always fine in a normal browser, and should not be reported as a broken link.
- `rate_limited`: HTTP 429, temporarily throttling. Check again later.
- `dead`: HTTP 404 or 410, the resource is gone.
- `error` / `timeout`: transport failure: DNS, TLS, refused connection, or no answer in time.

## Why this is not just another link list

Three things, and they matter more than the count.

**It is sorted by what you are trying to do.** The original compilation grouped sources into alphabetical sections A through T, which served whoever assembled it rather than the reader. Here every entry carries one of sixteen categories and one of five workflow stages, so a concrete question ("where is the code for this paper?") points at one slice instead of the whole list. The original group letter survives on each entry as a provenance trace, because rearranging someone else's list should be visible, not hidden.

**The links were actually checked.** A script probes all 200 and classifies every one, the results carry a date, and a GitHub Action repeats the run every Monday so the directory does not quietly rot. "These links work" is not a promise here, it is a build artifact you can reproduce.

**The content is data, not prose.** Everything on this page exists in `data/sources.json` in a form you can filter, join, or feed to a tool. The markdown is a rendering of the data, not a separate copy of it, so the two cannot drift apart.

## Contents

- [Full directory: 200 sources](DIRECTORY.md), grouped by kind of source
- [CHECKLIST.md](CHECKLIST.md), 16-point test for judging a research repository
- [QUERIES.md](QUERIES.md), 20 ready-to-paste search queries
- [CONTRIBUTING.md](CONTRIBUTING.md), how to add or fix an entry
- [audit/liveness.md](audit/liveness.md), per-link audit output
- [data/sources.json](data/sources.json) and [data/sources.csv](data/sources.csv), the data itself

Loading it from code:

```python
import json, urllib.request
src = json.load(urllib.request.urlopen(
    "https://raw.githubusercontent.com/rayss868/paper-code-datasets/main/data/sources.json"))
for e in src["entries"]:
    if "artifact" in e["kategori"].lower() and e["status"] == "alive":
        print(e["id"], e["name"], e["url"])
```

## The six-step workflow

[CHECKLIST.md](CHECKLIST.md) and [QUERIES.md](QUERIES.md) expand each step.

1. **Start from one paper** with a DOI or arXiv ID. Write down the exact title, the authors, the year, the DOI, what kind of experiment it reports, and which datasets it used.
2. **Find an implementation you can audit.** In order: the paper's own code availability statement, then the authors' or lab's site, then a lookup service, then code hosting, then artifact indexes. Confirm that the README, the paper title, the DOI, and the author identity actually match.
3. **Look for a full reproduction package**, not just a repository. An artifact badge, a DARTS entry, a Code Ocean capsule, or a software journal article is worth more than a promising README. See [CHECKLIST.md](CHECKLIST.md).
4. **Compare the artifact against the paper.** Dataset completeness, preprocessing, the train/validation/test split, random seeds, dependency versions, hyperparameters, hardware, metrics, and whether the scripts can regenerate the paper's tables and figures.
5. **Run the baseline before changing anything.** Use the release or commit that matches the paper. Keep the logs, the environment lockfile, the actual numbers, and the gap between them and the published ones.
6. **Only then modify.** Document what you changed, run ablations, test significance, and cite the paper, the code, and the dataset as three separate objects if all three have identifiers.

## Contributing

New sources, corrected URLs, and fixed classifications are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first, because the format is strict on purpose: the data files are meant to be processed by machines, not only read.

If you add a source, set its `kategori` from the fixed list and give it at least one tag. A source with no category is a source nobody will find again.

## What is verified, and what is not

Being precise about this is the difference between a useful directory and a plausible-looking one.

**Verified:**

- The structure of the list: 200 numbered entries in sequence, 199 unique URLs, and exactly one duplicate, where entries 48 and 133 point at the same GitHub topic. The duplicate is kept and labelled rather than quietly removed, since it is evidence of how the list was assembled.
- Host concentration: 200 entries spread over 149 distinct hosts, with `github.com` holding 46 of them, or 23%. Many of those are topic and tag pages rather than independent sources, so the honest count of distinct providers sits well below 200.
- Link liveness, as of the date in the audit table above.
- Categories and tags, assigned mechanically from the entry text so the set can be regenerated rather than argued about.

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
