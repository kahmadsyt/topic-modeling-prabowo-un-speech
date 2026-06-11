# Analisis Komputasional Topik Pidato Presiden Prabowo Menggunakan Manual Coding dan BERTopic

## 1. Deskripsi Project

Project ini merupakan tugas mata kuliah **Data Mining** pada Program Magister Teknik Informatika dengan peminatan Data Science. Project ini bertujuan untuk menganalisis topik utama dalam naskah pidato Presiden Prabowo pada forum nasional dan internasional menggunakan dua pendekatan, yaitu **Manual Coding** dan **BERTopic**.

Manual Coding digunakan untuk memahami tema pidato secara interpretatif melalui tahapan **Open Coding, Axial Coding, dan Selective Coding**. Sementara itu, BERTopic digunakan sebagai pendekatan komputasional berbasis embedding dan clustering untuk menemukan topik secara otomatis.

Hasil dari kedua pendekatan kemudian dibandingkan untuk melihat kesesuaian antara interpretasi manual dan hasil topic modeling otomatis.

## 2. Tujuan Project

Tujuan utama project ini adalah:

1. Mengumpulkan dan mendokumentasikan naskah pidato Presiden Prabowo dari beberapa forum nasional dan internasional.
2. Melakukan preprocessing teks agar data siap dianalisis.
3. Membagi teks pidato menjadi chunk sebagai unit analisis.
4. Melakukan Manual Coding menggunakan Open Coding, Axial Coding, dan Selective Coding.
5. Menerapkan BERTopic untuk menemukan topik secara otomatis.
6. Membandingkan hasil Manual Coding dan BERTopic.
7. Menyusun visualisasi dan laporan akhir sebagai bahan presentasi akademik.

## 3. Dataset

Dataset yang digunakan berupa naskah pidato Presiden Prabowo dalam format teks. Dataset mencakup pidato pada beberapa konteks, seperti forum nasional, forum internasional, isu pangan, energi, pendidikan, ekonomi, dan diplomasi.

Data mentah disimpan pada folder:

```text
data/raw/
```

Data hasil preprocessing dan modeling disimpan pada folder:

```text
data/processed/
```

Output tabel analisis disimpan pada folder:

```text
reports/tables/
```

Output visualisasi disimpan pada folder:

```text
reports/figures/
```

## 4. Metodologi

Project ini mengikuti alur kerja Data Mining berbasis CRISP-DM secara sederhana:

### 4.1 Business Understanding

Permasalahan utama dalam project ini adalah bagaimana mengidentifikasi topik dominan dari kumpulan pidato secara sistematis, baik melalui pendekatan manual maupun pendekatan komputasional.

### 4.2 Data Understanding

Tahap ini dilakukan dengan melakukan inventory data, membaca file naskah pidato, mengekstrak metadata, dan memvalidasi struktur data awal.

### 4.3 Data Preparation

Tahap ini mencakup text cleaning, preprocessing, normalisasi teks, dan text chunking agar naskah pidato dapat dianalisis pada unit teks yang lebih kecil.

### 4.4 Modeling

Modeling dilakukan dengan dua pendekatan:

1. Manual Coding:

   * Open Coding
   * Axial Coding
   * Selective Coding

2. BERTopic:

   * Sentence embedding
   * Dimensionality reduction
   * Clustering
   * Topic representation

### 4.5 Evaluation

Evaluasi dilakukan dengan membandingkan hasil Manual Coding dan BERTopic menggunakan tabulasi silang dan metrik clustering seperti:

* Normalized Mutual Information
* Adjusted Mutual Information
* Homogeneity
* Completeness
* V-measure

### 4.6 Reporting

Tahap akhir dilakukan dengan membuat tabel final, visualisasi, WordCloud, ringkasan temuan, dan catatan presentasi.

## 5. Alur Notebook

