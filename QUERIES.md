# Query pencarian siap pakai

Copy-paste ke mesin pencari. Ganti `JUDUL PAPER`, `NAMA ALGORITMA`, `TOPIK`,
dan `DOI` dengan milikmu.

## Alur dasar

```
1.  "JUDUL PAPER PERSIS" github
2.  "JUDUL PAPER PERSIS" "code availability"
3.  "JUDUL PAPER PERSIS" "replication package"
4.  "JUDUL PAPER PERSIS" source code dataset
5.  "NAMA ALGORITMA" "official implementation"
6.  "NAMA ALGORITMA" reproduce experiment
7.  site:github.com "JUDUL PAPER" "train.py"
8.  site:zenodo.org "JUDUL PAPER" software
9.  site:osf.io "JUDUL PAPER" code
10. site:github.com "DOI" "README"
11. site:papers.miccai.org "SEGMENTATION" code
12. site:secartifacts.github.io "intrusion detection"
13. site:drops.dagstuhl.de "artifact" "compiler"
14. site:jstatsoft.org "algorithm" "Python"
15. site:github.com "cybersecurity" "paper" "code"
16. site:github.com "intrusion detection" dataset preprocessing
17. site:github.com "benchmark" "reproduce results"
18. site:openreview.net "TOPIK" "code"
19. site:proceedings.mlr.press "TOPIK" supplementary
20. "JUDUL PAPER" (github OR gitlab OR zenodo)
```

## Modifier yang berguna

Tambahkan ke query mana pun untuk mempersempit:

| Modifier | Efek |
|---|---|
| `filetype:pdf` | Langsung ke dokumen |
| `site:github.com` | Batasi ke GitHub |
| `-survey` | Buang paper survei (kamu cari implementasi) |
| `"replication package"` | Paket replikasi eksplisit |
| `"code available at"` | Frasa khas bagian availability |
| `after:2023` | Batasi tahun terbit |

## Alternatif: lewat API

Daripada mesin pencari, untuk pencarian massal pakai sumber metadata
(lihat bagian **06 · Untuk AI Agent** di README):

```bash
# OpenAlex — cari paper, ambil DOI & metadata
curl -s "https://api.openalex.org/works?search=JUDUL%20PAPER&per-page=5"

# DataCite — cari software dengan DOI
curl -s "https://api.datacite.org/dois?query=JUDUL%20PAPER&resource-type-id=software"

# Papers With Code data archive (lokal, setelah clone)
jq -r '.[] | select(.title | test("JUDUL"; "i"))' paperswithcode-data/links.json
```
