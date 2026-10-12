# Contributing

Thanks for wanting to add something or fix something. Because this repo is used as structured data and not only read as a page, the format is strict. Here is what that means in practice.

## Adding a source or fixing a URL

Edit [`data/sources.json`](data/sources.json). Do not edit `DIRECTORY.md` by hand, since it is generated from the JSON and your change will be overwritten.

Add an entry with the next unused `id`:

```json
{
  "id": 201,
  "name": "Source name",
  "url": "https://example.org/",
  "kategori": "Dataset repository",
  "stage": "03-datasets",
  "tags": ["ml", "dataset", "doi"],
  "jenis": "Data repository",
  "bidang": "Machine learning",
  "yang_dicari": "The concrete thing you can find there.",
  "cara_pakai": "The practical steps for using it.",
  "catatan": "The limitation you should not ignore.",
  "section": "A"
}
```

## `kategori` is a closed list

Pick exactly one, and pick the one that decides where a reader would look for this source. Do not invent new values: a source in a category of its own is a source nobody finds.

`Artifact evaluation` | `Benchmark & leaderboard` | `Code search & hosting` | `Curated list` | `Dataset repository` | `Lab & organization repository` | `Metadata & knowledge graph` | `Model & algorithm repository` | `Package index` | `Paper discovery` | `Paper-to-code lookup` | `Proceedings & publisher` | `Reproducibility platform` | `Software directory` | `Software journal` | `Workflow registry`

## `stage` is the workflow step

One of `01-discover`, `02-find-code`, `03-datasets`, `04-reproduce`, `05-agents`. Choose it by the question the source answers, not by the field it belongs to. A paper search engine is `01-discover` even when it is used by physicists.

## `tags` are facets

Two to six lowercase tags, drawn from these two families. Field tags say what discipline the source serves; affordance tags say what you can do with it.

Field: `ml`, `security`, `biomedical`, `materials`, `earth`, `physics`, `social`, `open science`

Affordance: `api`, `dataset`, `code`, `benchmark`, `doi`, `licence`

Add at least one field tag and at least one affordance tag where they honestly apply. Both are assigned mechanically from the entry text, so a tag that does not appear anywhere in your description will look out of place.

## The prose fields

- **`jenis`** is a short descriptive label for the kind of place it is. Free text here, unlike `kategori`, because it is for humans.
- **`bidang`** is the field that fits best, not a hard boundary.
- **`yang_dicari`** has to be concrete. "Lots of useful things" is not an answer.
- **`cara_pakai`** is a procedure, not a description.
- **`catatan`** is the honest limitation. Leave it empty and the entry will not be merged. Every source disappoints someone somewhere, so write down where.
- **`section`** keeps the original grouping letter (A through T) as a provenance trace.

The descriptive fields are in English. Keep them that way.

## Refreshing audit results

Run the auditor and send the diff:

```bash
python3 scripts/audit_links.py
git diff data/sources.json audit/liveness.md
```

## Checking your entry against the published filters

The README shows queries that readers actually use. Run one before opening a pull request, so you know your entry will show up where you expect it to:

```bash
jq -r '.entries[] | select(.kategori=="Artifact evaluation") | .name' data/sources.json
```

## What gets rejected

- **Links you have not opened.** Check first. If the site blocks scripts, say in the pull request that you verified it in a browser.
- **Entries with an empty `catatan`.** Every source has a limit. Write it.
- **A `kategori` outside the fixed list**, or a missing one.
- **No tags, or tags that contradict the description.**
- **Unsourced numbers.** If you cite a figure, say where it came from, or mark it clearly as unverified.
- **Duplicates.** Search `sources.json` for the URL before adding it.
- **Hand-edits to `DIRECTORY.md` or `audit/liveness.md`.** Both are generated.

## Pull request format

```
Add: [source name]
Category: [one of the 16 above]
Stage: [01-discover | 02-find-code | 03-datasets | 04-reproduce | 05-agents]
Tags: [field + affordance tags]
Opened in a browser: [yes/no]
Note: [why this source earns its place, or why a status looks the way it does]
```

## Running the audit locally

```bash
python3 scripts/audit_links.py --workers 24 --timeout 15
```

No dependencies beyond the Python 3.10 standard library.

One thing to internalize before using the output: `bot_walled` is information, not a verdict. A 403 from a script almost always means the site is fine for a person.

## Reporting a problem

Open an issue with the entry number and URL, what you saw against what you expected, and the date you checked. That is usually enough to fix it.
