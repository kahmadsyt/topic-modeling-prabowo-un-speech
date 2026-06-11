# Analisis Komputasional Topik Pidato Presiden Prabowo pada Forum Nasional dan Internasional Menggunakan Manual Coding dan BERTopic

## Project Overview

This project analyzes the main topics in President Prabowo's speech at the 80th Session of the United Nations General Assembly.

The analysis combines two approaches:

1. Manual Analysis using open coding, axial coding, and selective coding.
2. Automated Topic Modeling using BERTopic.

This project was developed as part of a Data Mining course in the Master of Informatics Engineering program.

## Objectives

The objectives of this project are:

- To prepare a single long-form speech text into analyzable text chunks.
- To identify major themes using manual qualitative analysis.
- To perform automated topic modeling using BERTopic.
- To compare manual and automated topic analysis results.
- To present the findings through a Streamlit dashboard.

## Dataset

The dataset consists of the speech transcript titled:

"Sesi Debat Umum Sidang Majelis Umum Ke-80 Perserikatan Bangsa-Bangsa"

The speech text is in English. The interpretation and academic discussion are written in Indonesian.

## Methods

The project workflow includes:

1. Text input and data preparation
2. Light text cleaning
3. Sentence splitting
4. Text chunking every 3 sentences
5. Manual topic analysis
6. BERTopic modeling
7. Topic comparison and interpretation
8. Streamlit dashboard deployment

## Tools and Libraries

- Python
- Jupyter Notebook
- Pandas
- BERTopic
- Sentence Transformers
- UMAP
- HDBSCAN
- Plotly
- Streamlit

## Project Structure

```text
app/             Streamlit application
data/            Raw, processed, and final datasets
notebooks/       Jupyter notebooks for each analysis stage
assets/          Images and charts
reports/         Final report and supporting figures
```

## Expected Outputs

The project produces:

- Speech chunk dataset
- Manual analysis results
- BERTopic topic modeling results
- Comparison between manual and automated analysis
- Interactive Streamlit dashboard

## Author

Achmad Kamil  
Master of Informatics Engineering  
Data Science Interest

## License and Attribution

The source code in this repository is released under the MIT License.

The speech transcript is used for academic and educational purposes. All rights related to the original speech content belong to the respective official source.
