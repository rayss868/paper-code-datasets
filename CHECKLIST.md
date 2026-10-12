# Checklist — menilai repository penelitian sebelum dipakai

Isi checklist ini untuk **setiap** repository yang akan kamu jadikan basis.
Tujuannya memisahkan "ada kodenya" dari "bisa benar-benar dipakai dan
dipertanggungjawabkan".

## Identitas

- [ ] Judul paper, tahun, penulis, dan DOI/arXiv ID cocok.
- [ ] Ada tautan dari paper/penulis ke repository (wajib jika mengklaim
      *official implementation*).

## Lisensi & legal

- [ ] Lisensi kode jelas dan mengizinkan tujuan pemakaianmu.
- [ ] Lisensi dataset dan pembatasan privasi/etik sudah dibaca.
- [ ] Jika memakai pretrained weights, asal-usul dan lisensinya jelas.
- [ ] Kode tidak meminta API key rahasia secara tidak perlu.

## Instalasi & eksekusi

- [ ] Ada README dengan perintah instalasi dan eksekusi yang valid.
- [ ] Ada `requirements.txt`, `environment.yml`, lockfile, atau Dockerfile.
- [ ] Versi rilis/commit sesuai dengan eksperimen dalam publikasi.

## Data & eksperimen

- [ ] Dataset, split data, preprocessing, dan label diketahui.
- [ ] Hyperparameter, random seed, dan metrik evaluasi dijelaskan.
- [ ] Script training/inference/evaluation terpisah atau terdokumentasi.

## Verifikasi hasil

- [ ] Hasil bisa dibandingkan dengan tabel/gambar pada paper.
- [ ] Dependensi, model, dan data diperiksa sebelum dieksekusi.
- [ ] Keterbatasan reproduksi dan deviasi hasil dilaporkan.

## Sitasi

- [ ] Paper, kode, dataset, dan versi software disitasi dengan benar.

---

## Skor cepat (opsional)

Rubrik internal untuk membandingkan kandidat. **Ini bukan standar resmi
jurnal** — hanya alat bantu keputusan.

| Komponen | 0 (tidak ada) | 1 (parsial) | 2 (lengkap/terverifikasi) |
|---|---|---|---|
| Identitas paper | | | |
| Source code | | | |
| Instalasi | | | |
| Dataset | | | |
| Parameter | | | |
| Evaluasi | | | |
| Lisensi | | | |
| Reproducibility | | | |

**Maksimum 16 poin.**

Cara membaca skor:

- **13–16** — siap dijadikan baseline.
- **8–12** — bisa dipakai, tapi siapkan waktu untuk memperbaiki.
- **0–7** — anggap sebagai referensi ide saja, bukan basis kode.