| Tahap | Notebook                                                | Deskripsi                                                |
| ----- | ------------------------------------------------------- | -------------------------------------------------------- |
| 01    | `01_data_inventory_metadata.ipynb`                      | Inventory data dan metadata pidato                       |
| 02    | `02_text_cleaning_preprocessing.ipynb`                  | Text cleaning dan preprocessing                          |
| 03    | `03_text_chunking.ipynb`                                | Text chunking untuk Manual Coding dan BERTopic           |
| 04    | `04_manual_coding_open_axial_selective.ipynb`           | Manual Coding berbasis Open, Axial, dan Selective Coding |
| 05    | `05_bertopic_modeling.ipynb`                            | Topic modeling menggunakan BERTopic                      |
| 06    | `06_comparative_analysis_manual_vs_bertopic.ipynb`      | Perbandingan Manual Coding dan BERTopic                  |
| 07    | `07_visualization_interpretation_final_reporting.ipynb` | Visualisasi, interpretasi, WordCloud, dan laporan akhir  |

## 6. Output Utama

Beberapa output utama dari project ini adalah:

```text
data/processed/manual_coding_final.csv
data/processed/bertopic_document_topics_with_manual_reference.csv
data/processed/comparative_analysis_manual_vs_bertopic.csv
reports/tables/final_key_findings.csv
reports/tables/final_manual_theme_summary.csv
reports/tables/final_bertopic_topic_summary.csv
reports/tables/final_comparative_interpretation.csv
reports/final_report_summary.md
reports/final_presentation_notes.md
```

Visualisasi utama disimpan dalam folder:

```text
reports/figures/
```

## 7. Hasil Ringkas

Hasil akhir menunjukkan bahwa Manual Coding dan BERTopic dapat digunakan secara saling melengkapi. Manual Coding memberikan pemahaman konseptual terhadap tema pidato, sedangkan BERTopic memberikan pembanding komputasional berbasis pola semantik dalam teks.

Perbedaan antara hasil manual dan hasil BERTopic merupakan hal yang wajar karena Manual Coding berfokus pada interpretasi makna, sedangkan BERTopic berfokus pada kemiripan representasi teks dan distribusi kata kunci.

## 8. Cara Menjalankan Project

### 8.1 Clone Repository

```bash
git clone <URL_REPOSITORY>
cd topic-modeling-prabowo-un-speech
```

### 8.2 Buat Environment

```bash
conda create -n topic-mining python=3.10 -y
conda activate topic-mining
```

### 8.3 Install Dependency

```bash
pip install -r requirements.txt
```

### 8.4 Jalankan Notebook

Jalankan notebook secara berurutan dari Tahap 01 sampai Tahap 07:

```text
notebooks/01_data_inventory_metadata.ipynb
notebooks/02_text_cleaning_preprocessing.ipynb
notebooks/03_text_chunking.ipynb
notebooks/04_manual_coding_open_axial_selective.ipynb
notebooks/05_bertopic_modeling.ipynb
notebooks/06_comparative_analysis_manual_vs_bertopic.ipynb
notebooks/07_visualization_interpretation_final_reporting.ipynb
```

## 9. Rencana Streamlit Dashboard

Tahap berikutnya adalah membuat dashboard Streamlit untuk menampilkan:

1. Ringkasan project
2. Dataset dan chunk summary
3. Hasil Manual Coding
4. Hasil BERTopic
5. Comparative Analysis
6. WordCloud
7. Key Findings dan kesimpulan

File Streamlit akan disimpan pada folder:

```text
app/
```

## 10. Keterbatasan Project

Beberapa keterbatasan project ini adalah:

1. Jumlah pidato yang dianalisis masih terbatas.
2. BERTopic dijalankan pada jumlah chunk yang relatif kecil, sehingga hasil topik perlu ditafsirkan secara hati-hati.
3. Manual Coding dilakukan oleh satu coder, sehingga reliabilitas antar-coder belum diuji.
4. WordCloud digunakan sebagai visualisasi eksploratif, bukan sebagai metrik evaluasi utama.
5. Hasil interpretasi tetap bergantung pada konteks pidato dan proses pembacaan manual.

## 11. Kesimpulan

Project ini menunjukkan bahwa kombinasi Manual Coding dan BERTopic dapat memberikan analisis topik yang lebih komprehensif. Manual Coding membantu memahami konteks dan makna substantif pidato, sedangkan BERTopic membantu menemukan pola topik secara komputasional. Perbandingan keduanya memberikan dasar yang lebih kuat untuk interpretasi hasil dalam konteks Data Mining dan Natural Language Processing.