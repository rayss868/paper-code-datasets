# Search queries you can paste

Replace `PAPER TITLE`, `ALGORITHM`, `TOPIC`, and `DOI` with your own.

```
1.  "PAPER TITLE" github
2.  "PAPER TITLE" "code availability"
3.  "PAPER TITLE" "replication package"
4.  "PAPER TITLE" source code dataset
5.  "ALGORITHM" "official implementation"
6.  "ALGORITHM" reproduce experiment
7.  site:github.com "PAPER TITLE" "train.py"
8.  site:zenodo.org "PAPER TITLE" software
9.  site:osf.io "PAPER TITLE" code
10. site:github.com "DOI" "README"
11. site:papers.miccai.org "SEGMENTATION" code
12. site:secartifacts.github.io "intrusion detection"
13. site:drops.dagstuhl.de "artifact" "compiler"
14. site:jstatsoft.org "algorithm" "Python"
15. site:github.com "cybersecurity" "paper" "code"
16. site:github.com "intrusion detection" dataset preprocessing
17. site:github.com "benchmark" "reproduce results"
18. site:openreview.net "TOPIC" "code"
19. site:proceedings.mlr.press "TOPIC" supplementary
20. "PAPER TITLE" (github OR gitlab OR zenodo)
```

## Modifiers that narrow things down

| Modifier | What it does |
|---|---|
| `filetype:pdf` | Jumps straight to documents |
| `site:github.com` | Confines the search to GitHub |
| `-survey` | Drops survey papers, which you rarely want when hunting code |
| `"replication package"` | Finds explicit replication bundles |
| `"code available at"` | The phrasing availability statements tend to use |
| `after:2023` | Limits by publication year |

## When to skip search engines entirely

For bulk work, query the metadata endpoints instead. They are faster, they rate-limit in a knowable way, and they return structured results. See stage **05 · For agents and automation** in the README.

```bash
# OpenAlex: paper metadata
curl -s "https://api.openalex.org/works?search=PAPER%20TITLE&per-page=5"

# DataCite: software registered with a DOI
curl -s "https://api.datacite.org/dois?query=PAPER%20TITLE&resource-type-id=software"

# Papers With Code archive, after cloning it locally
jq -r '.[] | select(.title | test("TITLE"; "i"))' paperswithcode-data/links.json
```
