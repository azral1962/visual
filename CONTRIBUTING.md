# Mengembangkan proyek visual

## Alur kerja

1. Buat branch untuk perubahan yang ingin dilakukan.
2. Sunting `paper.qmd` untuk isi, caption, atau tabel; sunting `generate_figures.py` untuk diagram dan plot.
3. Jalankan `python generate_figures.py` bila figur atau data diubah.
4. Jalankan `quarto render paper.qmd --to html` dari direktori proyek untuk membuat keluaran naskah.
5. Periksa gambar pada ukuran baca akhir, tabel, sitasi, dan rujukan silang sebelum mengajukan pull request.

## Prinsip isi

- Pertahankan identitas label `fig-...` dan `tbl-...` ketika memindahkan representasi.
- Definisikan satuan, jenis hubungan, sumber data, dan arti ketidakpastian.
- Bedakan data sintetis, simulasi, dan pengukuran nyata secara eksplisit.
- Jangan mengubah data sumber hanya untuk memperindah pola hasil.
- Hubungkan kebutuhan Q1, fungsi Q2, arsitektur Q3, dan bukti Q4.
- Tambahkan sumber primer untuk klaim baru dan metadata rujukannya ke `references.bib`.
- Pastikan kode, angka tabel, serta figur tetap konsisten; sertakan keterbatasan hasil.

## Usulan pengembangan

- Menambah contoh visual dari bidang penelitian lain.
- Menambah diagram Mermaid atau Graphviz yang dieksekusi langsung oleh Quarto.
- Menguji keterbacaan pada layar ponsel dan versi cetak.
- Menyiapkan template jurnal dan versi bahasa Inggris.
- Melakukan eksperimen pembaca untuk mengevaluasi proposisi konseptual artikel.

Deskripsikan tujuan perubahan, berkas yang terpengaruh, dan pemeriksaan yang dilakukan dalam pull request. Untuk revisi angka atau bukti, jelaskan sumber serta metode perhitungannya.
