---
audience: humans-and-agents
last_reviewed: 2026-10-12
---

# Direktori Lengkap — 200 Sumber

Disusun ulang menurut **tahap alur kerja penulisan paper**, bukan abjad.

Data mentah: [`data/sources.json`](../data/sources.json) · [`data/sources.csv`](../data/sources.csv)
Status tautan: [`audit/liveness.md`](../audit/liveness.md)

> Setiap entri menyertakan `Jenis`, `Bidang`, `Yang dicari`, `Cara pakai`, dan `Catatan` (batasan).

## Daftar isi

- [Cari Paper](#01-discover) — 31 sumber
- [Cari Source Code](#02-find-code) — 100 sumber
- [Cari Dataset](#03-datasets) — 17 sumber
- [Reproduksi Eksperimen](#04-reproduce) — 43 sumber
- [Untuk AI Agent & Otomasi](#06-agents) — 9 sumber


<a id="01-discover"></a>
## Cari Paper — 31 sumber

Menemukan publikasi: preprint, prosiding, mesin pencari paper, peta literatur.

### A. Platform Khusus Research Code Dan Reproduksibilitas

#### [005] OpenAIRE Explore
- **URL:** https://explore.openaire.eu/
- **Jenis:** Discovery ilmiah
- **Bidang:** Lintas disiplin
- **Yang dicari:** Metadata publikasi, data, software, dan koneksi di antaranya.
- **Cara pakai:** Temukan publikasi; gunakan relasi research output untuk menemukan software atau dataset.
- **Catatan:** Tidak semua tautan metadata menunjuk kode yang bisa diunduh.

#### [011] MICCAI Open Access
- **URL:** https://papers.miccai.org/
- **Jenis:** Prosiding
- **Bidang:** Medical imaging AI
- **Yang dicari:** Paper konferensi serta link kode atau data jika penulis membagikannya.
- **Cara pakai:** Cari judul atau tahun MICCAI; periksa bagian resource, supplementary, GitHub.
- **Catatan:** Setiap artikel berbeda dalam ketersediaan kode.
- **Koreksi:** 2026-10-12: papers.miccai.org mengalihkan ke miccai.org/publications/miccai-open-access-reviews/. Halaman tujuan valid.

### C. Mesin Pencari Paper Yang Dapat Ditelusuri Ke Kode

#### [027] arXiv
- **URL:** https://arxiv.org/
- **Jenis:** Preprint
- **Bidang:** CS, ML, matematika, fisika
- **Yang dicari:** Manuskrip dan link GitHub/project yang dicantumkan penulis.
- **Cara pakai:** Cari judul paper; periksa abstrak, laman HTML, PDF, dan appendix.
- **Catatan:** Preprint belum tentu menjalani peer review; kode opsional.

#### [028] alphaXiv
- **URL:** https://www.alphaxiv.org/
- **Jenis:** Penjelajah paper
- **Bidang:** AI dan arXiv
- **Yang dicari:** Paper arXiv, diskusi dan fitur eksplorasi penelitian.
- **Cara pakai:** Cari ID arXiv; cek project links dan diskusi replikasi.
- **Catatan:** Ketersediaan fungsi dan tautan dapat berubah.

#### [029] Cool Papers
- **URL:** https://papers.cool/
- **Jenis:** Kurasi paper
- **Bidang:** AI dan ML
- **Yang dicari:** Jelajah paper populer dan topik AI.
- **Cara pakai:** Gunakan topik/konferensi untuk shortlist paper, lalu telusuri repo di situs penulis.
- **Catatan:** Platform discovery; bukan jaminan repository lengkap.

#### [030] OpenReview
- **URL:** https://openreview.net/
- **Jenis:** Review konferensi
- **Bidang:** ML dan AI
- **Yang dicari:** Submission, komentar review, lampiran, dan link kode bila ada.
- **Cara pakai:** Cari judul/venue; buka PDF, supplementary dan author response.
- **Catatan:** Kode bisa baru dibuka setelah acceptance atau tidak tersedia.

#### [031] CVF Open Access
- **URL:** https://openaccess.thecvf.com/
- **Jenis:** Prosiding
- **Bidang:** Computer vision
- **Yang dicari:** Paper CVPR/ICCV/WACV dan supplementary materials.
- **Cara pakai:** Cari tahun dan judul; telusuri project page, PDF, GitHub.
- **Catatan:** Tidak setiap paper menyertakan implementation release.

#### [032] ACL Anthology
- **URL:** https://aclanthology.org/
- **Jenis:** Prosiding
- **Bidang:** NLP
- **Yang dicari:** Artikel ACL, EMNLP dan konferensi bahasa lain.
- **Cara pakai:** Cari paper; periksa bagian Code/Data Availability dan situs proyek.
- **Catatan:** Lampiran publikasi bukan selalu source code.

#### [033] PMLR
- **URL:** https://proceedings.mlr.press/
- **Jenis:** Prosiding
- **Bidang:** Machine learning
- **Yang dicari:** Proceedings paper dan supplemental material jika disediakan.
- **Cara pakai:** Cari metode atau konferensi; ikuti author links dan appendix.
- **Catatan:** Kode sangat tergantung kebijakan paper/venue.

#### [034] NeurIPS Proceedings
- **URL:** https://proceedings.neurips.cc/
- **Jenis:** Prosiding
- **Bidang:** AI, deep learning
- **Yang dicari:** Paper NeurIPS dan materi supplementary.
- **Cara pakai:** Cari paper; buka supplementary dan tautan proyek/code.
- **Catatan:** Tidak semua submission merilis kode publik.

#### [035] USENIX Security
- **URL:** https://www.usenix.org/conferences/byname/108
- **Jenis:** Prosiding keamanan
- **Bidang:** Cybersecurity
- **Yang dicari:** Paper, appendix, dan artefak pada penelitian tertentu.
- **Cara pakai:** Cari topik/venue per tahun, lalu lihat artifact badge atau GitHub.
- **Catatan:** Sebagian artefak dibatasi karena keamanan, privasi, atau lisensi.

#### [036] NDSS Symposium
- **URL:** https://www.ndss-symposium.org/
- **Jenis:** Prosiding keamanan
- **Bidang:** Network dan system security
- **Yang dicari:** Paper dan referensi project/code dari penulis.
- **Cara pakai:** Telusuri tahun konferensi; buka paper dan artefak yang disebutkan.
- **Catatan:** Kode tidak dijamin tersedia untuk setiap paper.

#### [037] Semantic Scholar
- **URL:** https://www.semanticscholar.org/
- **Jenis:** Mesin paper
- **Bidang:** Lintas disiplin
- **Yang dicari:** Metadata, sitasi, versi paper dan tautan eksternal.
- **Cara pakai:** Cari judul tepat atau DOI; lanjut ke halaman penulis dan code availability.
- **Catatan:** Bukan hosting source code utama.

#### [038] Google Scholar
- **URL:** https://scholar.google.com/
- **Jenis:** Mesin paper
- **Bidang:** Lintas disiplin
- **Yang dicari:** Sitasi, versi PDF, dan halaman publikasi.
- **Cara pakai:** Cari judul + "github" atau + "supplementary code".
- **Catatan:** Hasil perlu diverifikasi; tidak semua tautan gratis/valid.

#### [039] Connected Papers
- **URL:** https://www.connectedpapers.com/
- **Jenis:** Peta literatur
- **Bidang:** Lintas disiplin
- **Yang dicari:** Graf jaringan paper yang berhubungan.
- **Cara pakai:** Masukkan DOI paper acuan; temukan metode pendahulu/penerus lalu cek masing-masing kode.
- **Catatan:** Tujuannya memetakan literatur, bukan mengunduh kode.

#### [040] ResearchRabbit
- **URL:** https://www.researchrabbit.ai/
- **Jenis:** Peta literatur
- **Bidang:** Lintas disiplin
- **Yang dicari:** Koleksi paper dan hubungan sitasi untuk eksplorasi topik.
- **Cara pakai:** Buat koleksi paper relevan lalu telusuri project sites/GitHub.
- **Catatan:** Biasanya kode perlu ditemukan di luar platform.

#### [041] PubMed Central
- **URL:** https://pmc.ncbi.nlm.nih.gov/
- **Jenis:** Arsip full text
- **Bidang:** Biomedis
- **Yang dicari:** Artikel ilmiah full text dan supplementary files.
- **Cara pakai:** Cari metode lalu find "Code availability" atau "Data and code".
- **Catatan:** Ketersediaan source code per artikel.

#### [042] Europe PMC
- **URL:** https://europepmc.org/
- **Jenis:** Arsip paper
- **Bidang:** Biomedis
- **Yang dicari:** Publikasi, metadata dan supplementary material.
- **Cara pakai:** Cari judul dan DOI; telusuri software/data links dan availability statements.
- **Catatan:** Tidak semuanya memiliki repository source.

#### [044] CORE
- **URL:** https://core.ac.uk/
- **Jenis:** Agregator open access
- **Bidang:** Lintas disiplin
- **Yang dicari:** Naskah akses terbuka dari repositori institusional.
- **Cara pakai:** Cari paper; telaah bagian Availability dan materi tambahan.
- **Catatan:** Open access paper tidak berarti open-source code.

#### [045] IEEE Xplore
- **URL:** https://ieeexplore.ieee.org/
- **Jenis:** Penerbit/prosiding
- **Bidang:** Teknik, cybersecurity, AI
- **Yang dicari:** Artikel teknis, DOI dan supplementary jika tersedia.
- **Cara pakai:** Cari paper; lihat supplemental material serta project website penulis.
- **Catatan:** Banyak konten memerlukan langganan institusi.

#### [046] ACM Digital Library
- **URL:** https://dl.acm.org/
- **Jenis:** Penerbit/prosiding
- **Bidang:** Computer science
- **Yang dicari:** Paper, artifact badge, supplementary files, dan DOI.
- **Cara pakai:** Cari paper dan tanda Artifacts Available/Evaluated/Results Reproduced.
- **Catatan:** Akses paper atau materi bisa dibatasi.

### H. Portal Paper, Data, Notebook Dan Software

#### [092] F1000Research
- **URL:** https://f1000research.com/
- **Jenis:** Jurnal open research
- **Bidang:** Lintas disiplin
- **Yang dicari:** Artikel Software Tool disertai informasi ketersediaan kode.
- **Cara pakai:** Cari tipe artikel Software Tool; ikuti source code availability.
- **Catatan:** Perhatikan tahapan peer review tiap artikel.

### J. Darts, Jurnal Software Dan Kurasi Kode Tambahan

#### [108] SciPy Proceedings
- **URL:** https://proceedings.scipy.org/
- **Jenis:** Prosiding
- **Bidang:** Scientific Python
- **Yang dicari:** Paper ekosistem SciPy, paket dan notebook.
- **Cara pakai:** Cari topik Python; ikuti repo software serta notebook artikel.
- **Catatan:** Paper dan implementasi bisa tersebar di beberapa repo.

#### [109] SciPy Proceedings Source
- **URL:** https://github.com/scipy-conference/scipy_proceedings
- **Jenis:** Repository prosiding
- **Bidang:** Scientific Python
- **Yang dicari:** Sumber penerbitan prosiding, paper assets dan proses review.
- **Cara pakai:** Gunakan pencarian nama artikel; cocokkan source dan eksternal repo penulis.
- **Catatan:** Utamanya sumber prosiding, bukan katalog kode aplikasi.

#### [110] Papers We Love
- **URL:** https://github.com/papers-we-love/papers-we-love
- **Jenis:** Kurasi paper
- **Bidang:** Computer science
- **Yang dicari:** Paper klasik/modern untuk belajar ide algoritma.
- **Cara pakai:** Pilih topik, baca paper lalu cari implementasinya terpisah.
- **Catatan:** Bukan repositori kode paper secara langsung.

### M. Repository Resmi Lab Ai

#### [128] Ai2 Research Papers
- **URL:** https://allenai.org/papers
- **Jenis:** Katalog lab
- **Bidang:** NLP, AI dan agents
- **Yang dicari:** Publikasi Ai2 dan tautan proyek/code jika tersedia.
- **Cara pakai:** Cari paper/model; periksa links pada halaman publikasi.
- **Catatan:** Halaman publikasi dapat mengarah ke repo eksternal.

#### [129] Google Research Publications
- **URL:** https://research.google/pubs/
- **Jenis:** Katalog publikasi
- **Bidang:** AI dan sains komputasi
- **Yang dicari:** Artikel riset Google untuk dicocokkan dengan repository.
- **Cara pakai:** Cari judul, lalu cocokkan dengan repo google-research/DeepMind.
- **Catatan:** Bukan hosting source code secara langsung.

### N. Sumber Dari Awal Percakapan Yang Belum Tercantum Dan Penanda Duplikat

#### [132] Hugging Face Papers
- **URL:** https://huggingface.co/papers
- **Jenis:** Paper discovery
- **Bidang:** AI dan ML
- **Yang dicari:** Paper, arXiv links, model dan resource kode/dataset terkait.
- **Cara pakai:** Cari judul atau task; periksa Code/Models/Datasets terkait.
- **Catatan:** Tidak semua paper memiliki training code open-source.

### Q. Jurnal, Benchmark Ml, Dan Kode Paper

#### [166] PLOS Computational Biology - Code Availability
- **URL:** https://journals.plos.org/ploscompbiol/s/code-availability
- **Jenis:** Jurnal kebijakan source code
- **Bidang:** Computational biology, ML biomedis
- **Yang dicari:** Paper yang wajib menyatakan lokasi kode buatan penulis terkait hasil riset, dengan pengecualian tertentu.
- **Cara pakai:** Cari paper pada jurnal; periksa Data/Code Availability, DOI serta repository.
- **Catatan:** Tidak semua paper memiliki paket training lengkap dan pengecualian kode berlaku.

### T. Benchmark, Dataset, Dan Implementasi Risetpaper

#### [193] Nature Scientific Data
- **URL:** https://www.nature.com/sdata/
- **Jenis:** Jurnal dataset + kode
- **Bidang:** Lintas bidang komputasional
- **Yang dicari:** Data descriptor dan code availability statement untuk kode pemrosesan data khusus.
- **Cara pakai:** Cari topik pada jurnal; buka Code availability dan akses software/data.
- **Catatan:** Tidak semua paper menggunakan custom code; sebagian mempunyai batasan akses.

#### [194] INSPIRE-HEP
- **URL:** https://inspirehep.net/
- **Jenis:** Discovery paper + resources
- **Bidang:** High-energy physics
- **Yang dicari:** Metadata paper fisika energi tinggi, identifier, eksperimen, tautan data/software terkait.
- **Cara pakai:** Cari DOI/arXiv HEP; ikuti related resources ke dataset/kode jika ada.
- **Catatan:** Indeks literatur, bukan portal kode langsung.


<a id="02-find-code"></a>
## Cari Source Code — 100 sumber

Menemukan implementasi kode dari paper: jurnal software, indeks kode, hub kode.

### A. Platform Khusus Research Code Dan Reproduksibilitas

#### [001] Journal of Open Source Software (JOSS)
- **URL:** https://joss.theoj.org/papers
- **Jenis:** Jurnal software
- **Bidang:** Software ilmiah lintas bidang
- **Yang dicari:** Artikel software, DOI, dan repositori implementasi yang ditautkan.
- **Cara pakai:** Cari kata kunci bidang; buka paper; ikuti tautan repository dan dokumentasi instalasi.
- **Catatan:** Fokusnya publikasi software, bukan semua jenis paper eksperimen.

#### [002] JMLR Machine Learning Open Source Software (MLOSS)
- **URL:** https://www.jmlr.org/mloss/
- **Jenis:** Jurnal software
- **Bidang:** Machine learning
- **Yang dicari:** Paper perangkat lunak ML dan tautan paket/source code.
- **Cara pakai:** Telusuri judul algoritma di arsip MLOSS, lalu cek tautan code serta versi library.
- **Catatan:** Artikel dapat menggunakan versi dependensi lama.

#### [004] Research Software Directory
- **URL:** https://research-software-directory.org/
- **Jenis:** Indeks software
- **Bidang:** Software akademik
- **Yang dicari:** Direktori proyek perangkat lunak riset, kontributor dan publikasi terkait.
- **Cara pakai:** Cari nama institusi, bidang, atau software; lanjutkan ke repo serta referensi paper.
- **Catatan:** Cakupan mengikuti institusi/komunitas yang berpartisipasi.

#### [006] Software Heritage
- **URL:** https://archive.softwareheritage.org/
- **Jenis:** Arsip kode
- **Bidang:** Lintas disiplin
- **Yang dicari:** Snapshot source code dan riwayat arsip software.
- **Cara pakai:** Cari URL/identitas repo dari paper; periksa apakah revisi kodenya diarsipkan.
- **Catatan:** Arsip kode tidak otomatis mencakup dataset maupun petunjuk eksekusi.

#### [007] Open Scientific Code Registry
- **URL:** https://openscicode.org/
- **Jenis:** Indeks kode
- **Bidang:** Neuroscience
- **Yang dicari:** Kode yang dirujuk dalam artikel atau penelitian neuroscience.
- **Cara pakai:** Cari judul paper atau nama metode, lalu ikuti kode yang terindeks.
- **Catatan:** Cakupannya terutama neuroscience; perlu cek pembaruan indeks.

#### [008] bio.tools
- **URL:** https://bio.tools/
- **Jenis:** Registry software
- **Bidang:** Bioinformatika
- **Yang dicari:** Daftar software, fungsi, publikasi dan tautan kodenya.
- **Cara pakai:** Saring berdasarkan fungsi bioinformatika; buka publikasi dan URL repositori.
- **Catatan:** Sebagian merupakan tools web, bukan full source code.

#### [009] SciCrunch Resources
- **URL:** https://scicrunch.org/resources
- **Jenis:** Registry alat
- **Bidang:** Biomedis dan ilmu hayati
- **Yang dicari:** Research resources, software, identifiers, dan informasi alat.
- **Cara pakai:** Cari nama tool atau RRID; temukan halaman vendor/proyek dan artikel terkait.
- **Catatan:** Tidak menjamin kode sumber tersedia secara terbuka.

#### [012] SciCodes
- **URL:** https://scicodes.net/
- **Jenis:** Jaringan registry
- **Bidang:** Software ilmiah
- **Yang dicari:** Daftar registry dan inisiatif pengindeksan kode ilmiah.
- **Cara pakai:** Mulai dari daftar mitra; pilih registry sesuai bidang riset.
- **Catatan:** Portal konsorsium, bukan mesin download kode tunggal.

### B. Repositori Kode Penelitian Dan Executable Papers

#### [013] Journal of Statistical Software
- **URL:** https://www.jstatsoft.org/
- **Jenis:** Jurnal software
- **Bidang:** Statistik, R dan Python
- **Yang dicari:** Paper implementasi metode, paket software dan materi replikasi.
- **Cara pakai:** Cari metode statistik; buka artikel dan supplementary code/CRAN/GitHub.
- **Catatan:** Perhatikan versi paket serta perbedaan API terbaru.

#### [014] The R Journal
- **URL:** https://journal.r-project.org/
- **Jenis:** Jurnal software
- **Bidang:** Statistik dengan R
- **Yang dicari:** Artikel penggunaan/pengembangan paket R serta kode contoh.
- **Cara pakai:** Cari nama algoritma; buka paper, contoh R, dan repo paket terkait.
- **Catatan:** Mayoritas ekosistem R, bukan Python.

#### [015] AEA Data and Code Repository
- **URL:** https://www.icpsr.umich.edu/sites/aea/home
- **Jenis:** Replikasi
- **Bidang:** Ekonomi empiris
- **Yang dicari:** Paket data, scripts, dokumentasi dan bahan replikasi artikel AEA.
- **Cara pakai:** Cari judul artikel; unduh replication package dan jalankan README.
- **Catatan:** Sebagian data berlisensi/terbatas dan tidak didistribusikan langsung.

#### [016] openICPSR
- **URL:** https://www.openicpsr.org/
- **Jenis:** Repositori
- **Bidang:** Ilmu sosial dan ekonomi
- **Yang dicari:** Dataset, kode, syntax files dan paket proyek penelitian.
- **Cara pakai:** Cari penulis/judul/DOI; saring tipe file lalu periksa lampiran kode.
- **Catatan:** Kelengkapan bahan bervariasi antar depositor.

#### [018] NASA Open Source Software
- **URL:** https://code.nasa.gov/
- **Jenis:** Katalog software
- **Bidang:** Antariksa, simulasi, sains
- **Yang dicari:** Proyek open-source NASA dan tautan repository.
- **Cara pakai:** Cari topik atau nama software; lanjut ke repository resmi.
- **Catatan:** Tidak semua software berkaitan langsung dengan satu paper.

#### [019] DOE CODE
- **URL:** https://www.osti.gov/doecode
- **Jenis:** Katalog software
- **Bidang:** Energi, fisika, komputasi
- **Yang dicari:** Software penelitian Departemen Energi AS beserta metadata.
- **Cara pakai:** Cari nama proyek atau DOI software; ikuti tautan source/download.
- **Catatan:** Lisensi dan kelengkapan source tergantung masing-masing item.

#### [020] CodaLab Worksheets
- **URL:** https://codalab.org/codalab-worksheets/
- **Jenis:** Eksperimen
- **Bidang:** ML dan komputasi
- **Yang dicari:** Worksheets yang mencatat command, data, hasil dan eksperimen.
- **Cara pakai:** Cari worksheet publik terkait benchmark; lihat run, inputs, outputs.
- **Catatan:** Akses dan ketersediaan lingkungan eksekusi tergantung proyek.

#### [021] Wolfram Notebook Archive
- **URL:** https://www.notebookarchive.org/
- **Jenis:** Notebook
- **Bidang:** Matematika dan komputasi
- **Yang dicari:** Notebook interaktif yang dapat dibaca/dijalankan dengan Wolfram.
- **Cara pakai:** Cari konsep matematis atau algoritma lalu unduh notebook.
- **Catatan:** Menjalankan lokal mungkin memerlukan Wolfram Language/produk terkait.

#### [022] Bioconductor
- **URL:** https://bioconductor.org/packages/release/bioc/
- **Jenis:** Paket software
- **Bidang:** Bioinformatika R
- **Yang dicari:** Paket open-source, source tarball, vignette, dan sitasi.
- **Cara pakai:** Cari paket atau tugas analitik; baca vignette dan artikel sitasinya.
- **Catatan:** Berfokus pada R/Bioconductor, bukan paper pada seluruh bidang.
- **Koreksi:** 2026-10-12: /packages/ mengembalikan 404. Diganti ke /packages/release/bioc/ (terverifikasi 200).

#### [023] CRAN Packages
- **URL:** https://cran.r-project.org/web/packages/
- **Jenis:** Paket software
- **Bidang:** R, statistik dan data mining
- **Yang dicari:** Source code paket R, dokumentasi, referensi metode.
- **Cara pakai:** Cari nama metode; buka Reference manual, source dan DESCRIPTION.
- **Catatan:** Paket bukan pengganti pembacaan paper sumber metode.

#### [024] PyPI
- **URL:** https://pypi.org/
- **Jenis:** Paket software
- **Bidang:** Python
- **Yang dicari:** Library dan tautan halaman source/publikasi jika dicantumkan.
- **Cara pakai:** Cari paket terkait algoritma; ikuti project links ke source dan paper.
- **Catatan:** Unggahan PyPI tidak otomatis melewati peer review ilmiah.

#### [026] Binder
- **URL:** https://mybinder.org/
- **Jenis:** Eksekusi notebook
- **Bidang:** Jupyter dan data science
- **Yang dicari:** Menjalankan repository notebook sebagai environment sementara.
- **Cara pakai:** Gunakan repo GitHub/GitLab dari paper lalu coba launch melalui Binder.
- **Catatan:** Binder sendiri bukan indeks paper; environment bisa gagal karena dependensi.

### D. Implementasi Source Code Secara Langsung

#### [047] GitHub Code Search
- **URL:** https://github.com/search?type=code
- **Jenis:** Pencarian kode
- **Bidang:** Lintas bidang
- **Yang dicari:** File source dan repository berdasarkan istilah spesifik.
- **Cara pakai:** Cari judul paper persis, nama metode, DOI, nama fungsi, atau dataset.
- **Catatan:** Cek lisensi, commit, dan keaslian penulis; hasil tidak peer-reviewed.

#### [048] GitHub Topic: paper-implementations
- **URL:** https://github.com/topics/paper-implementations
- **Jenis:** Kurasi repo
- **Bidang:** AI dan bidang lain
- **Yang dicari:** Repository berlabel implementasi paper.
- **Cara pakai:** Sort by recently updated; periksa citation, README dan training scripts.
- **Catatan:** Tag dikelola pemilik repo, bukan bukti kelengkapan.

#### [049] GitHub Topic: paper-implementation
- **URL:** https://github.com/topics/paper-implementation
- **Jenis:** Kurasi repo
- **Bidang:** AI dan bidang lain
- **Yang dicari:** Repository implementasi dari paper.
- **Cara pakai:** Gunakan pencarian topik; cocokkan DOI/judul dengan repository.
- **Catatan:** Label tidak membuktikan hasil eksperimen setara paper.

#### [050] GitHub Topic: research-paper-implementation
- **URL:** https://github.com/topics/research-paper-implementation
- **Jenis:** Kurasi repo
- **Bidang:** Computer science
- **Yang dicari:** Implementasi metode dari paper yang ditandai komunitas.
- **Cara pakai:** Saring bahasa Python, tingkat aktivitas, dan kesesuaian paper.
- **Catatan:** Repository bisa merupakan implementasi pihak ketiga.

#### [051] GitLab Explore
- **URL:** https://gitlab.com/explore
- **Jenis:** Hosting kode
- **Bidang:** Lintas bidang
- **Yang dicari:** Repositori dan proyek software yang dibuat publik.
- **Cara pakai:** Cari nama algoritma atau judul paper di GitLab.
- **Catatan:** Tidak semuanya terkait publikasi dan ada yang private.

#### [052] Hugging Face Models
- **URL:** https://huggingface.co/models
- **Jenis:** Hub model
- **Bidang:** Machine learning
- **Yang dicari:** Bobot model, konfigurasi, model cards dan tautan paper.
- **Cara pakai:** Filter task; lihat model card, arXiv paper, dan linked code.
- **Catatan:** Weights bukan otomatis training code atau dataset lengkap.

#### [053] Hugging Face Spaces
- **URL:** https://huggingface.co/spaces
- **Jenis:** Demo + kode
- **Bidang:** AI
- **Yang dicari:** Demo interaktif dan Git repo aplikasi untuk Space publik.
- **Cara pakai:** Temukan demo sesuai metode lalu buka Files and versions.
- **Catatan:** Kode demo bisa hanya inference, bukan implementasi training.

#### [054] Kaggle Code
- **URL:** https://www.kaggle.com/code
- **Jenis:** Notebook
- **Bidang:** Data science
- **Yang dicari:** Notebook Python/R untuk data dan algoritma.
- **Cara pakai:** Cari paper/metode/dataset, filter notebook dengan output jelas.
- **Catatan:** Notebook komunitas tidak selalu sesuai paper yang diklaim.

#### [055] R-universe
- **URL:** https://r-universe.dev/
- **Jenis:** Paket ilmiah
- **Bidang:** R
- **Yang dicari:** Paket, binary dan tautan sumber R dari berbagai komunitas.
- **Cara pakai:** Cari paket fungsi analisis, lanjut ke repository serta artikel sitasi.
- **Catatan:** Bukan indeks komprehensif kode paper.

#### [056] Codeberg Explore
- **URL:** https://codeberg.org/explore/repos
- **Jenis:** Hosting kode
- **Bidang:** Open-source
- **Yang dicari:** Repository open-source alternatif.
- **Cara pakai:** Gunakan kata kunci metode, paper, dan nama penulis.
- **Catatan:** Ketersediaan metadata akademik tidak konsisten.

#### [057] SourceForge Directory
- **URL:** https://sourceforge.net/directory/
- **Jenis:** Direktori software
- **Bidang:** Lintas bidang
- **Yang dicari:** Software, rilis dan download proyek teknis.
- **Cara pakai:** Cari tools scientific computing; periksa source, dokumentasi dan publikasi.
- **Catatan:** Banyak tool bukan reproduksi paper spesifik.

### E. Benchmark, Kompetisi, Baseline Dan Model Zoo

#### [064] OpenMMLab GitHub
- **URL:** https://github.com/open-mmlab
- **Jenis:** Framework penelitian
- **Bidang:** Computer vision
- **Yang dicari:** Implementasi model, config training dan model zoo.
- **Cara pakai:** Cari nama arsitektur; cek config, model checkpoint dan referensi paper.
- **Catatan:** Framework besar membutuhkan versi CUDA/PyTorch yang sesuai.

### F. Github Curated Lists Untuk Paper + Kode

#### [067] amusi CVPR2026 Papers with Code
- **URL:** https://github.com/amusi/CVPR2026-Papers-with-Code
- **Jenis:** Kurasi GitHub
- **Bidang:** Computer vision
- **Yang dicari:** Daftar paper CVPR 2026 dengan resource code saat tersedia.
- **Cara pakai:** Cari nama task/model di README; ikuti GitHub/project links.
- **Catatan:** Repositori kurasi komunitas, tautan mungkin tidak selalu diperbarui.

#### [068] firetix Awesome CVPR 2026 Papers
- **URL:** https://github.com/firetix/awesome-cvpr-2026-papers
- **Jenis:** Kurasi GitHub
- **Bidang:** Computer vision
- **Yang dicari:** Koleksi paper CVPR 2026 berdasarkan topik dan resources.
- **Cara pakai:** Filter kategori; cek apakah label code berarti source atau hanya project page.
- **Catatan:** Jangan samakan demo/model dengan full training code.

#### [069] MICCAI OpenSourcePapers
- **URL:** https://github.com/JunMa11/MICCAI-OpenSourcePapers
- **Jenis:** Kurasi GitHub
- **Bidang:** Medical AI
- **Yang dicari:** Daftar paper MICCAI dengan tautan source dan resources.
- **Cara pakai:** Cari nama metode, paper dan tahun; ikuti repo penulis.
- **Catatan:** Sebagian tautan bisa pindah atau berganti versi.

#### [070] Awesome MICCAI 2026
- **URL:** https://github.com/ambicuity/Awesome-MICCAI-2026
- **Jenis:** Kurasi GitHub
- **Bidang:** Medical AI
- **Yang dicari:** Daftar paper dan repository publik MICCAI 2026.
- **Cara pakai:** Cari medical image task dan cek URL kode per paper.
- **Catatan:** Perlu verifikasi kelengkapan data/replikasi.

#### [071] Awesome AI for Cybersecurity Papers
- **URL:** https://github.com/BaichengDanny/awesome-ai-for-cybersecurity-papers
- **Jenis:** Kurasi GitHub
- **Bidang:** AI untuk cybersecurity
- **Yang dicari:** Paper, benchmark dan beberapa tautan implementasi.
- **Cara pakai:** Pilih subbidang intrusion/malware/vulnerability; buka kode dan data asli.
- **Catatan:** Sebagian entri mungkin hanya referensi literatur.

#### [072] Awesome ML for Cybersecurity
- **URL:** https://github.com/jivoi/awesome-ml-for-cybersecurity
- **Jenis:** Kurasi GitHub
- **Bidang:** Cybersecurity
- **Yang dicari:** Daftar paper, tools, dataset dan resource ML keamanan.
- **Cara pakai:** Temukan sumber dataset atau baseline sesuai serangan/skenario.
- **Catatan:** Materi berbeda-beda kualitas dan kebaruannya.

#### [073] Machine Learning for Cyber Security
- **URL:** https://github.com/wtsxDev/Machine-Learning-for-Cyber-Security
- **Jenis:** Kurasi GitHub
- **Bidang:** Cybersecurity
- **Yang dicari:** Materi metode, dataset, dan sumber bacaan keamanan ML.
- **Cara pakai:** Cari kategori metode; lanjutkan ke sumber asli dan GitHub.
- **Catatan:** Jangan asumsikan semua resource memiliki kode lengkap.

#### [074] OpenSci Awesome ML Cybersecurity
- **URL:** https://github.com/opensci-hub/Awesome-ML-Cybersecurity
- **Jenis:** Kurasi GitHub
- **Bidang:** Cybersecurity
- **Yang dicari:** Koleksi literatur dan tools ML keamanan.
- **Cara pakai:** Cari teknik deteksi/klasifikasi dan bandingkan repository aktif.
- **Catatan:** Indeks komunitas bukan penilaian kinerja metode.

#### [075] Awesome AI Papers
- **URL:** https://github.com/songqiang321/Awesome-AI-Papers
- **Jenis:** Kurasi GitHub
- **Bidang:** AI
- **Yang dicari:** Daftar publikasi AI dan tautan pendukung.
- **Cara pakai:** Cari istilah riset; catat arXiv/DOI lalu cari implementasi.
- **Catatan:** Proporsi entri berkode dapat berbeda menurut topik.

#### [076] Awesome CV MasterHub
- **URL:** https://github.com/cuixing158/Awesome-CV-MasterHub
- **Jenis:** Kurasi GitHub
- **Bidang:** Computer vision
- **Yang dicari:** Koleksi model, paper dan informasi kode terkait.
- **Cara pakai:** Cari deteksi, segmentasi, klasifikasi lalu cek source link.
- **Catatan:** Periksa apakah link paper/kode masih aktif.

### G. Jurnal Kode Dan Notebook Ilmiah Khusus

#### [077] SciPost Physics Codebases
- **URL:** https://scipost.org/journals/SciPostPhysCodeb
- **Jenis:** Jurnal kode
- **Bidang:** Fisika komputasi
- **Yang dicari:** Artikel codebase dengan identitas publikasi dan arsip source.
- **Cara pakai:** Cari tipe simulasi; buka artikel dan rilis code yang disitir.
- **Catatan:** Dominan fisika, bukan semua disiplin.

#### [079] Astrophysics Source Code Library (ASCL)
- **URL:** https://ascl.net/
- **Jenis:** Registry kode
- **Bidang:** Astronomi dan astrofisika
- **Yang dicari:** Kode yang digunakan/dirujuk dalam publikasi astronomi.
- **Cara pakai:** Cari kode via nama software atau paper; ikuti source URL dan sitasi.
- **Catatan:** Tidak semua entri menawarkan installer modern.

#### [080] PhysioNet Software
- **URL:** https://physionet.org/software/
- **Jenis:** Katalog kode
- **Bidang:** Medis dan sinyal fisiologis
- **Yang dicari:** Software untuk ECG, ICU, biosignal, dan analisis klinis.
- **Cara pakai:** Cari toolkit sesuai dataset/riset; baca dokumentasi dan lisensi.
- **Catatan:** Data klinis dan izin pemakaian dapat berbeda dengan kode.

#### [082] Pangeo Gallery
- **URL:** https://gallery.pangeo.io/
- **Jenis:** Notebook contoh
- **Bidang:** Iklim, geospasial
- **Yang dicari:** Notebook Python/Jupyter untuk analisis data bumi.
- **Cara pakai:** Pilih notebook terkait dataset iklim/satelit, temukan repo sumber.
- **Catatan:** Contoh pengolahan data tidak selalu terkait paper tunggal.

### H. Portal Paper, Data, Notebook Dan Software

#### [083] Image Processing On Line (IPOL)
- **URL:** https://www.ipol.im/
- **Jenis:** Jurnal algoritma
- **Bidang:** Image processing
- **Yang dicari:** Artikel algoritma dengan source code dan online demo.
- **Cara pakai:** Cari teknik citra, baca penjelasan, akses kode dan jalankan contoh.
- **Catatan:** Cocok image processing klasik; cakupan ML tertentu terbatas.

#### [084] Journal of Open Research Software
- **URL:** https://openresearchsoftware.metajnl.com/
- **Jenis:** Jurnal software
- **Bidang:** Software riset lintas disiplin
- **Yang dicari:** Software metapapers dengan metadata ketersediaan kode.
- **Cara pakai:** Cari paper/software; ikuti availability statement ke repository.
- **Catatan:** Artikel software, bukan semua paper terapan.
- **Koreksi:** 2026-10-12: tidak dapat dijangkau (timeout) dari host audit, tetapi situs AKTIF (artikel terbit Sep 2026). Kemungkinan pembatasan IP/geo — bukan tautan mati.

#### [085] Journal of Open Source Education (JOSE)
- **URL:** https://jose.theoj.org/papers
- **Jenis:** Jurnal edukasi
- **Bidang:** Komputasi dan pendidikan
- **Yang dicari:** Software/materi pendidikan terbuka berikut repository.
- **Cara pakai:** Cari bahan pengajaran teknis; lihat repo dan materi notebook.
- **Catatan:** Tidak dirancang khusus untuk reproduksi hasil riset mutakhir.

#### [086] pyOpenSci Packages
- **URL:** https://www.pyopensci.org/python-packages/
- **Jenis:** Review software
- **Bidang:** Python ilmiah
- **Yang dicari:** Paket Python terkurasi dengan penilaian terbuka.
- **Cara pakai:** Cari task pengolahan data; buka source, review dan dokumentasi.
- **Catatan:** Review kualitas software bukan validasi seluruh klaim paper.

#### [087] rOpenSci Packages
- **URL:** https://ropensci.org/packages/
- **Jenis:** Review software
- **Bidang:** R dan open science
- **Yang dicari:** Paket R riset, dokumentasi, source dan beberapa review.
- **Cara pakai:** Filter kategori paket dan pelajari reference serta source repo.
- **Catatan:** Lebih cocok ekosistem R.

#### [089] ESA EarthCODE Workflows
- **URL:** https://earthcode.esa.int/workflows
- **Jenis:** Workflow riset
- **Bidang:** Earth observation
- **Yang dicari:** Workflow komputasi, metadata dan output riset geospasial.
- **Cara pakai:** Cari workflow berdasarkan sensor/metode lalu telusuri code artefact.
- **Catatan:** Sebagian pekerjaan terkait layanan/cloud tertentu.

#### [090] DANDI Notebooks
- **URL:** https://notebooks.dandiarchive.org/index.html
- **Jenis:** Notebook
- **Bidang:** Neuroscience
- **Yang dicari:** Notebook analisis untuk dataset neuroscience dan paper.
- **Cara pakai:** Pilih dataset DANDI, buka notebook lalu coba Colab bila tersedia.
- **Catatan:** Penyimpanan data dan notebook dapat berbeda lokasi.

### J. Darts, Jurnal Software Dan Kurasi Kode Tambahan

#### [106] SoftwareX
- **URL:** https://www.sciencedirect.com/journal/softwarex
- **Jenis:** Jurnal software
- **Bidang:** Komputasi ilmiah
- **Yang dicari:** Artikel software, availability statements dan tautan repo.
- **Cara pakai:** Cari nama tool atau topik; ikuti source code availability.
- **Catatan:** Akses full text dan lisensi artikel/software berbeda.

#### [107] ElsevierSoftwareX GitHub
- **URL:** https://github.com/ElsevierSoftwareX
- **Jenis:** Repository organisasi
- **Bidang:** Software riset
- **Yang dicari:** Repository yang dikaitkan dengan sebagian publikasi SoftwareX.
- **Cara pakai:** Cari nama paper di repo organisasi; cek versi dan paper DOI.
- **Catatan:** Tidak harus mencakup seluruh artikel jurnal.

#### [111] GitHub Topic: reproducible-paper
- **URL:** https://github.com/topics/reproducible-paper
- **Jenis:** Kurasi repo
- **Bidang:** Komputasi ilmiah
- **Yang dicari:** Repository yang menandai paket replikasi paper.
- **Cara pakai:** Cari repositori dengan scripts dan env, cocokkan publikasi.
- **Catatan:** Topik diisi sendiri oleh pemilik repo.

### K. Arsip Algoritma Dan Model Komputasi

#### [112] ACM Collected Algorithms (CALGO/Netlib)
- **URL:** https://www.netlib.org/toms/
- **Jenis:** Arsip algoritma
- **Bidang:** Numerical computing
- **Yang dicari:** Kode algoritma matematis/numerik yang terkait publikasi ACM TOMS.
- **Cara pakai:** Cari nomor algoritma atau nama metode, unduh source dan baca referensi.
- **Catatan:** Banyak kode historis memakai Fortran/C lawas.

#### [113] ModelDB
- **URL:** https://modeldb.science/
- **Jenis:** Repositori model
- **Bidang:** Computational neuroscience
- **Yang dicari:** Model simulasi neuron dan jaringan terkait paper.
- **Cara pakai:** Cari paper atau jenis neuron; unduh model files dan parameter.
- **Catatan:** Menjalankan simulasi dapat membutuhkan NEURON/GENESIS/tool khusus.

#### [114] Physiome Model Repository
- **URL:** https://models.physiomeproject.org/
- **Jenis:** Repositori model
- **Bidang:** Biologi/fisiologi
- **Yang dicari:** Model biologis dan matematis, format CellML dan kode pendukung.
- **Cara pakai:** Cari model berdasarkan artikel, lihat versi dan format eksekusi.
- **Catatan:** Model yang dapat dijalankan tidak selalu Python langsung.

#### [115] CoMSES Computational Model Library
- **URL:** https://www.comses.net/codebases/
- **Jenis:** Repositori model
- **Bidang:** Agent-based simulation
- **Yang dicari:** Model, source code, metadata paper dan review model.
- **Cara pakai:** Cari domain sosial/lingkungan; lihat Codebase dan publikasi terkait.
- **Catatan:** Perlu periksa versi software simulator yang digunakan.

#### [116] NetLogo Models Library
- **URL:** https://ccl.northwestern.edu/netlogo/models/
- **Jenis:** Model/contoh
- **Bidang:** Agent-based modeling
- **Yang dicari:** Kode model NetLogo dan contoh simulasi interaktif.
- **Cara pakai:** Cari fenomena/metode; jalankan model dan inspeksi source.
- **Catatan:** Model edukasi tidak otomatis representasi paper asli.

#### [117] Open Source Brain
- **URL:** https://www.opensourcebrain.org/
- **Jenis:** Repositori model
- **Bidang:** Neuroscience
- **Yang dicari:** Model otak, skrip simulasi dan data penelitian.
- **Cara pakai:** Cari publikasi/neural model; telusuri Git repository dan workflow.
- **Catatan:** Sebagian model bergantung simulator khusus.

#### [118] BioModels
- **URL:** https://www.ebi.ac.uk/biomodels/
- **Jenis:** Repositori model
- **Bidang:** Systems biology
- **Yang dicari:** Model matematika yang ditautkan ke publikasi, sering format SBML.
- **Cara pakai:** Cari judul/DOI paper; unduh model, jalankan dengan kompatibel tool.
- **Catatan:** Model persamaan berbeda dengan paket source code lengkap.

#### [120] REANA Demo BSM Search
- **URL:** https://github.com/reanahub/reana-demo-bsm-search
- **Jenis:** Contoh workflow
- **Bidang:** Fisika energi tinggi
- **Yang dicari:** Repository demonstrasi analisis dengan scripts dan workflow.
- **Cara pakai:** Baca workflow YAML serta tahap input-proses-output.
- **Catatan:** Satu contoh proyek, bukan direktori pencarian umum.

### L. Knowledge Graph Paper-Ke-Repository

#### [123] SemRepo Source
- **URL:** https://github.com/faerber-lab/semrepo
- **Jenis:** Source platform
- **Bidang:** Metadata ilmiah
- **Yang dicari:** Kode/pipeline pembangunan knowledge graph SemRepo.
- **Cara pakai:** Baca docs dan skema untuk integrasi sistem pencarian sendiri.
- **Catatan:** Source pengindeks, bukan kumpulan implementasi tiap paper.

### M. Repository Resmi Lab Ai

#### [125] Google Research Code
- **URL:** https://github.com/google-research/google-research
- **Jenis:** Repository lab
- **Bidang:** AI dan ML
- **Yang dicari:** Implementasi resmi/pendamping paper Google Research.
- **Cara pakai:** Cari nama paper dalam subfolder; baca README dan command eksperimen.
- **Catatan:** Banyak proyek historis; konfigurasi lingkungan bervariasi.

#### [126] Google DeepMind Research
- **URL:** https://github.com/google-deepmind/deepmind-research
- **Jenis:** Repository lab
- **Bidang:** AI dan ML
- **Yang dicari:** Kode yang dirilis untuk mendampingi paper DeepMind.
- **Cara pakai:** Cari nama paper; lihat training/evaluation dan lisensi.
- **Catatan:** Tidak semua model/weights/data penelitian dirilis.

#### [127] Meta Research GitHub
- **URL:** https://github.com/facebookresearch
- **Jenis:** Repository organisasi
- **Bidang:** AI dan ML
- **Yang dicari:** Source code penelitian Meta dan library terkait.
- **Cara pakai:** Cari nama riset atau arsitektur; pilih repository resmi.
- **Catatan:** Repository organisasi besar; tak semua kode merujuk paper.

### N. Sumber Dari Awal Percakapan Yang Belum Tercantum Dan Penanda Duplikat

#### [130] CatalyzeX
- **URL:** https://www.catalyzex.com/
- **Jenis:** Paper-to-code search
- **Bidang:** AI dan ML
- **Yang dicari:** Pencarian implementasi GitHub yang dihubungkan dengan paper.
- **Cara pakai:** Masukkan judul paper/arXiv ID, buka "Code" atau repositori terkait.
- **Catatan:** Link bisa implementasi pihak ketiga; perlu cek validitas.

#### [131] Code Ocean Capsules
- **URL:** https://codeocean.com/explore/capsules/
- **Jenis:** Executable research
- **Bidang:** Lintas disiplin
- **Yang dicari:** Paket kode, data, environment dan run untuk hasil paper.
- **Cara pakai:** Cari judul/artikel; buka Compute Capsule dan prosedur run.
- **Catatan:** Sebagian capsule/resource mensyaratkan akses atau lingkungan tertentu.

#### [133] GitHub Topic: paper-implementations (duplikat no. 48)
- **URL:** https://github.com/topics/paper-implementations
- **Jenis:** Kurasi repo
- **Bidang:** AI dan bidang lain
- **Yang dicari:** Tautan dari daftar pertama yang sama persis dengan nomor 48.
- **Cara pakai:** Gunakan petunjuk pencarian di nomor 48.
- **Catatan:** DUPLIKAT URL; dihitung sebagai jejak daftar awal, bukan website unik.

#### [134] Zenodo
- **URL:** https://zenodo.org/
- **Jenis:** Repositori DOI
- **Bidang:** Lintas disiplin
- **Yang dicari:** Rilis kode, replication packages, data, laporan dan DOI.
- **Cara pakai:** Cari judul, DOI, penulis, atau "replication package"; filter Software.
- **Catatan:** Lisensi dan jenis file bervariasi; tidak semua record berisi source.

#### [138] Papers With Code Data Archive
- **URL:** https://github.com/paperswithcode/paperswithcode-data
- **Jenis:** Arsip metadata
- **Bidang:** Machine learning
- **Yang dicari:** Data historis paper, repo, task, dan hubungan benchmark.
- **Cara pakai:** Gunakan dump metadata untuk pencarian massal/offline lalu validasi URL repo.
- **Catatan:** Sumber historis; tidak boleh diperlakukan sebagai indeks terkini.

#### [140] Papers With Code (situs historis)
- **URL:** https://paperswithcode.com/
- **Jenis:** Portal historis
- **Bidang:** Machine learning
- **Yang dicari:** Dahulu menghubungkan paper, code dan leaderboard.
- **Cara pakai:** Gunakan arsip nomor 138 atau alternatif terbaru; jangan andalkan situs lama.
- **Catatan:** Status layanan berubah/dihentikan; ini entri historis, bukan rekomendasi aktif.
- **Koreksi:** 2026-10-12: terkonfirmasi redirect ke huggingface.co/papers/trending (sesuai catatan historis). Gunakan arsip entri 138 untuk data.

### N. Workflow, Kode Penelitian, Dan Direktori Model

#### [143] nf-core Pipelines
- **URL:** https://nf-co.re/pipelines/
- **Jenis:** Pipeline open source
- **Bidang:** Bioinformatika, genomik
- **Yang dicari:** Pipeline Nextflow lengkap dengan source code, dokumentasi, parameter dan literatur.
- **Cara pakai:** Pilih pipeline berdasarkan jenis analisis; buka GitHub dan panduan penggunaan.
- **Catatan:** Fokus bioinformatika dan versi pipeline harus disesuaikan dengan paper.

#### [144] Archive of Formal Proofs (AFP)
- **URL:** https://www.isa-afp.org/
- **Jenis:** Arsip bukti formal
- **Bidang:** Formal methods, algoritma, matematika
- **Yang dicari:** Teori dan kode pembuktian Isabelle dengan publikasi pendukung.
- **Cara pakai:** Cari konsep atau paper; unduh entry formal proof dan periksa sesi build.
- **Catatan:** Kode berupa artefak pembuktian formal, bukan aplikasi Python konvensional.

#### [145] CSDMS Model Download Portal
- **URL:** https://csdms.colorado.edu/wiki/Model_portal
- **Jenis:** Katalog model
- **Bidang:** Geoscience, hidrologi, lingkungan
- **Yang dicari:** Model simulasi, perangkat lunak ilmiah, referensi artikel dan tautan unduhan.
- **Cara pakai:** Cari nama model; cek model metadata, halaman kode, dan paper yang menggunakannya.
- **Catatan:** Lisensi, bahasa kode, dan akses bervariasi menurut pemilik model.
- **Koreksi:** 2026-10-12: /wiki/Model_download_portal mengembalikan 404. Diganti ke /wiki/Model_portal (halaman resmi unduhan model).

#### [146] USGS Model Catalog
- **URL:** https://data.usgs.gov/modelcatalog/
- **Jenis:** Katalog model
- **Bidang:** Geoscience, lingkungan, hidrologi
- **Yang dicari:** Metadata model pemerintah, dokumentasi dan kemungkinan tautan software.
- **Cara pakai:** Cari kata kunci fenomena/algoritma; lanjutkan ke source code atau technical report.
- **Catatan:** Metadata model tidak selalu berarti implementasi publik tersedia.

#### [147] NITRC
- **URL:** https://www.nitrc.org/
- **Jenis:** Direktori software riset
- **Bidang:** Neuroimaging, neuroscience
- **Yang dicari:** Software, dataset, dokumentasi dan proyek pengolahan citra otak.
- **Cara pakai:** Cari aplikasi sesuai metode; lihat project files, code host, publikasi dan lisensi.
- **Catatan:** Ada tool binary saja atau proyek yang membutuhkan registrasi.

#### [149] Brainlife.io
- **URL:** https://brainlife.io/
- **Jenis:** Platform analisis
- **Bidang:** Neuroscience, neuroinformatics
- **Yang dicari:** Data, aplikasi analisis, workflow dan tools yang digunakan dalam publikasi.
- **Cara pakai:** Telusuri aplikasi/pipeline dan lihat dokumentasi serta repository terhubung.
- **Catatan:** Sebagian fungsi melalui layanan hosted dan memerlukan akun.

### O. Algoritma, Jurnal Software, Dan Reproducibility

#### [150] Geoscientific Model Development (GMD)
- **URL:** https://gmd.copernicus.org/
- **Jenis:** Jurnal dengan kebijakan kode
- **Bidang:** Iklim, atmosfer, pemodelan
- **Yang dicari:** Paper model komputasi dengan bagian code/data availability dan versi artefak.
- **Cara pakai:** Cari judul model; buka Code and data availability untuk arsip dan repository.
- **Catatan:** Ketersediaan bisa dibatasi atau kode bergantung stack ilmiah khusus.

#### [153] Graphics Replicability Database
- **URL:** https://graphicsreplicability.github.io/replicability.graphics/
- **Jenis:** Database replikasi
- **Bidang:** Computer graphics
- **Yang dicari:** Pemetaan paper computer graphics terhadap artefak dan status replikasi.
- **Cara pakai:** Telusuri paper dan cari tautan source/data yang dirujuk; verifikasi satu per satu.
- **Catatan:** Cakupan dan kebaruan rekaman dapat terbatas.

#### [154] MATLAB File Exchange
- **URL:** https://www.mathworks.com/matlabcentral/fileexchange/
- **Jenis:** Berbagi source code
- **Bidang:** Numerical computing, signal processing
- **Yang dicari:** Script dan paket MATLAB untuk berbagai metode numerik, pemodelan, simulasi.
- **Cara pakai:** Cari algoritma atau judul paper; lihat lisensi, dependensi dan contoh pemakaian.
- **Catatan:** Tidak semua proyek berasal dari paper peer-reviewed; bisa memerlukan MATLAB.

#### [155] Julia Packages
- **URL:** https://juliapackages.com/packages
- **Jenis:** Indeks paket
- **Bidang:** Matematika, optimasi, machine learning
- **Yang dicari:** Paket Julia dengan repository dan sebagian mempunyai paper akademik.
- **Cara pakai:** Cari algoritma/bidang dan lanjutkan ke link source serta artikel/citation.
- **Catatan:** Direktori paket, bukan indeks paper yang selalu mengandung kode eksperimen.

#### [156] Galaxy Tool Shed
- **URL:** https://toolshed.g2.bx.psu.edu/
- **Jenis:** Repositori tools workflow
- **Bidang:** Bioinformatika
- **Yang dicari:** Tool analisis, wrappers, dependensi, workflow serta referensi ilmiah.
- **Cara pakai:** Cari nama paket, periksa install info dan repository pengembang.
- **Catatan:** Banyak item wrapper untuk tool eksternal, bukan seluruh kode algoritma.

### P. Repositori Akademik Dan Jaringan Data

#### [160] EMBL-EBI BioStudies
- **URL:** https://www.ebi.ac.uk/biostudies/
- **Jenis:** Arsip studi ilmiah
- **Bidang:** Biologi, bioinformatika
- **Yang dicari:** Data studi, supplementary attachments, kode atau link jika disertakan.
- **Cara pakai:** Cari accession/DOI, lihat study files dan software links.
- **Catatan:** Format lampiran bervariasi; data dapat dibatasi.

### Q. Jurnal, Benchmark Ml, Dan Kode Paper

#### [167] Bioinformatics (Oxford Academic) - Application Notes
- **URL:** https://academic.oup.com/bioinformatics
- **Jenis:** Jurnal software/algoritma
- **Bidang:** Bioinformatika, genomics ML
- **Yang dicari:** Artikel penerapan algoritma baru dan software, umumnya dengan availability statement dan URL kode.
- **Cara pakai:** Cari Application Note / Software paper; cek Availability and Implementation.
- **Catatan:** Kebijakan akses dapat mencakup syarat penggunaan nonkomersial.

#### [173] aeon Time Series Toolkit
- **URL:** https://github.com/aeon-toolkit/aeon
- **Jenis:** Perpustakaan implementasi riset
- **Bidang:** Time series ML, anomaly detection
- **Yang dicari:** Kode Python untuk metode classification, regression, forecasting, clustering dan paper asal.
- **Cara pakai:** Cari estimator/algoritma dalam dokumentasi; ikuti citation dan contoh penggunaan.
- **Catatan:** Library terintegrasi dapat berbeda dari script orisinal paper.

### R. Implementasi Deep Learning Dan Nlp

#### [175] TensorFlow Model Garden
- **URL:** https://github.com/tensorflow/models
- **Jenis:** Repository kode model
- **Bidang:** Vision, NLP, speech, reinforcement learning
- **Yang dicari:** Kode research models dari paper terbit, script training, models dan dokumentasi.
- **Cara pakai:** Buka research/ atau official/; pilih paper, cocokkan TensorFlow version.
- **Catatan:** Sebagian model lama memakai TensorFlow 1 dan perlu penyesuaian.

#### [176] PyTorch Examples
- **URL:** https://github.com/pytorch/examples
- **Jenis:** Kode dan contoh baseline
- **Bidang:** Deep learning lintas task
- **Yang dicari:** Contoh CNN, Transformer, VAE, GAN, RL serta script training sederhana.
- **Cara pakai:** Cari folder model/tugas; jalankan baseline lalu telusuri referensi algoritma.
- **Catatan:** Contoh edukatif tidak selalu mereproduksi konfigurasi paper secara penuh.

#### [177] timm / PyTorch Image Models
- **URL:** https://github.com/huggingface/pytorch-image-models
- **Jenis:** Implementasi arsitektur
- **Bidang:** Computer vision
- **Yang dicari:** Implementasi beragam arsitektur dari paper, pretrained weights, training/eval scripts.
- **Cara pakai:** Cari nama arsitektur atau paper di model docs; jalankan script dan cek weights.
- **Catatan:** Bobot/varian model berbeda-beda; rujuk citation dan konfigurasi tepat.

#### [178] Detectron2
- **URL:** https://github.com/facebookresearch/detectron2
- **Jenis:** Framework model riset
- **Bidang:** Object detection, segmentation
- **Yang dicari:** Model zoo, baseline, config, checkpoint serta implementasi metode vision.
- **Cara pakai:** Cocokkan paper dengan configs/projects, jalankan training dan evaluasi.
- **Catatan:** Membutuhkan GPU/dependensi kompatibel untuk sejumlah tugas.

#### [180] OpenNMT
- **URL:** https://opennmt.net/
- **Jenis:** Toolkit model NLP
- **Bidang:** Machine translation, sequence modeling
- **Yang dicari:** Implementasi seq2seq dan Transformer, dokumentasi training serta referensi paper.
- **Cara pakai:** Pilih toolkit PyTorch atau TensorFlow, ikuti training/validation scripts.
- **Catatan:** Framework bukan indeks paper universal; cek versi dan tokenisasi.

#### [181] fairseq
- **URL:** https://github.com/facebookresearch/fairseq
- **Jenis:** Implementasi paper NLP
- **Bidang:** Machine translation, speech, language modeling
- **Yang dicari:** Repository algoritma seq-to-seq dan daftar penelitian yang diimplementasikan.
- **Cara pakai:** Cari daftar implemented papers; ikuti folder examples dan konfigurasi.
- **Catatan:** Sebagian paper mengandalkan dependency/model lawas; cek status maintenance.

### S. Materials Science, Energy, Dan Research Software

#### [186] Materials Project Software
- **URL:** https://github.com/materialsproject
- **Jenis:** Organisasi kode riset
- **Bidang:** Computational materials
- **Yang dicari:** Paket Python, API, tools analisis material dengan dokumentasi dan publikasi.
- **Cara pakai:** Cari library sesuai metode, cek repositori pymatgen/mp-api dan citation paper.
- **Catatan:** Kode toolkit tidak otomatis menyertakan seluruh data/training scripts paper.

#### [187] AiiDA
- **URL:** https://aiida.net/
- **Jenis:** Workflow reproducibility
- **Bidang:** Scientific computing, material simulation
- **Yang dicari:** Framework Python workflow, provenance graph dan plugin koneksi ke software simulasi.
- **Cara pakai:** Cari workflow/plugin AiiDA yang dipakai penulis; impor dan jalankan prosesnya.
- **Catatan:** AiiDA merupakan infrastruktur, bukan katalog lengkap semua paper.

#### [188] PyPSA
- **URL:** https://github.com/PyPSA/PyPSA
- **Jenis:** Software penelitian + paper
- **Bidang:** Energy systems, electrical engineering
- **Yang dicari:** Kode optimasi sistem tenaga, benchmark, examples dan paper referensi.
- **Cara pakai:** Cari model studi kasus PyPSA, replikasi skenario dan versi solver.
- **Catatan:** Software tool utama perlu data kasus studi untuk mereplikasi paper tertentu.

#### [189] Pangeo Forge Recipes
- **URL:** https://github.com/pangeo-forge/pangeo-forge-recipes
- **Jenis:** Pipeline data ilmiah
- **Bidang:** Climate, geospatial, earth data
- **Yang dicari:** Kode pipeline konversi dataset ke format analisis cloud.
- **Cara pakai:** Cari recipe/feeds yang relevan dan referensi asal data serta publish metadata.
- **Catatan:** Repository ini menyatakan tidak lagi dalam pengembangan aktif; bukan indeks kode paper.

### T. Benchmark, Dataset, Dan Implementasi Risetpaper

#### [196] openmod Open Models Directory
- **URL:** https://wiki.openmod-initiative.org/wiki/Open_Models
- **Jenis:** Katalog kode pemodelan
- **Bidang:** Energy system modelling
- **Yang dicari:** Daftar model energi open-source, bahasa pemrograman, lisensi dan link kode.
- **Cara pakai:** Filter model energi; lanjut ke repository lalu paper metode yang dirujuk.
- **Catatan:** Katalog komunitas dapat mencakup entri lama atau framework yang sama.

#### [198] PyTorch Geometric (PyG)
- **URL:** https://github.com/pyg-team/pytorch_geometric
- **Jenis:** Kode metode paper
- **Bidang:** Graph neural networks
- **Yang dicari:** Layer GNN dari berbagai paper, datasets, contoh train/eval dan model.
- **Cara pakai:** Cari nama metode dalam docs dan examples; ikuti referensi paper pada layer.
- **Catatan:** Framework implementation tidak identik dengan semua pipeline paper.


<a id="03-datasets"></a>
## Cari Dataset — 17 sumber

Repositori dataset dan materi pendukung publikasi.

### A. Platform Khusus Research Code Dan Reproduksibilitas

#### [010] OpenML
- **URL:** https://www.openml.org/
- **Jenis:** Benchmark/data
- **Bidang:** Machine learning
- **Yang dicari:** Dataset, tasks, runs, evaluasi algoritma, dan metadata eksperimen.
- **Cara pakai:** Pilih task, telusuri runs/baselines lalu cocokkan metode dengan paket Python/R.
- **Catatan:** Runs eksperimen tidak selalu menyertakan repository paper lengkap.

### B. Repositori Kode Penelitian Dan Executable Papers

#### [017] Open Science Framework (OSF)
- **URL:** https://osf.io/
- **Jenis:** Repositori proyek
- **Bidang:** Lintas disiplin
- **Yang dicari:** Proyek, preregistrasi, data, kode, protokol, dan bahan riset.
- **Cara pakai:** Cari proyek publik; cek Components, Files, Wiki, dan koneksi repositori.
- **Catatan:** Sebagian proyek private, embargo, atau hanya data/protokol.

### H. Portal Paper, Data, Notebook Dan Software

#### [088] GigaDB
- **URL:** https://gigadb.org/
- **Jenis:** Data + software
- **Bidang:** Bioinformatika, data science
- **Yang dicari:** Dataset besar, software dan workflow pendukung publikasi.
- **Cara pakai:** Cari dataset/studi; cek bagian Files/Tools/Code dan DOI.
- **Catatan:** Tidak setiap record berisi kode.

#### [091] Dryad
- **URL:** https://datadryad.org/
- **Jenis:** Data pendukung
- **Bidang:** Lintas disiplin
- **Yang dicari:** Dataset ilmiah dan materi riset yang dapat dikutip.
- **Cara pakai:** Cari DOI/judul; lihat metadata dan tautan Zenodo untuk software.
- **Catatan:** Fokus utama data; source code tidak selalu disertakan.

#### [093] CERN Open Data
- **URL:** https://opendata.cern.ch/
- **Jenis:** Open data + contoh
- **Bidang:** Fisika energi tinggi
- **Yang dicari:** Data eksperimen, software contoh, analisis dan dokumentasi.
- **Cara pakai:** Pilih dataset dan contoh notebook/run analysis, lihat versi software.
- **Catatan:** Data/lingkungan fisika dapat memerlukan storage besar.

#### [094] Mendeley Data
- **URL:** https://data.mendeley.com/
- **Jenis:** Repositori data
- **Bidang:** Lintas disiplin
- **Yang dicari:** Dataset serta supplementary yang kadang memuat source scripts.
- **Cara pakai:** Cari judul paper; periksa berkas .py/.R/.m dan README.
- **Catatan:** Berorientasi data; kode tidak selalu tersedia.

### N. Sumber Dari Awal Percakapan Yang Belum Tercantum Dan Penanda Duplikat

#### [136] Figshare
- **URL:** https://figshare.com/
- **Jenis:** Repositori riset
- **Bidang:** Lintas disiplin
- **Yang dicari:** Dataset, software, supporting files dan materi penelitian.
- **Cara pakai:** Cari judul paper, DOI atau "source code"; periksa file download.
- **Catatan:** Banyak record berupa data/figure, bukan source code.

#### [139] Harvard Dataverse
- **URL:** https://dataverse.harvard.edu/
- **Jenis:** Repositori data
- **Bidang:** Lintas disiplin
- **Yang dicari:** Dataset penelitian, file pendukung, kode jika depositor menyertakan.
- **Cara pakai:** Cari judul/DOI paper; lihat Files dan metadata lalu pilih file script.
- **Catatan:** Fokus dataset; ketersediaan source code berbeda antar record.

### P. Repositori Akademik Dan Jaringan Data

#### [157] 4TU.ResearchData
- **URL:** https://data.4tu.nl/
- **Jenis:** Repositori data/software
- **Bidang:** Engineering, teknik, geoscience
- **Yang dicari:** Dataset, model, script dan artefak komputasi penelitian dengan DOI.
- **Cara pakai:** Cari paper/title dan gunakan filter tipe record; unduh files & metadata.
- **Catatan:** Tidak setiap record memuat kode, sebagian fokus dataset.

#### [158] DataverseNO
- **URL:** https://dataverse.no/
- **Jenis:** Repositori Dataverse
- **Bidang:** Penelitian lintas disiplin
- **Yang dicari:** Dataset, script R/Python, replication package, metadata dan DOI.
- **Cara pakai:** Cari keyword atau judul publikasi; periksa tab Files untuk script/data.
- **Catatan:** Sama seperti Harvard Dataverse, ketersediaan kode tergantung deposit.

#### [159] Borealis Canadian Dataverse Repository
- **URL:** https://borealisdata.ca/
- **Jenis:** Repositori Dataverse
- **Bidang:** Penelitian lintas disiplin
- **Yang dicari:** Dataset riset Kanada serta script atau dokumen pendukung jika tersedia.
- **Cara pakai:** Telusuri judul paper dan list file di record; simpan DOI serta lisensi.
- **Catatan:** Lebih berorientasi data daripada source code lengkap.

#### [161] PANGAEA
- **URL:** https://www.pangaea.de/
- **Jenis:** Repositori data
- **Bidang:** Earth science, geoscience
- **Yang dicari:** Dataset dengan metadata kuat, DOI, referensi paper dan bahan pendukung.
- **Cara pakai:** Cari publikasi atau parameter; telusuri references serta external links.
- **Catatan:** Sumber data, bukan prioritas bila kebutuhan utama source code.

### Q. Jurnal, Benchmark Ml, Dan Kode Paper

#### [168] Materials Cloud Archive
- **URL:** https://archive.materialscloud.org/
- **Jenis:** Arsip data/simulasi
- **Bidang:** Computational materials science
- **Yang dicari:** Data perhitungan, workflow AiiDA, input/output dan kadang code untuk reproduksi paper.
- **Cara pakai:** Cari nama material, judul paper atau DOI; buka file pendukung dan provenance.
- **Catatan:** Bergantung software fisika komputasi dan tidak semua deposit berisi kode.

### R. Implementasi Deep Learning Dan Nlp

#### [174] Hugging Face Datasets
- **URL:** https://huggingface.co/datasets
- **Jenis:** Katalog dataset & cards
- **Bidang:** AI, NLP, vision, audio
- **Yang dicari:** Dataset Hub, dataset cards, lisensi, splits dan referensi paper bila ditulis author.
- **Cara pakai:** Cari dataset yang disebut paper; cek Dataset Card lalu ikuti repository kode.
- **Catatan:** Portal dataset; ketersediaan script training tidak dijamin.

### S. Materials Science, Energy, Dan Research Software

#### [185] NOMAD Laboratory
- **URL:** https://nomad-lab.eu/
- **Jenis:** Arsip data/workflow
- **Bidang:** Materials informatics
- **Yang dicari:** Data simulasi dan eksperimen material serta metadata yang dapat dikaitkan ke workflow.
- **Cara pakai:** Cari record dengan nama material/publikasi; periksa file input-output dan link code.
- **Catatan:** Utamanya data komputasional; source code tidak selalu tersedia.

### T. Benchmark, Dataset, Dan Implementasi Risetpaper

#### [191] UCI Machine Learning Repository
- **URL:** https://archive.ics.uci.edu/
- **Jenis:** Repositori dataset
- **Bidang:** Machine learning umum
- **Yang dicari:** Dataset klasik dan baru beserta deskripsi tugas dan sitasi.
- **Cara pakai:** Temukan dataset pada paper lalu telusuri implementasi dari artikel GitHub.
- **Catatan:** Berisi data, tidak menjanjikan kode implementasi paper.

#### [195] HEPData
- **URL:** https://www.hepdata.net/
- **Jenis:** Data penelitian + auxiliary files
- **Bidang:** High-energy physics
- **Yang dicari:** Tabel data paper fisika, metadata, resource files tambahan, API dan DOI.
- **Cara pakai:** Cari INSPIRE paper atau collaboration; lihat resources dan downloads record.
- **Catatan:** Kode hanya ada jika disertakan sebagai auxiliary file atau link.


<a id="04-reproduce"></a>
## Reproduksi Eksperimen — 43 sumber

Artifact evaluation, benchmark, paket replikasi, model zoo.

### A. Platform Khusus Research Code Dan Reproduksibilitas

#### [003] ReScience C
- **URL:** https://rescience.github.io/read/
- **Jenis:** Reproduksibilitas
- **Bidang:** Komputasi ilmiah
- **Yang dicari:** Artikel replikasi beserta kode pendukung eksperimen.
- **Cara pakai:** Mulai dari hasil reproduksi paper; buka link Code; bandingkan metode asli dan reproduksinya.
- **Catatan:** Replikasi dapat memiliki perbedaan hasil yang dibahas dalam artikelnya.

### B. Repositori Kode Penelitian Dan Executable Papers

#### [025] Renku
- **URL:** https://renkulab.io/
- **Jenis:** Platform reproduksibilitas
- **Bidang:** Data science
- **Yang dicari:** Proyek komputasi kolaboratif, workflow dan lingkungan penelitian.
- **Cara pakai:** Cari proyek publik; pelajari metadata, repository dan workflow.
- **Catatan:** Sangat bergantung pada setelan publikasi dan akses proyek.

### E. Benchmark, Kompetisi, Baseline Dan Model Zoo

#### [058] MLCommons / MLPerf
- **URL:** https://mlcommons.org/benchmarks/
- **Jenis:** Benchmark
- **Bidang:** AI/ML
- **Yang dicari:** Suite benchmark, hasil, aturan evaluasi, implementasi acuan.
- **Cara pakai:** Pilih benchmark; ikuti reference implementation dan konfigurasi run.
- **Catatan:** Benchmark bukan pengganti kode metode paper tertentu.

#### [059] Codabench
- **URL:** https://www.codabench.org/
- **Jenis:** Benchmark
- **Bidang:** AI, data science
- **Yang dicari:** Benchmark, paket evaluation, dan submission algoritma.
- **Cara pakai:** Cari competition akademik; unduh starter kit jika tersedia.
- **Catatan:** Akses kode submission peserta bervariasi.

#### [060] AIcrowd Challenges
- **URL:** https://www.aicrowd.com/challenges
- **Jenis:** Kompetisi
- **Bidang:** AI dan ML
- **Yang dicari:** Datasets, baseline, starter scripts pada challenge tertentu.
- **Cara pakai:** Buka challenge; lihat resources, baseline repository dan forum.
- **Catatan:** Banyak challenge memiliki fase/akses terbatas.

#### [061] EvalAI
- **URL:** https://eval.ai/
- **Jenis:** Evaluasi AI
- **Bidang:** AI
- **Yang dicari:** Challenge, evaluasi model dan leaderboard.
- **Cara pakai:** Cari challenge yang terhubung dengan paper; periksa baseline dan submission docs.
- **Catatan:** Tidak semua solusi peserta open source.

#### [062] Grand Challenge
- **URL:** https://grand-challenge.org/challenges/
- **Jenis:** Benchmark medis
- **Bidang:** Medical image analysis
- **Yang dicari:** Dataset dan benchmark medis dengan protokol evaluasi.
- **Cara pakai:** Pilih challenge; baca dataset policy dan starter code.
- **Catatan:** Data medis dapat memerlukan registrasi atau perjanjian.

#### [063] DrivenData Competitions
- **URL:** https://www.drivendata.org/competitions/
- **Jenis:** Kompetisi
- **Bidang:** Data science untuk dampak sosial
- **Yang dicari:** Data kompetisi, problem statement dan baseline di beberapa event.
- **Cara pakai:** Cari topik; buka Benchmarks, Resources atau community solutions.
- **Catatan:** Kode top solutions tidak selalu dipublikasikan.

#### [065] MONAI Model Zoo
- **URL:** https://github.com/Project-MONAI/model-zoo
- **Jenis:** Model zoo
- **Bidang:** Medical imaging AI
- **Yang dicari:** Paket model dan konfigurasi eksperimen.
- **Cara pakai:** Cari model bundle; baca metadata, dataset dan workflow training/inference.
- **Catatan:** Model bundle belum tentu memuat data medis asli.

#### [066] Kaggle Competitions
- **URL:** https://www.kaggle.com/competitions
- **Jenis:** Kompetisi/benchmark
- **Bidang:** AI dan data science
- **Yang dicari:** Datasets, evaluation metric, diskusi dan notebook.
- **Cara pakai:** Buka competition; lihat Code dan referensi teknik pemenang.
- **Catatan:** Solusi kompetisi bukan otomatis implementasi publikasi ilmiah.

### G. Jurnal Kode Dan Notebook Ilmiah Khusus

#### [078] NeuroLibre
- **URL:** https://neurolibre.org/
- **Jenis:** Executable article
- **Bidang:** Neuroscience
- **Yang dicari:** Artikel interaktif berbasis notebook, kode, data dan lingkungan.
- **Cara pakai:** Pilih paper dan buka notebook interaktif/repo pendukung.
- **Catatan:** Environment mungkin memakai resource komputasi khusus.

#### [081] Whole Tale
- **URL:** https://wholetale.readthedocs.io/en/stable/
- **Jenis:** Platform reproducibility
- **Bidang:** Komputasi ilmiah
- **Yang dicari:** Konsep paket reproduksibilitas dan dokumentasi workflow.
- **Cara pakai:** Pelajari cara mengekspor tale untuk gabungkan code-data-env.
- **Catatan:** Tautan ini terutama dokumentasi; bukan katalog publikasi utama.

### I. Konferensi Dan Artifact Evaluation

#### [095] Security Research Artifacts
- **URL:** https://secartifacts.github.io/
- **Jenis:** Indeks artefak
- **Bidang:** Cybersecurity
- **Yang dicari:** Tautan research artifacts konferensi keamanan.
- **Cara pakai:** Cari konferensi/tahun atau paper; ikuti repo/arsip artefak.
- **Catatan:** Indeks tidak menjamin seluruh artefak tetap online.

#### [096] SIGMOD Reproducibility
- **URL:** https://reproducibility.sigmod.org/
- **Jenis:** Reproduksibilitas konferensi
- **Bidang:** Database systems
- **Yang dicari:** Artifacts, experiment scripts dan laporan reproduksibilitas.
- **Cara pakai:** Cari paper SIGMOD; lihat artifact evaluation dan hasil reproduksi.
- **Catatan:** Beberapa artefak memerlukan resource server besar.

#### [097] ICSE 2026 Artifact Evaluation
- **URL:** https://conf.researchr.org/track/icse-2026/icse-2026-artifact-evaluation
- **Jenis:** Program konferensi
- **Bidang:** Software engineering
- **Yang dicari:** Pedoman dan paper yang ikut evaluasi artefak ICSE.
- **Cara pakai:** Temukan accepted artifacts lalu akses arsip paper terkait.
- **Catatan:** Halaman program, tidak selalu direktori unduhan kode.

#### [098] ISSTA 2026 Artifact Evaluation
- **URL:** https://conf.researchr.org/track/issta-2026/issta-2026-artifact-evaluation
- **Jenis:** Program konferensi
- **Bidang:** Software testing
- **Yang dicari:** Paket eksperimen static/dynamic analysis dan testing.
- **Cara pakai:** Cari paper yang memiliki badge artefak lalu cek repo.
- **Catatan:** Sebagian artefak punya batasan lisensi/perangkat.

#### [099] POPL 2026 Artifact Evaluation
- **URL:** https://popl26.sigplan.org/track/POPL-2026-artifact-evaluation
- **Jenis:** Program konferensi
- **Bidang:** Programming languages
- **Yang dicari:** Compiler, interpreter, proof artifacts dan implementasi riset.
- **Cara pakai:** Telusuri paper POPL dan artifact appendix.
- **Catatan:** Program evaluasi tidak sama dengan repositori kode terbuka.

#### [100] PLDI 2026 Research Artifacts
- **URL:** https://pldi26.sigplan.org/track/pldi-2026-pldi-research-artifacts
- **Jenis:** Program konferensi
- **Bidang:** Compiler/programming languages
- **Yang dicari:** Kode eksperimen compiler, bahasa dan optimasi.
- **Cara pakai:** Cari artifact badge; lihat container/VM/code yang dibagikan.
- **Catatan:** Mungkin perlu toolchain lama/khusus.

#### [101] ICFP 2026 Artifact Evaluation
- **URL:** https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation
- **Jenis:** Program konferensi
- **Bidang:** Functional programming
- **Yang dicari:** Implementasi bahasa fungsional dan bukti/eksperimen.
- **Cara pakai:** Mulai dari accepted papers, cari link artifact.
- **Catatan:** Kelengkapan tergantung penulis dan evaluasi.

#### [102] EuroSys 2026 Artifacts
- **URL:** https://sysartifacts.github.io/eurosys2026/index
- **Jenis:** Program konferensi
- **Bidang:** Distributed systems
- **Yang dicari:** Artefak eksperimen sistem operasi/cloud/distribusi.
- **Cara pakai:** Cari artikel dengan artifact badge; cek instruksi deployment.
- **Catatan:** Resource cluster dan kernel khusus mungkin dibutuhkan.

#### [103] ACM CCS 2026 Artifacts
- **URL:** https://www.sigsac.org/ccs/CCS2026/call-for/call-for-artifacts.html
- **Jenis:** Program konferensi
- **Bidang:** Cybersecurity
- **Yang dicari:** Pedoman rilis dan penilaian artefak paper keamanan.
- **Cara pakai:** Telusuri accepted papers yang menyerahkan artefak; cek GitHub/Zenodo.
- **Catatan:** Tautan adalah call for artifacts, bukan daftar seluruh kode.

#### [104] ISCA 2026 Artifact Evaluation
- **URL:** https://iscaconf.org/isca2026/submit/artifactevaluation.php
- **Jenis:** Program konferensi
- **Bidang:** Arsitektur komputer
- **Yang dicari:** Artefak eksperimen hardware/compiler/performance.
- **Cara pakai:** Cari accepted artifacts; baca petunjuk toolchain dan environment.
- **Catatan:** Hardware khusus dapat membatasi reproduksibilitas.

### J. Darts, Jurnal Software Dan Kurasi Kode Tambahan

#### [105] Dagstuhl Artifacts Series (DARTS)
- **URL:** https://drops.dagstuhl.de/entities/journal/DARTS
- **Jenis:** Jurnal artefak
- **Bidang:** Computer science
- **Yang dicari:** Publikasi artefak berupa kode, VM, dataset dan scripts.
- **Cara pakai:** Cari paper terkait; unduh artifact package dan baca README evaluasi.
- **Catatan:** Beberapa paket besar atau bergantung tool khusus.

### K. Arsip Algoritma Dan Model Komputasi

#### [119] CERN REANA
- **URL:** https://github.com/reanahub/reana
- **Jenis:** Framework
- **Bidang:** Reproduksibilitas HEP
- **Yang dicari:** Platform eksekusi computational workflows reproducible.
- **Cara pakai:** Pelajari orchestrator; cari contoh analisis yang dapat dibangun ulang.
- **Catatan:** Ini infrastruktur, bukan database seluruh paper.

### L. Knowledge Graph Paper-Ke-Repository

#### [124] Wizwand
- **URL:** https://www.wizwand.com/
- **Jenis:** Discovery benchmark
- **Bidang:** Machine learning
- **Yang dicari:** Indeks paper, benchmark dan state-of-the-art terkait.
- **Cara pakai:** Cari task/model lalu ikuti paper maupun code links jika ada.
- **Catatan:** Periksa apakah halaman dan data aktif/terbarui.
- **Koreksi:** 2026-10-12: wizwand.com sekarang mengalihkan (redirect) ke sota2.com/research — kemungkinan rebranding. URL masih berfungsi sebagai pintu masuk.

### N. Sumber Dari Awal Percakapan Yang Belum Tercantum Dan Penanda Duplikat

#### [135] HyperAI Papers
- **URL:** https://hyper.ai/en/papers
- **Jenis:** Paper/benchmark discovery
- **Bidang:** AI dan ML
- **Yang dicari:** Artikel dan metadata model/benchmark terkait AI.
- **Cara pakai:** Cari metode atau topik; lanjut ke paper dan resource kode.
- **Catatan:** Periksa tautan aktif serta tanggal pembaruan.

#### [137] CodeSOTA
- **URL:** https://www.codesota.com/
- **Jenis:** Paper/benchmark discovery
- **Bidang:** Machine learning
- **Yang dicari:** Penelusuran model, hasil benchmark dan implementasi jika tersedia.
- **Cara pakai:** Cari task/model, telusuri referensi paper dan code links.
- **Catatan:** Perlu mengecek status situs dan kebaruan leaderboard.

### N. Workflow, Kode Penelitian, Dan Direktori Model

#### [141] WorkflowHub
- **URL:** https://workflowhub.eu/
- **Jenis:** Workflow registry
- **Bidang:** Bioinformatika, komputasi lintas disiplin
- **Yang dicari:** Workflow ilmiah, file alur kerja, metadata penulis dan tautan publikasi.
- **Cara pakai:** Cari judul metode atau keyword; buka workflow dan periksa file serta referensi paper.
- **Catatan:** Tidak semua workflow mencakup dataset penuh; format engine bervariasi.

#### [142] Dockstore
- **URL:** https://dockstore.org/
- **Jenis:** Workflow registry
- **Bidang:** Bioinformatika dan komputasi reproducible
- **Yang dicari:** Workflow containerized dan deskriptor CWL/WDL/Nextflow/Galaxy terkait penelitian.
- **Cara pakai:** Cari workflow dan lihat source repository, container image, test files dan versinya.
- **Catatan:** Menjalankan workflow dapat memerlukan compute/cloud, container, atau akses data.

#### [148] BioImage Model Zoo
- **URL:** https://bioimage.io/
- **Jenis:** Model zoo
- **Bidang:** Bioimaging, microscopy AI
- **Yang dicari:** Model DL biomedis, format model, contoh penggunaan, weights dan referensi paper.
- **Cara pakai:** Cari task/model, buka resource dan identifikasi implementation atau notebook.
- **Catatan:** Model weights tidak sama dengan source training code; validasi tiap item.

### O. Algoritma, Jurnal Software, Dan Reproducibility

#### [152] Graphics Replicability Stamp Initiative (GRSI)
- **URL:** https://www.replicabilitystamp.org/
- **Jenis:** Inisiatif penilaian artefak
- **Bidang:** Computer graphics, visualization
- **Yang dicari:** Paper yang memperoleh penilaian replicability beserta link kode dan data.
- **Cara pakai:** Pilih tahun/paper bersertifikasi; periksa material dan petunjuk reproduksi.
- **Catatan:** Penilaian mengikuti protokol GRSI, bukan jaminan eksperimen mudah dijalankan.

### Q. Jurnal, Benchmark Ml, Dan Kode Paper

#### [169] Open Graph Benchmark (OGB)
- **URL:** https://ogb.stanford.edu/
- **Jenis:** Benchmark + evaluator
- **Bidang:** Graph machine learning
- **Yang dicari:** Dataset graph, baseline, data loader, evaluators dan leaderboard.
- **Cara pakai:** Pilih graph/node/link task; lihat baseline scripts dan evaluasi resmi.
- **Catatan:** Benchmark bukan satu implementasi spesifik semua paper GNN.

#### [170] NeurIPS 2026 Evaluations & Datasets Track
- **URL:** https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets
- **Jenis:** Venue paper benchmark
- **Bidang:** Machine learning evaluation
- **Yang dicari:** Paper dataset/evaluation 2026 dan aturan keterbukaan code/dataset untuk camera-ready.
- **Cara pakai:** Cari paper penerimaan melalui proceedings/OpenReview; cek supplementary dan source.
- **Catatan:** Link ini halaman track/call, bukan katalog unduhan paper langsung.

#### [171] NLP Progress
- **URL:** https://nlpprogress.com/
- **Jenis:** Indeks benchmark
- **Bidang:** Natural language processing
- **Yang dicari:** Daftar task NLP, benchmark, metode, publikasi serta link kode jika tersedia.
- **Cara pakai:** Pilih NLP task; telusuri kolom Code dan paper untuk implementasi resmi.
- **Catatan:** Maintenance tidak selalu terbaru; sebagian task tidak memiliki code link.

#### [172] Time Series Classification Website
- **URL:** https://www.timeseriesclassification.com/
- **Jenis:** Benchmark dan kode
- **Bidang:** Time series ML
- **Yang dicari:** Arsip UCR/UEA, hasil benchmark, tautan toolkit aeon/tsml dan baseline.
- **Cara pakai:** Pilih classification/clustering/regression, bandingkan paper dengan hasil dan kode.
- **Catatan:** Dataset/baseline berasal dari berbagai tahun; cocokkan split/protokol.

### R. Implementasi Deep Learning Dan Nlp

#### [179] MMDetection
- **URL:** https://github.com/open-mmlab/mmdetection
- **Jenis:** Model zoo dan framework
- **Bidang:** Object detection, segmentation
- **Yang dicari:** Kode arsitektur paper, config training, weights, benchmark COCO dan evaluasi.
- **Cara pakai:** Cari nama model di model zoo, cek README paper dan jalankan config baseline.
- **Catatan:** Bagian dari OpenMMLab [64]; berbeda titik masuk dari daftar organisasi.

#### [182] EleutherAI Language Model Evaluation Harness
- **URL:** https://github.com/EleutherAI/lm-evaluation-harness
- **Jenis:** Benchmark evaluation code
- **Bidang:** LLM, NLP
- **Yang dicari:** Framework benchmark, task configs, evaluators dan sitasi hasil eksperimen.
- **Cara pakai:** Cari benchmark yang digunakan dalam paper; cocokkan few-shot setup/metric/model.
- **Catatan:** Tool evaluasi, bukan implementasi training semua LLM.

### S. Materials Science, Energy, Dan Research Software

#### [183] Open Catalyst Project
- **URL:** https://opencatalystproject.org/
- **Jenis:** Benchmark+source
- **Bidang:** AI for materials, catalysis
- **Yang dicari:** Dataset OC20/OC22, baseline ML, open-source code, leaderboard dan paper.
- **Cara pakai:** Buka dataset paper, lalu GitHub baseline dan dokumentasi metrik eksperimen.
- **Catatan:** Dataset besar, memerlukan compute/storage tinggi.

#### [184] Matbench
- **URL:** https://github.com/materialsproject/matbench
- **Jenis:** Benchmark source code
- **Bidang:** ML for materials
- **Yang dicari:** Tugas prediksi properti bahan, kode dataset loader, benchmark dan paper.
- **Cara pakai:** Buka source/documentation, jalankan baseline dan bandingkan leaderboard.
- **Catatan:** Fokus sifat material; split dan metrik harus mengikuti benchmark.

### T. Benchmark, Dataset, Dan Implementasi Risetpaper

#### [190] MLCommons DataPerf
- **URL:** https://github.com/mlcommons/dataperf
- **Jenis:** Benchmark kode
- **Bidang:** Data-centric machine learning
- **Yang dicari:** Task benchmark, kode baseline dan evaluasi pengembangan dataset.
- **Cara pakai:** Buka challenge atau paper DataPerf; jalankan reference baseline dan evaluator.
- **Catatan:** Implementasi spesifik challenge, bukan source code paper untuk semua bidang.

#### [192] Monash Time Series Forecasting Archive
- **URL:** https://forecastingdata.org/
- **Jenis:** Benchmark forecasting
- **Bidang:** Forecasting, time series
- **Yang dicari:** Dataset forecasting, kode pembaca R/Python, baseline, evaluasi dan paper NeurIPS terkait.
- **Cara pakai:** Buka tab Results atau Software/GitHub pada situs resminya; cocokkan horizon dan metrik.
- **Catatan:** Kekuatan utamanya dataset dan metadata, bukan semua script model paper.

#### [197] Numenta Anomaly Benchmark (NAB)
- **URL:** https://github.com/numenta/NAB
- **Jenis:** Benchmark + source
- **Bidang:** Time-series anomaly detection
- **Yang dicari:** Dataset deret waktu berlabel, scoring, runner, baseline, publikasi terkait.
- **Cara pakai:** Klon repository, jalankan evaluasi detector dan bandingkan skor dengan paper.
- **Catatan:** Versi lama; perlu penyesuaian lingkungan Python dan metrik benchmark.

#### [200] TimeEval Research Benchmark
- **URL:** https://github.com/TimeEval/TimeEval
- **Jenis:** Benchmark reproducibility
- **Bidang:** Time-series anomaly detection
- **Yang dicari:** Toolkit evaluasi, ratusan dataset, algoritma containerized dan link paper PVLDB.
- **Cara pakai:** Gunakan TimeEval algorithms/benchmark manager; replikasi protokol dalam paper.
- **Catatan:** Docker dan Linux/WSL dapat diperlukan; cek versi runtime.


<a id="06-agents"></a>
## Untuk AI Agent & Otomasi — 9 sumber

Endpoint API dan metadata terstruktur untuk pencarian otomatis.

### C. Mesin Pencari Paper Yang Dapat Ditelusuri Ke Kode

#### [043] OpenAlex
- **URL:** https://openalex.org/
- **Jenis:** Metadata/API
- **Bidang:** Lintas disiplin
- **Yang dicari:** Indeks paper, DOI, topik, institusi dan relasi sitasi.
- **Cara pakai:** Gunakan web/API untuk temukan karya, lalu enrich dengan GitHub/Zenodo.
- **Catatan:** Tidak khusus mengindeks repository kode secara lengkap.

### L. Knowledge Graph Paper-Ke-Repository

#### [121] Linked Papers With Code
- **URL:** https://linkedpaperswithcode.com/
- **Jenis:** Knowledge graph
- **Bidang:** Machine learning
- **Yang dicari:** Relasi paper, metode, dataset dan tautan kode dari data PWC.
- **Cara pakai:** Cari judul/metode, ikuti entri repo dan dataset.
- **Catatan:** Sebagian sumber bersifat historis; periksa tanggal refresh.

#### [122] SemRepo
- **URL:** https://semrepo.org/
- **Jenis:** Knowledge graph
- **Bidang:** Research software
- **Yang dicari:** Metadata repository ilmiah dan relasi publikasinya.
- **Cara pakai:** Cari repo/paper; eksplorasi graph, dependensi dan link code.
- **Catatan:** Perlu validasi cakupan serta pembaruan snapshot.

### O. Algoritma, Jurnal Software, Dan Reproducibility

#### [151] zbMATH Open (swMATH records)
- **URL:** https://zbmath.org/
- **Jenis:** Indeks software matematis
- **Bidang:** Matematika komputasional
- **Yang dicari:** Hubungan software matematika dengan sitasi dan literatur ilmiah.
- **Cara pakai:** Cari nama software atau algoritma; ikuti metadata dan referensi implementasi.
- **Catatan:** Indeks bibliografi; perlu menelusuri situs publisher atau repository terpisah.

### P. Repositori Akademik Dan Jaringan Data

#### [162] DataCite Commons
- **URL:** https://commons.datacite.org/
- **Jenis:** Pencarian DOI/metadata
- **Bidang:** Lintas disiplin
- **Yang dicari:** Relasi DOI antara publikasi, dataset, software dan contributor.
- **Cara pakai:** Cari judul/DOI paper; telusuri related identifiers terutama software/data.
- **Catatan:** Metadata bukan file kode; perlu mengunjungi repository tujuan.

#### [163] re3data
- **URL:** https://www.re3data.org/
- **Jenis:** Direktori repositori
- **Bidang:** Lintas disiplin
- **Yang dicari:** Katalog repository ilmiah dengan informasi tipe, akses, dan kebijakan.
- **Cara pakai:** Filter disiplin atau content type, temukan repository baru yang menerima software.
- **Catatan:** Direktori platform, bukan tempat unduh software langsung.

#### [164] FAIRsharing
- **URL:** https://fairsharing.org/
- **Jenis:** Registry data/standar
- **Bidang:** Life sciences, lintas disiplin
- **Yang dicari:** Database riset, metadata standar dan kebijakan repositori.
- **Cara pakai:** Cari bidang atau metode; pilih database terhubung lalu cek resources.
- **Catatan:** Biasanya tidak mengindeks source code paper secara langsung.

#### [165] DataLad Public Dataset Registry
- **URL:** https://github.com/datalad/datasets.datalad.org
- **Jenis:** Registry dataset berversi
- **Bidang:** Neuroinformatics dan ilmu komputasi
- **Yang dicari:** Koleksi dataset versioned dengan provenance dan pointer penyimpanan.
- **Cara pakai:** Cari dataset dan periksa README/data access; cocokkan dengan implementasi paper.
- **Catatan:** Fokus manajemen data; tidak semua dataset memiliki script publikasi.

### T. Benchmark, Dataset, Dan Implementasi Risetpaper

#### [199] Deep Graph Library (DGL) Examples
- **URL:** https://github.com/dmlc/dgl/tree/master/examples
- **Jenis:** Koleksi kode paper GNN
- **Bidang:** Graph ML, knowledge graphs
- **Yang dicari:** Contoh implementasi paper GNN termasuk traffic forecasting, link prediction dan node classification.
- **Cara pakai:** Cari daftar Official DGL Examples; buka paper link dan jalankan contoh terkait.
- **Catatan:** DGL menandai beberapa example kompatibel hanya dengan versi tertentu.
