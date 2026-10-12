# Paper → Code → Dataset → Reproduksi

**Direktori 200 sumber terverifikasi untuk menemukan implementasi kode, dataset,
dan paket reproduksi dari paper ilmiah.**

Bukan daftar link biasa. Setiap sumber dikelompokkan menurut **tahap alur kerja
penulisan paper**, diverifikasi statusnya lewat audit otomatis, dan tersedia
dalam format terstruktur (JSON/CSV) supaya bisa dipakai manusia maupun agent.

```
Cari paper  →  Cari kode  →  Cari dataset  →  Reproduksi  →  Sitasi
   01             02             03              04            05
```

---

## Kenapa repo ini beda

Tiga hal yang membedakan dari ratusan daftar "awesome" lainnya:

1. **Diurutkan menurut alur kerja, bukan abjad.** Kalau kamu punya satu
   pertanyaan konkret ("cara cari kode dari paper ini gimana?"), kamu langsung
   tahu harus ke bagian mana.
2. **Status setiap tautan dicek, bukan diklaim.** [`scripts/audit_links.py`](scripts/audit_links.py)
   menjalankan probe HTTP ke seluruh 200 URL dan menandai hasilnya
   `alive` / `redirected` / `bot_walled` / `dead`. Siapa pun bisa menjalankannya
   ulang dan mendapat klasifikasi yang sama.
3. **Tersedia sebagai data.** [`data/sources.json`](data/sources.json) dan
   [`data/sources.csv`](data/sources.csv) bisa di-import ke alat lain, dipakai
   untuk membangun pencarian sendiri, atau dijadikan basis agent.

---

## Status audit

<!-- AUDIT-TABLE-START -->
**Audit terakhir: 2026-10-12** — 200 URL diprobe otomatis
(`scripts/audit_links.py`, timeout 15s).

| Status | Jumlah | Arti |
|---|---:|---|
| `alive` | 171 | Aktif dan menyajikan konten |
| `redirected` | 3 | Pindah host — URL di daftar sudah usang |
| `bot_walled` | 17 | Menolak klien otomatis — **normal di browser** |
| `rate_limited` | 6 | HTTP 429 saat audit — coba lagi nanti |
| `timeout` | 3 | Tidak terjangkau dari host audit |
| `dead` | 0 | — |
| `error` | 0 | — |

Temuan yang perlu diketahui:

- **25 sumber (`bot_walled` + `rate_limited` + `timeout`) tidak gagal.**
  `bot_walled` hampir selalu berarti situs normal di browser (Cloudflare dsb.);
  `timeout` sering karena host audit diblokir, bukan tautannya mati. Contoh:
  *Journal of Open Research Software* timeout dari sini, tetapi jelas aktif
  (artikel terbit Sep 2026).
- **4 tautan dikoreksi** hasil audit — lihat field `correction` di
  `data/sources.json` (Bioconductor 404 → path baru; CSDMS 404 → halaman resmi;
  Wizwand rebranding ke sota2.com; MICCAI OA pindah halaman).
- **`paperswithcode.com` → `huggingface.co/papers/trending`** terkonfirmasi:
  situsnya memang dihentikan Juli 2025. Pakai arsip datanya (entri 138).

Rincian per tautan: [`audit/liveness.md`](audit/liveness.md).
<!-- AUDIT-TABLE-END -->

**Legenda status** — ini penting sebelum menyimpulkan sesuatu rusak:

- `alive` — aktif, konten tersaji, host sama seperti yang terdaftar.
- `redirected` — bisa diakses tapi mengarah ke host lain. URL di daftar sudah
  usang, situsnya pindah. Contoh nyata: `paperswithcode.com` → `huggingface.co`.
- `bot_walled` — menolak klien otomatis (401/403 atau halaman challenge
  Cloudflare). **Bukan berarti mati** — hampir selalu normal saat dibuka di
  browser biasa. Jangan laporkan sebagai tautan rusak.
- `rate_limited` — HTTP 429, sementara membatasi. Cek ulang nanti.
- `dead` — HTTP 404/410, sumbernya sudah hilang.
- `error` / `timeout` — gagal transport (DNS, TLS, koneksi di-refuse).

---

## Daftar isi

