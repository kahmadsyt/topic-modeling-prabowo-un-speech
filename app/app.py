from pathlib import Path

import pandas as pd
import streamlit as st

from utils import (
    load_csv,
    load_markdown,
    render_dataframe_section,
    render_html_figure,
    render_metric_from_df,
    render_missing_file_warning,
    render_png_image,
    make_download_button_for_dataframe,
    shorten_text,
)


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Topic Modeling Pidato Prabowo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# File Paths
# ============================================================

PATHS = {
    "final_key_findings": "reports/tables/final_key_findings.csv",
    "final_manual_theme_summary": "reports/tables/final_manual_theme_summary.csv",
    "final_bertopic_topic_summary": "reports/tables/final_bertopic_topic_summary.csv",
    "final_comparative_interpretation": "reports/tables/final_comparative_interpretation.csv",
    "final_representative_evidence": "reports/tables/final_representative_evidence.csv",
    "comparative_metrics_summary": "reports/tables/comparative_metrics_summary.csv",
    "comparative_analysis": "data/processed/comparative_analysis_manual_vs_bertopic.csv",
    "final_report_summary_md": "reports/final_report_summary.md",
    "final_presentation_notes_md": "reports/final_presentation_notes.md",

    "fig_manual_theme_distribution": "reports/figures/final_manual_theme_distribution.html",
    "fig_bertopic_topic_distribution": "reports/figures/final_bertopic_topic_distribution.html",
    "fig_topic_purity": "reports/figures/final_topic_purity_bar.html",
    "fig_comparative_heatmap": "reports/figures/final_comparative_heatmap.html",
    "fig_alignment": "reports/figures/final_manual_theme_topic_alignment.html",

    "wordcloud_all": "reports/figures/final_wordcloud_all_corpus.png",
}


# ============================================================
# Data Loading
# ============================================================

final_key_findings_df = load_csv(PATHS["final_key_findings"])
final_manual_theme_summary_df = load_csv(PATHS["final_manual_theme_summary"])
final_bertopic_topic_summary_df = load_csv(PATHS["final_bertopic_topic_summary"])
final_comparative_interpretation_df = load_csv(PATHS["final_comparative_interpretation"])
final_representative_evidence_df = load_csv(PATHS["final_representative_evidence"])
comparative_metrics_df = load_csv(PATHS["comparative_metrics_summary"])
comparative_analysis_df = load_csv(PATHS["comparative_analysis"])

final_report_summary_md = load_markdown(PATHS["final_report_summary_md"])
final_presentation_notes_md = load_markdown(PATHS["final_presentation_notes_md"])


# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("📊 Topic Modeling Dashboard")
st.sidebar.caption("Manual Coding vs BERTopic")

menu = st.sidebar.radio(
    "Navigasi",
    [
        "Project Overview",
        "Dataset & Metrics",
        "Manual Coding Result",
        "BERTopic Result",
        "Comparative Analysis",
        "WordCloud",
        "Representative Evidence",
        "Final Report Notes",
    ]
)

st.sidebar.divider()
st.sidebar.markdown("**Project Stage**")
st.sidebar.success("Tahap 08B — Streamlit Dashboard Lokal")

st.sidebar.markdown("**Input utama dashboard**")
st.sidebar.code("reports/tables/\nreports/figures/\ndata/processed/")


# ============================================================
# Header
# ============================================================

st.title("Analisis Topik Pidato Presiden Prabowo")
st.markdown(
    """
    Dashboard ini menampilkan hasil akhir project Data Mining berbasis **Manual Coding**
    dan **BERTopic**. Dashboard membaca output final dari notebook Tahap 07, sehingga
    tidak melakukan training ulang model.
    """
)


# ============================================================
# Page 1 — Project Overview
# ============================================================

