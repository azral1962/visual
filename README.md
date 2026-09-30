# visual

Proyek Quarto tentang **Visual dan Tabel sebagai Infrastruktur Argumen dalam Tulisan Akademik**, dengan TISE dan Q-Cycle sebagai kerangka penjelasan. Proyek memuat 15 tabel, delapan visual, data sintetis, dan kode pembentuk visual untuk dipelajari serta dikembangkan.

Mulai dari `paper.html` untuk membaca hasil, `paper.qmd` untuk menyunting naskah, dan `generate_figures.py` untuk mengembangkan diagram serta plot. Petunjuk kontribusi ada di [CONTRIBUTING.md](CONTRIBUTING.md).

Draf paper konseptual berbahasa Indonesia, 30 September 2026. Penjelasan TISE mengacu pada naskah Armein Z. R. Langi, *Apa Itu TISE?*, 23 Agustus 2026. Atribusi penulis dan isi draf perlu ditinjau sebelum publikasi. Belum disesuaikan ke templat jurnal tertentu.

## Isi

- `paper.qmd`: naskah utama.
- `_quarto.yml`, `references.bib`, `styles.css`: konfigurasi dan rujukan.
- `figures/`: delapan figur, masing-masing PNG dan SVG.
- `data/`: tiga CSV sintetis dan ringkasan numerik JSON.
- `generate_figures.py`: membuat kembali seluruh figur dan data.
- `diagrams/`: contoh Mermaid dan DOT.
- `paper.html`: salinan baca mandiri dengan gambar tertanam.
- `build_preview.py`: pembentuk salinan HTML menggunakan Pandoc.
- `validation.json`: hasil pemeriksaan struktural dan numerik.
- `requirements.txt`: versi dependensi yang dipakai saat pembuatan.

## Menjalankan Quarto

Ekstrak seluruh ZIP sebelum menjalankan agar sumber dan gambar berada di tempat yang benar. Dari direktori proyek:

```bash
python -m pip install -r requirements.txt
python generate_figures.py
quarto render paper.qmd --to html
```

Render PDF opsional memerlukan Quarto dan distribusi TeX, misalnya TinyTeX:

```bash
quarto install tinytex
quarto render paper.qmd --to pdf
```

Figur PNG sudah tersedia; render naskah tidak memerlukan eksekusi ulang skrip Python. SVG disediakan untuk ekspor vektor atau penyuntingan. Mermaid dan DOT dalam paper adalah cuplikan bahasa, bukan blok eksekusi; padanan diagram utama sudah ditampilkan sebagai figur. Pengguna yang menginginkan diagram native dapat mengubah pagar menjadi `{mermaid}` atau `{dot}` sesuai dokumentasi Quarto.

## Salinan baca HTML

`paper.html` dibuat dengan Pandoc 3.1.3, bukan mesin Quarto. Skrip hanya menerjemahkan rujukan silang Quarto menjadi nomor dan tautan, lalu merender sitasi dan menanam gambar. Bila sumber diubah, jalankan kembali `python build_preview.py` atau langsung gunakan Quarto. Pandoc tidak diperlukan untuk render Quarto.

Quarto CLI tidak tersedia pada lingkungan pembuatan. Karena itu, render HTML/PDF melalui Quarto belum diuji; pemeriksaan dilakukan atas struktur QMD, YAML, label, sumber sitasi, keberadaan aset, angka, dan keluaran HTML Pandoc. Tidak ada PDF yang diklaim telah dirender.

## Status ilmiah

Ini paper konseptual dan metodologis, bukan systematic review, bukan laporan uji pengguna, dan bukan bukti empiris efektivitas TISE. Semua angka demonstrasi ditentukan secara sintetis; kurva adaptif lebih cepat karena konstanta waktunya dipilih lebih kecil. Label target layanan kampus merupakan spesifikasi ilustratif.

Rujukan TISE adalah naskah pengantar pribadi penulis; URL, DOI, atau status penelaahan sejawat tidak diciptakan. Dokumen sumber tersebut tidak disertakan ulang. Literatur eksternal dan dokumentasi resmi diperiksa pada 30 September 2026.

## Reproduksi data

Tidak ada generator acak pada contoh. Dua distribusi dibentuk dari vektor eksplisit dan dinormalisasi ke rerata 50 serta SD sampel 10; pasangan waktu memakai nilai eksplisit; kurva pemulihan mengikuti fungsi eksponensial dengan parameter terdokumentasi. Ini menjaga kesesuaian nilai tabel dengan plot.