- [01 · Cari Paper](#01--cari-paper-31-sumber) — 31 sumber
- [02 · Cari Source Code](#02--cari-source-code-100-sumber) — 100 sumber
- [03 · Cari Dataset](#03--cari-dataset-17-sumber) — 17 sumber
- [04 · Reproduksi Eksperimen](#04--reproduksi-eksperimen-43-sumber) — 43 sumber
- [06 · Untuk AI Agent & Otomasi](#06--untuk-ai-agent--otomasi-9-sumber) — 9 sumber
- [Pilih dari mana — 10 pintu masuk terbaik](#pilih-dari-mana--10-pintu-masuk-terbaik)
- [Alur 6 langkah](#alur-6-langkah-menulis-paper-dengan-kode)
- [Berkas pendukung](#berkas-pendukung)
- [Cara berkontribusi](#cara-berkontribusi)
- [Disclaimer & keterbatasan](#disclaimer--keterbatasan)

**Detail lengkap 200 entri** — setiap entri dengan `Jenis`, `Bidang`,
`Yang dicari`, `Cara pakai`, dan `Catatan` — ada di **[DIRECTORY.md](DIRECTORY.md)**.

---

## 01 · Cari Paper (31 sumber)

Preprint, prosiding, mesin pencari, peta literatur.

| Kategori | Sumber |
|---|---|
| Preprint & prosiding | arXiv, OpenReview, PMLR, NeurIPS Proceedings, CVF Open Access, ACL Anthology, USENIX Security, NDSS Symposium, MICCAI Open Access |
| Mesin pencari | Semantic Scholar, Google Scholar, OpenAIRE Explore, CORE, INSPIRE-HEP |
| Peta literatur | Connected Papers, ResearchRabbit |
| Biomedis | PubMed Central, Europe PMC, PLOS Comp Biol (Code Availability), Nature Scientific Data |
| Penerbit | IEEE Xplore, ACM Digital Library, F1000Research |
| Katalog lab | Ai2 Research Papers, Google Research Publications, Hugging Face Papers |

## 02 · Cari Source Code (100 sumber)

Jurnal software, indeks kode, hub kode, kurasi komunitas.

| Kategori | Sumber |
|---|---|
| Jurnal software (kode = bagian publikasi) | JOSS, JMLR MLOSS, Journal of Statistical Software, The R Journal, SoftwareX, Journal of Open Research Software, SciPost Physics Codebases, IPOL, JOSE |
| Paper-to-code search | **CatalyzeX**, **Code Ocean Capsules**, Papers With Code Data Archive |
| Hub kode & model | GitHub Code Search, GitLab, Codeberg, Hugging Face Models/Spaces, PyPI, CRAN, Bioconductor, R-universe, Zenodo |
| Implementasi resmi lab | Google Research, Google DeepMind, Meta Research, TensorFlow Model Garden, PyTorch Examples, timm, Detectron2, MMDetection, OpenMMLab, fairseq, OpenNMT |
| Arsip algoritma & model | CALGO/Netlib, ModelDB, BioModels, CoMSES, Physiome, NetLogo, ACM |
| Registry per bidang | bio.tools, SciCrunch, ASCL (astronomi), PhysioNet, NITRC (neuroimaging), Galaxy Tool Shed, Materials Project |
| Kurasi komunitas GitHub | 10× direktori "Awesome" & "…-Papers-with-Code" (CVPR, MICCAI, cybersecurity) |

## 03 · Cari Dataset (17 sumber)

| Kategori | Sumber |
|---|---|
| Repositori umum + DOI | **Harvard Dataverse**, Zenodo, Figshare, Dryad, Mendeley Data, OSF, UCI ML Repository |
| Dataverse regional | DataverseNO, Borealis (Kanada), 4TU.ResearchData |
| Bidang khusus | PANGAEA (bumi), CERN Open Data (fisika), HEPData (HEP), GigaDB (bioinformatika), Materials Cloud (material), NOMAD (material) |
| Hub dataset | Hugging Face Datasets, OpenML |
| Arsip studi | EMBL-EBI BioStudies |

## 04 · Reproduksi Eksperimen (43 sumber)

Artifact evaluation, benchmark, paket replikasi, model zoo.

| Kategori | Sumber |
|---|---|
| Artifact evaluation konferensi | Security Research Artifacts, SIGMOD Reproducibility, ICSE/ISSTA/POPL/PLDI/ICFP/EuroSys/CCS/ISCA 2026 |
| Jurnal artefak | **DARTS** (Dagstuhl — artefak dievaluasi, bukan sekadar diunggah) |
| Paket replikasi | ReScience C, Renku, Whole Tale, Code Ocean, WorkflowHub, Dockstore, nf-core |
| Benchmark & leaderboard | MLCommons/MLPerf, Codabench, AIcrowd, EvalAI, Grand Challenge, DrivenData, Kaggle, OGB, DataPerf, NAB, TimeEval, Monash Forecasting |
| Model zoo | MONAI, BioImage, MMDetection |
| Evaluasi LLM | EleutherAI LM Evaluation Harness |
| Grafis | GRSI, Graphics Replicability Database |
| Discovery pengganti PWC | HyperAI, CodeSOTA, Wizwand, NLP Progress, Time Series Classification |

## 06 · Untuk AI Agent & Otomasi (9 sumber)

Endpoint API dan metadata terstruktur — bagian yang hampir tidak ada di repo sejenis.

| Sumber | Kegunaan |
|---|---|
| **OpenAlex** | API metadata paper lintas disiplin |
| **SemRepo** | Knowledge graph 190k+ repository riset (RDF/SPARQL) |
| **Linked Papers With Code** | Graf relasi paper ↔ metode ↔ dataset ↔ kode |
| **DataCite Commons** | Relasi DOI antara paper, dataset, dan software |
| **re3data** | Direktori repositori ilmiah (untuk menemukan sumber baru) |
| **FAIRsharing** | Registry standar & database riset |
| zbMATH/swMATH | Software matematika ↔ literatur |
| DataLad Registry | Dataset berversi + provenance |
| DGL Examples | Koleksi implementasi paper GNN |

---

## Pilih dari mana — 10 pintu masuk terbaik

Kalau bingung mulai dari mana:

| # | Sumber | Kenapa |
|---|---|---|
| 1 | [**CatalyzeX**](https://www.catalyzex.com/) | Tempel judul paper → langsung dapat link kode. Paling cepat. |
| 2 | [**Papers With Code Data Archive**](https://github.com/paperswithcode/paperswithcode-data) | Situs aslinya mati Juli 2025, tapi dump datanya masih hidup dan bisa di-query massal. |
| 3 | [**JOSS**](https://joss.theoj.org/papers) | Paper tentang software — kode adalah subjek publikasinya. |
| 4 | [**Journal of Statistical Software**](https://www.jstatsoft.org/) | Paper + paket + skrip replikasi, satu halaman. |
| 5 | [**Zenodo**](https://zenodo.org/) | Repositori DOI; filter `Software` untuk paket yang bisa dikutip. |
| 6 | [**Code Ocean**](https://codeocean.com/explore/capsules/) | Bukan cuma kode — lingkungan eksekusinya sekalian. |
| 7 | [**Cari Paper**](https://arxiv.org/) + [**Security Research Artifacts**](https://secartifacts.github.io/) | Untuk cybersecurity: banyak paper keamanan wajib rilis artefak. |
| 8 | [**DARTS**](https://drops.dagstuhl.de/entities/journal/DARTS) | Artefak yang sudah **dievaluasi**, bukan sekadar diunggah. |
| 9 | [**OpenAlex**](https://openalex.org/) | Kalau kamu mau otomasi, bukan klik manual. |
| 10 | [**SemRepo**](https://semrepo.org/) | Query SPARQL ke graf repository riset. |

---

## Alur 6 langkah: menulis paper dengan kode

1. **Mulai dari satu paper** yang punya DOI/arXiv ID. Catat: judul persis,
   penulis, tahun, DOI, jenis eksperimen, dataset.
2. **Cari implementasi** yang bisa diaudit. Urutan prioritas: bagian *Code
   Availability* di paper → situs lab/penulis → CatalyzeX/Hugging Face →
   GitHub/GitLab/Zenodo/Code Ocean → indeks artefak. Cocokkan README, nama
   paper, DOI, identitas penulis.
3. **Cari paket reproduksi lengkap.** Prioritas: artifact badge resmi, DARTS,
   ReScience C, Code Ocean, SoftwareX/JOSS/JMLR MLOSS, supplementary jurnal,
   Zenodo. → lihat [CHECKLIST.md](CHECKLIST.md)
4. **Verifikasi artefak terhadap paper.** Cek kelengkapan dataset,
   preprocessing, split train/val/test, seed, versi dependensi, hiperparameter,
   hardware, metrik, dan perintah untuk menghasilkan tabel/gambar paper.
5. **Jalankan baseline sebelum modifikasi.** Pakai commit/rilis yang sesuai.
   Simpan log, hash, lockfile environment, hasil aktual, dan selisihnya
   terhadap paper asli.
6. **Baru kembangkan.** Dokumentasikan modifikasi, ablation, uji statistik, dan
   perbandingan yang adil. Sitasi paper, kode, dan dataset sebagai tiga objek
   terpisah.

Query pencarian siap copy: **[QUERIES.md](QUERIES.md)** (20 query).

---

## Berkas pendukung

| Berkas | Isi |
|---|---|
| [`DIRECTORY.md`](DIRECTORY.md) | 200 entri lengkap, dikelompokkan per tahap alur kerja |
| [`data/sources.json`](data/sources.json) | Data terstruktur + status audit |
| [`data/sources.csv`](data/sources.csv) | Versi spreadsheet |
| [`audit/liveness.md`](audit/liveness.md) | Hasil audit per tautan terbaru |
| [`CHECKLIST.md`](CHECKLIST.md) | Checklist 16 poin untuk menilai repo penelitian |
| [`QUERIES.md`](QUERIES.md) | 20 query pencarian siap pakai |
| [`scripts/audit_links.py`](scripts/audit_links.py) | Script audit liveness |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Cara menambah/memperbaiki sumber |

Pakai dari kode:

```python
import json, urllib.request
src = json.load(urllib.request.urlopen(
    "https://raw.githubusercontent.com/rayss868/paper-code-datasets/main/data/sources.json"))
cyber = [e for e in src["entries"]
         if "security" in e["bidang"].lower() and e["status"] == "alive"]
print(len(cyber), "sumber cybersecurity yang aktif")
```

---

## Cara berkontribusi

Sumber baru, koreksi tautan, atau perbaikan status sangat diterima.
Baca [CONTRIBUTING.md](CONTRIBUTING.md) — formatnya ketat supaya data tetap
bisa diproses mesin.

---

## Disclaimer & keterbatasan

Repo ini adalah **kompilasi dari percakapan riset**, bukan audit manual
satu-per-satu oleh penyusun asalnya. Yang **sudah** diverifikasi:

- Integritas struktur daftar: 200 entri bernomor berurutan, 199 URL unik,
  satu duplikat persis di entri 48 & 133 (dicatat, sengaja dipertahankan
  sebagai jejak daftar awal).
- Konsentrasi host: 149 host berbeda untuk 200 entri; `github.com` menampung
  46 entri (23%). **Banyak entri GitHub adalah topik/tag, bukan sumber
  independen** — perhitungkan itu saat menilai "jumlah sumber".
- Liveness: lihat tabel status audit di atas (dijalankan otomatis).

Yang **belum** diverifikasi dan perlu kehati-hatian:

- Klaim kuantitatif pada deskripsi entri tertentu (mis. statistik jumlah
  repository sebuah proyek) — perlakukan sebagai klaim penyusun asal, bukan
  fakta terverifikasi, sampai kamu cek sendiri ke sumbernya.
- Kualitas, lisensi, dan kelengkapan setiap repository yang ditemukan.
- Keaktifan pemeliharaan proyek (repo aktif vs terbengkalai).

**Peringatan penting:**

1. Tautan yang ada **tidak otomatis berarti kode paper tersedia**. Sebagian
   hanya indeks bibliografi, dataset, atau halaman program konferensi.
2. *"Official implementation"* harus dicocokkan dengan penulis/lab/paper.
3. *"Artifact available"* ≠ *"results reproduced"*.
4. Software ber-DOI bukan jaminan bebas bug atau berkualitas tinggi.
5. Rilis lama bisa butuh environment khusus — pakai container/VM terisolasi,
   dan **jangan jalankan skrip yang tidak kamu percaya**.
6. Untuk publikasi akademik, sitasi paper, kode, dan dataset sebagai tiga
   objek terpisah bila masing-masing punya DOI.
7. Sebagian besar katalog berubah; verifikasi tautan saat dipakai.

**Catatan sejarah:** Papers With Code (entri 140) dinonaktifkan Meta pada Juli
2025; domainnya kini mengarah ke Hugging Face Trending Papers. Data historisnya
masih tersedia lewat arsip (entri 138).

---

## Lisensi

Kompilasi ini dirilis dengan [CC0 1.0 Universal](LICENSE) — domain publik.
Data boleh dipakai, dimodifikasi, dan didistribusikan tanpa syarat.

Sumber pihak ketiga yang ditautkan tetap tunduk pada lisensi masing-masing;
repo ini tidak mengklaim hak atas konten tersebut.