if menu == "Project Overview":
    st.header("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if final_manual_theme_summary_df is not None:
            st.metric("Manual Themes", final_manual_theme_summary_df.shape[0])
        else:
            st.metric("Manual Themes", "-")

    with col2:
        if final_bertopic_topic_summary_df is not None:
            st.metric("BERTopic Topics", final_bertopic_topic_summary_df.shape[0])
        else:
            st.metric("BERTopic Topics", "-")

    with col3:
        if comparative_analysis_df is not None:
            st.metric("Chunk Komparatif", comparative_analysis_df.shape[0])
        else:
            st.metric("Chunk Komparatif", "-")

    with col4:
        render_metric_from_df(comparative_metrics_df, "V-measure", "v_measure")

    st.subheader("Deskripsi Singkat")
    st.markdown(
        """
        Project ini bertujuan untuk menganalisis topik pidato Presiden Prabowo pada
        forum nasional dan internasional. Pendekatan yang digunakan terdiri dari:

        1. **Manual Coding** melalui Open Coding, Axial Coding, dan Selective Coding.
        2. **BERTopic** sebagai pendekatan topic modeling komputasional.
        3. **Comparative Analysis** untuk membandingkan hasil manual dan hasil komputasional.
        """
    )

    st.subheader("Temuan Kunci")
    if final_key_findings_df is None:
        render_missing_file_warning(PATHS["final_key_findings"])
    else:
        for _, row in final_key_findings_df.iterrows():
            title = row.get("finding_title", "Finding")
            description = row.get("finding_description", "")
            with st.expander(f"{row.get('finding_id', '')} — {title}", expanded=False):
                st.write(description)


# ============================================================
# Page 2 — Dataset & Metrics
# ============================================================

elif menu == "Dataset & Metrics":
    st.header("Dataset & Metrics")

    st.subheader("Metrik Perbandingan")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        render_metric_from_df(comparative_metrics_df, "NMI", "normalized_mutual_information")
    with col2:
        render_metric_from_df(comparative_metrics_df, "AMI", "adjusted_mutual_information")
    with col3:
        render_metric_from_df(comparative_metrics_df, "Homogeneity", "homogeneity")
    with col4:
        render_metric_from_df(comparative_metrics_df, "Completeness", "completeness")
    with col5:
        render_metric_from_df(comparative_metrics_df, "V-measure", "v_measure")

    render_dataframe_section(
        "Comparative Metrics Summary",
        comparative_metrics_df,
        PATHS["comparative_metrics_summary"],
        height=260
    )

    render_dataframe_section(
        "Comparative Analysis Dataset",
        comparative_analysis_df,
        PATHS["comparative_analysis"],
        height=420
    )


# ============================================================
# Page 3 — Manual Coding Result
# ============================================================

elif menu == "Manual Coding Result":
    st.header("Manual Coding Result")

    st.markdown(
        """
        Halaman ini menampilkan ringkasan hasil Manual Coding pada level
        **Selective Theme**.
        """
    )

    render_html_figure(PATHS["fig_manual_theme_distribution"], height=560)

    render_dataframe_section(
        "Final Manual Theme Summary",
        final_manual_theme_summary_df,
        PATHS["final_manual_theme_summary"],
        height=360
    )

    make_download_button_for_dataframe(
        final_manual_theme_summary_df,
        "final_manual_theme_summary.csv",
        "Download Manual Theme Summary"
    )


# ============================================================
# Page 4 — BERTopic Result
# ============================================================

elif menu == "BERTopic Result":
    st.header("BERTopic Result")

    st.markdown(
        """
        Halaman ini menampilkan distribusi topik yang dihasilkan oleh BERTopic dan
        hubungan setiap topik dengan tema manual dominan.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribusi Topic")
        render_html_figure(PATHS["fig_bertopic_topic_distribution"], height=520)

    with col2:
        st.subheader("Topic Purity")
        render_html_figure(PATHS["fig_topic_purity"], height=520)

    render_dataframe_section(
        "Final BERTopic Topic Summary",
        final_bertopic_topic_summary_df,
        PATHS["final_bertopic_topic_summary"],
        height=420
    )

    make_download_button_for_dataframe(
        final_bertopic_topic_summary_df,
        "final_bertopic_topic_summary.csv",
        "Download BERTopic Topic Summary"
    )


# ============================================================
# Page 5 — Comparative Analysis
# ============================================================

elif menu == "Comparative Analysis":
    st.header("Comparative Analysis")

    st.markdown(
        """
        Halaman ini memperlihatkan hubungan antara tema hasil Manual Coding dan
        topik hasil BERTopic. Heatmap menunjukkan jumlah chunk pada setiap kombinasi
        tema manual dan topik BERTopic.
        """
    )

    st.subheader("Heatmap Manual Theme vs BERTopic Topic")
    render_html_figure(PATHS["fig_comparative_heatmap"], height=680)

    st.subheader("Alignment Manual Theme ke BERTopic Topic")
    render_html_figure(PATHS["fig_alignment"], height=560)

    render_dataframe_section(
        "Final Comparative Interpretation",
        final_comparative_interpretation_df,
        PATHS["final_comparative_interpretation"],
        height=420
    )

    make_download_button_for_dataframe(
        final_comparative_interpretation_df,
        "final_comparative_interpretation.csv",
        "Download Comparative Interpretation"
    )


# ============================================================
# Page 6 — WordCloud
# ============================================================

elif menu == "WordCloud":
    st.header("WordCloud Visualization")

    st.markdown(
        """
        WordCloud digunakan sebagai visualisasi eksploratif untuk memperlihatkan
        kata-kata dominan dalam korpus pidato. Visualisasi ini bukan metrik evaluasi
        utama, tetapi berguna untuk presentasi dan interpretasi awal.
        """
    )

    st.subheader("WordCloud Seluruh Korpus")
    render_png_image(
        PATHS["wordcloud_all"],
        caption="WordCloud seluruh korpus pidato"
    )

    st.divider()
    st.subheader("WordCloud Manual Theme dan BERTopic Topic")

    st.info(
        "Jika Bapak sudah membuat WordCloud per tema atau per topic, file PNG akan tetap "
        "tersimpan di reports/figures/. Untuk tampilan Streamlit awal, dashboard ini "
        "menampilkan WordCloud seluruh korpus sebagai visual utama."
    )


# ============================================================
# Page 7 — Representative Evidence
# ============================================================

elif menu == "Representative Evidence":
    st.header("Representative Evidence")

    st.markdown(
        """
        Tabel ini menampilkan potongan teks representatif untuk mendukung interpretasi
        topik. Evidence membantu menjelaskan bahwa hasil numerik tetap memiliki dasar
        pada teks asli.
        """
    )

    if final_representative_evidence_df is None:
        render_missing_file_warning(PATHS["final_representative_evidence"])
    else:
        topic_options = ["Semua Topic"] + sorted(
            final_representative_evidence_df["bertopic_topic_id"].astype(str).unique().tolist()
        )

        selected_topic = st.selectbox("Filter BERTopic Topic", topic_options)

        filtered_evidence_df = final_representative_evidence_df.copy()

        if selected_topic != "Semua Topic":
            filtered_evidence_df = filtered_evidence_df[
                filtered_evidence_df["bertopic_topic_id"].astype(str) == selected_topic
            ]

        st.dataframe(filtered_evidence_df, use_container_width=True, height=520)

        st.subheader("Evidence Preview")
        for _, row in filtered_evidence_df.head(5).iterrows():
            topic_id = row.get("bertopic_topic_id", "-")
            manual_theme = row.get("manual_selective_theme", "-")
            text_excerpt = row.get("text_excerpt", row.get("text", ""))

            with st.expander(f"Topic {topic_id} — {manual_theme}", expanded=False):
                st.write(shorten_text(text_excerpt, max_chars=900))


# ============================================================
# Page 8 — Final Report Notes
# ============================================================

elif menu == "Final Report Notes":
    st.header("Final Report Notes")

    tab1, tab2 = st.tabs(["Final Report Summary", "Presentation Notes"])

    with tab1:
        if final_report_summary_md is None:
            render_missing_file_warning(PATHS["final_report_summary_md"])
        else:
            st.markdown(final_report_summary_md)

    with tab2:
        if final_presentation_notes_md is None:
            render_missing_file_warning(PATHS["final_presentation_notes_md"])
        else:
            st.markdown(final_presentation_notes_md)


# ============================================================
# Footer
# ============================================================

st.divider()
st.caption(
    "Dashboard Streamlit ini membaca output final dari notebook Tahap 07 dan tidak melakukan training ulang model."
)
