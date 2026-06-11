# Catatan Presentasi Final

## Slide 1 — Judul

Project ini berjudul **Analisis Komputasional Topik Pidato Presiden Prabowo pada Forum Nasional dan Internasional Menggunakan Manual Coding dan BERTopic**.

Fokus utama project adalah membandingkan hasil analisis topik secara manual dengan hasil topic modeling otomatis menggunakan BERTopic.

## Slide 2 — Latar Belakang

Pidato politik dan kenegaraan memiliki banyak pesan strategis, seperti isu kedaulatan, pembangunan manusia, diplomasi, pangan, energi, pendidikan, dan tata kelola. Karena itu, diperlukan pendekatan analisis yang mampu menangkap tema secara sistematis.

## Slide 3 — Metodologi

Project ini mengikuti alur CRISP-DM secara sederhana:

1. Data understanding melalui inventory naskah pidato.
2. Data preparation melalui cleaning dan chunking.
3. Modeling melalui Manual Coding dan BERTopic.
4. Evaluation melalui comparative analysis.
5. Reporting melalui visualisasi dan interpretasi akhir.

## Slide 4 — Dataset

Dataset terdiri dari naskah pidato Presiden Prabowo pada forum nasional dan internasional. Setelah preprocessing dan chunking, data dianalisis pada level chunk agar unit analisis lebih konsisten.

Total chunk manual: 74.  
Chunk yang digunakan BERTopic: 71.  
Chunk yang dikeluarkan: 3.

## Slide 5 — Manual Coding

Manual Coding dilakukan dengan tiga tahap:

1. Open Coding untuk memberi label awal pada chunk.
2. Axial Coding untuk mengelompokkan kode ke kategori.
3. Selective Coding untuk menentukan tema utama.

Tema manual paling dominan adalah **Pembangunan manusia dan keadilan sosial** dengan 24 chunk.

## Slide 6 — BERTopic

BERTopic digunakan untuk menemukan topik otomatis berbasis embedding dan clustering. Model menghasilkan 15 label topik termasuk outlier, dengan 14 topik non-outlier.

Topik terbesar adalah Topic 0, dengan 13 chunk, dan dominan berkaitan dengan tema **Kedaulatan dan kemandirian nasional**.

## Slide 7 — Comparative Analysis

Perbandingan dilakukan antara manual_selective_theme dan bertopic_topic_id. Metrik yang digunakan adalah NMI, AMI, Homogeneity, Completeness, dan V-measure.

Nilai NMI=0.334, AMI=0.1263, Homogeneity=0.45, Completeness=0.2656, dan V-measure=0.334.

Metrik ini tidak dibaca sebagai accuracy, tetapi sebagai indikasi hubungan antara struktur tema manual dan cluster BERTopic.

## Slide 8 — Temuan Utama

- **Jumlah data analisis final**: Manual Coding mencakup 74 chunk, dengan 71 chunk berstatus REVIEWED dan 3 chunk berstatus EXCLUDED. BERTopic dijalankan pada 71 chunk substantif.
- **Tema manual paling dominan**: Tema manual paling dominan adalah 'Pembangunan manusia dan keadilan sosial' dengan 24 chunk.
- **Jumlah topik BERTopic**: BERTopic menghasilkan 15 label topik termasuk outlier. Jumlah topik non-outlier adalah 14, sedangkan jumlah dokumen pada topik outlier -1 adalah 2.
- **Topik BERTopic terbesar**: Topik BERTopic terbesar adalah Topic 0 dengan 13 chunk dan dominan berkaitan dengan tema manual 'Kedaulatan dan kemandirian nasional'.
- **Tema dengan alignment terkuat**: Alignment terkuat muncul pada tema manual 'Keberlanjutan lingkungan dan sumber daya' dengan dominant BERTopic Topic -1 dan theme concentration 0.5.
- **Kesesuaian Manual Coding dan BERTopic**: Metrik clustering menunjukkan NMI=0.334, AMI=0.1263, Homogeneity=0.45, Completeness=0.2656, dan V-measure=0.334. Nilai ini menunjukkan tingkat hubungan antara tema manual dan struktur topik BERTopic, bukan akurasi klasifikasi.

## Slide 9 — Interpretasi

Manual Coding lebih kuat dalam menangkap konteks substantif dan makna konseptual. BERTopic lebih kuat dalam menemukan pola kemiripan semantik secara otomatis. Perbedaan hasil keduanya wajar karena pendekatan manual dan komputasional bekerja dengan prinsip yang berbeda.

## Slide 10 — Kesimpulan

Kombinasi Manual Coding dan BERTopic memberikan hasil analisis topik yang lebih komprehensif. Manual Coding menyediakan validasi interpretatif, sedangkan BERTopic menyediakan pembanding komputasional. Pendekatan ini relevan untuk analisis teks pidato yang memiliki struktur topik kompleks.
