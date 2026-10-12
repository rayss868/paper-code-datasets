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
  "stage": "02-find-code",
  "jenis": "Software journal",
  "bidang": "Machine learning",
  "yang_dicari": "The concrete thing you can find there.",
  "cara_pakai": "The practical steps for using it.",
  "catatan": "The limitation you should not ignore.",
  "section": "A"
}
```

Field rules:

- **`stage`** picks the workflow step, based on the question the source answers rather than the field it belongs to. One of `01-discover`, `02-find-code`, `03-datasets`, `04-reproduce`, `05-agents`.
- **`jenis`** is a short category. Copy the style of neighboring entries.
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

## What gets rejected

- **Links you have not opened.** Check first. If the site blocks scripts, say in the pull request that you verified it in a browser.
- **Entries with an empty `catatan`.** Every source has a limit. Write it.
- **Unsourced numbers.** If you cite a figure, say where it came from, or mark it clearly as unverified.
- **Duplicates.** Search `sources.json` for the URL before adding it.
- **Hand-edits to `DIRECTORY.md` or `audit/liveness.md`.** Both are generated.

## Pull request format

```
Add: [source name]
Stage: [01-discover | 02-find-code | 03-datasets | 04-reproduce | 05-agents]
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
