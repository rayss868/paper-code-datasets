# Berkontribusi

Terima kasih mau menambah atau memperbaiki. Karena repo ini dipakai sebagai
data terstruktur (bukan cuma dibaca), formatnya ketat.

## Dua cara berkontribusi

### 1. Sumber baru / koreksi tautan

Edit [`data/sources.json`](data/sources.json) — **jangan** edit `DIRECTORY.md`
langsung; berkas itu di-generate dari JSON.

Tambahkan entri dengan `id` berikutnya yang belum terpakai:

```json
{
  "id": 201,
  "name": "Nama Sumber",
  "url": "https://contoh.org/",
  "stage": "02-find-code",
  "jenis": "Jurnal software",
  "bidang": "Machine learning",
  "yang_dicari": "Benda konkret yang bisa ditemukan di sana.",
  "cara_pakai": "Langkah praktis memakainya.",
  "catatan": "Batasan yang jangan diabaikan.",
  "section": "A"
}
```

Aturan field:

- **`stage`** — salah satu dari `01-discover`, `02-find-code`, `03-datasets`,
  `04-reproduce`, `06-agents`. Pilih berdasarkan *pertanyaan apa yang dijawab*
  sumber tersebut, bukan bidangnya.
- **`jenis`** — kategori singkat (lihat entri lain sebagai contoh).
- **`bidang`** — bidang yang paling umum; bukan batasan mutlak.
- **`yang_dicari`** — harus **konkret**. "Banyak hal berguna" bukan jawaban.
- **`cara_pakai`** — langkah praktis, bukan deskripsi umum.
- **`catatan`** — batasan jujur. Jangan dikosongkan; tulis apa yang bisa
  mengecewakan pemakai.
- **`section`** — huruf kelompok asal (A–T), untuk jejak.

### 2. Perbaiki status tautan

Jalankan audit, lalu kirim PR dengan hasilnya:

```bash
python3 scripts/audit_links.py
git diff data/sources.json audit/liveness.md
```

## Yang tidak diterima

- **Link yang tidak pernah kamu buka.** Cek dulu; kalau `bot_walled`, sebutkan
  di deskripsi PR bahwa kamu memverifikasinya di browser.
- **Entri tanpa `catatan`.** Semua sumber punya batasan — tulis.
- **Klaim kuantitatif tanpa sumber.** Kalau menyebut angka, sertakan di mana
  kamu mendapatkannya, atau tandai jelas sebagai belum terverifikasi.
- **Duplikat.** Cek dulu apakah URL-nya sudah ada di `sources.json`.
- **Perubahan pada `DIRECTORY.md` / `audit/liveness.md` secara manual** — dua
  berkas itu di-generate.

## Format PR

```
Tambah: [nama sumber]
Stage:  [01-discover | 02-find-code | 03-datasets | 04-reproduce | 06-agents]
Sudah dibuka di browser: [ya/tidak]
Catatan: [kenapa sumber ini berguna / kenapa statusnya begini]
```

## Menjalankan audit lokal

```bash
python3 scripts/audit_links.py --workers 24 --timeout 15
```

Tidak butuh dependensi eksternal — hanya pustaka standar Python 3.10+.

Gunakan `bot_walled` sebagai **informasi**, bukan alasan menandai sumber mati:
403 dari script hampir selalu berarti situsnya normal di browser.

## Pelaporan masalah

Kalau menemukan tautan mati, entri salah klasifikasi, atau klaim yang tidak
akurat, buka issue. Sertakan:

- nomor entri dan URL,
- apa yang kamu lihat vs. apa yang seharusnya,
- tanggal pengecekan.
