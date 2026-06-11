import pandas as pd
import plotly.express as px
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
    value_count_df,
)


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Dashboard Analisis Topik Pidato",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# Light Custom Styling
# ============================================================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    .small-caption {
        color: #6b7280;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True
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


# ============================================================
# Helper Functions for Visualization
# ============================================================

def apply_global_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Menerapkan filter sidebar pada dataset komparatif.
    """
    if df is None:
        return pd.DataFrame()

    filtered_df = df.copy()

    if selected_forum != "Semua" and "forum_scope_inferred" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["forum_scope_inferred"].astype(str) == selected_forum]

    if selected_theme != "Semua" and "manual_selective_theme_clean" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["manual_selective_theme_clean"].astype(str) == selected_theme]

    if selected_topic != "Semua" and "bertopic_topic_id" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["bertopic_topic_id"].astype(str) == selected_topic]

    return filtered_df


def plot_bar(df: pd.DataFrame, x: str, y: str, title: str, labels: dict, orientation: str = "v"):
    """
    Membuat bar chart Plotly.
    """
    if df is None or df.empty:
        st.info("Data belum tersedia untuk visualisasi ini.")
        return

    fig = px.bar(
        df,
        x=x,
        y=y,
        orientation=orientation,
        title=title,
        labels=labels,
        text=y
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        height=520,
        margin=dict(l=20, r=20, t=70, b=90),
        xaxis_tickangle=-30 if orientation == "v" else 0
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_pie(df: pd.DataFrame, names: str, values: str, title: str):
    """
    Membuat pie chart Plotly.
    """
    if df is None or df.empty:
        st.info("Data belum tersedia untuk visualisasi ini.")
        return

    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title,
        hole=0.35
    )

    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)


def plot_heatmap_from_filtered(df: pd.DataFrame):
    """
    Membuat heatmap dinamis berdasarkan filter aktif.
    """
    if df is None or df.empty:
        st.info("Data belum tersedia untuk heatmap.")
        return

    required_columns = {"manual_selective_theme_clean", "bertopic_topic_id", "doc_id"}

    if not required_columns.issubset(df.columns):
        st.info("Kolom untuk heatmap belum lengkap.")
        return

    crosstab_df = pd.crosstab(
        df["manual_selective_theme_clean"],
        df["bertopic_topic_id"].astype(str)
    )

    fig = px.imshow(
        crosstab_df,
        text_auto=True,
        aspect="auto",
        title="Heatmap Tema Manual vs Topik BERTopic",
        labels={
            "x": "Topik BERTopic",
            "y": "Tema Manual",
            "color": "Jumlah Chunk"
        }
    )

    fig.update_layout(height=620)
    st.plotly_chart(fig, use_container_width=True)


def plot_scatter_probability(df: pd.DataFrame):
    """
    Scatter plot probabilitas topik berdasarkan panjang chunk.
    """
    if df is None or df.empty:
        st.info("Data belum tersedia untuk scatter plot.")
        return

    required_columns = {"chunk_word_count", "bertopic_topic_probability", "bertopic_topic_id"}

    if not required_columns.issubset(df.columns):
        st.info("Kolom probabilitas atau panjang chunk belum tersedia.")
        return

    fig = px.scatter(
        df,
        x="chunk_word_count",
        y="bertopic_topic_probability",
        color=df["bertopic_topic_id"].astype(str),
        hover_data=[col for col in ["doc_id", "manual_selective_theme_clean", "speech_id"] if col in df.columns],
        title="Panjang Chunk vs Probabilitas Topik BERTopic",
        labels={
            "chunk_word_count": "Jumlah Kata per Chunk",
            "bertopic_topic_probability": "Probabilitas Topik",
            "color": "Topik"
        }
    )

    fig.update_layout(height=560)
    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("📊 Dashboard Analisis Topik")
st.sidebar.caption("Manual Coding dan BERTopic")

menu = st.sidebar.radio(
    "Menu",
    [
        "Ringkasan",
        "Visual Dashboard",
        "Dataset dan Metrik",
        "Manual Coding",
        "BERTopic",
        "Perbandingan Metode",
        "WordCloud",
        "Evidence Teks",
        "Ringkasan Laporan",
    ]
)

st.sidebar.divider()
st.sidebar.markdown("**Filter Data**")

if comparative_analysis_df is not None:
    if "forum_scope_inferred" in comparative_analysis_df.columns:
        forum_options = ["Semua"] + sorted(comparative_analysis_df["forum_scope_inferred"].dropna().astype(str).unique().tolist())
    else:
        forum_options = ["Semua"]

    if "manual_selective_theme_clean" in comparative_analysis_df.columns:
        theme_options = ["Semua"] + sorted(comparative_analysis_df["manual_selective_theme_clean"].dropna().astype(str).unique().tolist())
    else:
        theme_options = ["Semua"]

    if "bertopic_topic_id" in comparative_analysis_df.columns:
        topic_options = ["Semua"] + sorted(comparative_analysis_df["bertopic_topic_id"].dropna().astype(str).unique().tolist(), key=lambda x: int(x) if x.lstrip("-").isdigit() else x)
    else:
        topic_options = ["Semua"]

else:
    forum_options = ["Semua"]
    theme_options = ["Semua"]
    topic_options = ["Semua"]

selected_forum = st.sidebar.selectbox("Forum", forum_options)
selected_theme = st.sidebar.selectbox("Tema Manual", theme_options)
selected_topic = st.sidebar.selectbox("Topik BERTopic", topic_options)

filtered_comparative_df = apply_global_filters(comparative_analysis_df)

st.sidebar.caption(f"Data aktif: {len(filtered_comparative_df)} chunk")


# ============================================================
# Header
# ============================================================

st.title("Analisis Topik Pidato Presiden Prabowo")
st.markdown(
    """
    Dashboard ini menyajikan hasil analisis topik pidato menggunakan **Manual Coding**
    dan **BERTopic**. Visualisasi dibuat untuk membantu membaca distribusi tema,
    pola topik, kesesuaian metode, dan contoh evidence teks.
    """
)


# ============================================================
# Page 1 — Ringkasan
# ============================================================

if menu == "Ringkasan":
    st.header("Ringkasan Analisis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if final_manual_theme_summary_df is not None:
            st.metric("Tema Manual", final_manual_theme_summary_df.shape[0])
        else:
            st.metric("Tema Manual", "-")

    with col2:
        if final_bertopic_topic_summary_df is not None:
            st.metric("Topik BERTopic", final_bertopic_topic_summary_df.shape[0])
        else:
            st.metric("Topik BERTopic", "-")

    with col3:
        if comparative_analysis_df is not None:
            st.metric("Chunk Dianalisis", comparative_analysis_df.shape[0])
        else:
            st.metric("Chunk Dianalisis", "-")

    with col4:
        render_metric_from_df(comparative_metrics_df, "V-measure", "v_measure")

    st.subheader("Fokus Analisis")
    st.markdown(
        """
        Analisis ini digunakan untuk melihat topik utama dalam kumpulan pidato,
        membandingkan hasil pembacaan manual dengan topic modeling otomatis, serta
        menyajikan evidence teks yang mendukung interpretasi.
        """
    )

    st.subheader("Temuan Utama")
    if final_key_findings_df is None:
        render_missing_file_warning(PATHS["final_key_findings"])
    else:
        for _, row in final_key_findings_df.iterrows():
            title = row.get("finding_title", "Temuan")
            description = row.get("finding_description", "")
            with st.expander(f"{row.get('finding_id', '')} — {title}", expanded=False):
                st.write(description)


# ============================================================
# Page 2 — Visual Dashboard
# ============================================================

elif menu == "Visual Dashboard":
    st.header("Visual Dashboard")

    st.markdown(
        """
        Halaman ini merangkum visualisasi utama yang paling mudah digunakan untuk
        presentasi: distribusi tema, distribusi topik, komposisi metode, heatmap,
        dan hubungan probabilitas topik.
        """
    )

    if filtered_comparative_df.empty:
        st.warning("Tidak ada data setelah filter diterapkan.")
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Chunk Aktif", len(filtered_comparative_df))
        with col2:
            if "manual_selective_theme_clean" in filtered_comparative_df.columns:
                st.metric("Tema Aktif", filtered_comparative_df["manual_selective_theme_clean"].nunique())
        with col3:
            if "bertopic_topic_id" in filtered_comparative_df.columns:
                st.metric("Topik Aktif", filtered_comparative_df["bertopic_topic_id"].nunique())

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Distribusi Utama",
                "Manual vs BERTopic",
                "Kualitas Topik",
                "Eksplorasi Chunk",
            ]
        )

        with tab1:
            left, right = st.columns(2)

            with left:
                manual_theme_dist_df = value_count_df(
                    filtered_comparative_df,
                    "manual_selective_theme_clean",
                    "Tema Manual",
                    "Jumlah Chunk"
                )

                plot_bar(
                    manual_theme_dist_df,
                    x="Tema Manual",
                    y="Jumlah Chunk",
                    title="Distribusi Tema Manual",
                    labels={"Tema Manual": "Tema Manual", "Jumlah Chunk": "Jumlah Chunk"}
                )

            with right:
                topic_dist_df = value_count_df(
                    filtered_comparative_df,
                    "bertopic_topic_id",
                    "Topik BERTopic",
                    "Jumlah Chunk"
                )

                plot_bar(
                    topic_dist_df,
                    x="Topik BERTopic",
                    y="Jumlah Chunk",
                    title="Distribusi Topik BERTopic",
                    labels={"Topik BERTopic": "Topik BERTopic", "Jumlah Chunk": "Jumlah Chunk"}
                )

            if "manual_axial_category_clean" in filtered_comparative_df.columns:
                axial_dist_df = value_count_df(
                    filtered_comparative_df,
                    "manual_axial_category_clean",
                    "Axial Category",
                    "Jumlah Chunk"
                )

                plot_bar(
                    axial_dist_df,
                    x="Jumlah Chunk",
                    y="Axial Category",
                    title="Distribusi Axial Category",
                    labels={"Jumlah Chunk": "Jumlah Chunk", "Axial Category": "Axial Category"},
                    orientation="h"
                )

        with tab2:
            plot_heatmap_from_filtered(filtered_comparative_df)

            if {"manual_selective_theme_clean", "bertopic_topic_id", "doc_id"}.issubset(filtered_comparative_df.columns):
                stacked_df = (
                    filtered_comparative_df
                    .groupby(["bertopic_topic_id", "manual_selective_theme_clean"], dropna=False)
                    .agg(Jumlah=("doc_id", "count"))
                    .reset_index()
                )

                fig_stacked = px.bar(
                    stacked_df,
                    x="bertopic_topic_id",
                    y="Jumlah",
                    color="manual_selective_theme_clean",
                    title="Komposisi Tema Manual pada Setiap Topik BERTopic",
                    labels={
                        "bertopic_topic_id": "Topik BERTopic",
                        "Jumlah": "Jumlah Chunk",
                        "manual_selective_theme_clean": "Tema Manual"
                    }
                )

                fig_stacked.update_layout(height=560)
                st.plotly_chart(fig_stacked, use_container_width=True)

        with tab3:
            left, right = st.columns(2)

            with left:
                if final_bertopic_topic_summary_df is not None and "topic_purity" in final_bertopic_topic_summary_df.columns:
                    purity_df = final_bertopic_topic_summary_df.copy()
                    purity_df["bertopic_topic_id"] = purity_df["bertopic_topic_id"].astype(str)

                    plot_bar(
                        purity_df,
                        x="bertopic_topic_id",
                        y="topic_purity",
                        title="Topic Purity terhadap Tema Manual Dominan",
                        labels={"bertopic_topic_id": "Topik BERTopic", "topic_purity": "Topic Purity"}
                    )
                else:
                    st.info("Data topic purity belum tersedia.")

            with right:
                if final_bertopic_topic_summary_df is not None and {"topic_document_count", "topic_purity"}.issubset(final_bertopic_topic_summary_df.columns):
                    topic_quality_df = final_bertopic_topic_summary_df.copy()
                    topic_quality_df["bertopic_topic_id_label"] = topic_quality_df["bertopic_topic_id"].astype(str)

                    fig_quality = px.scatter(
                        topic_quality_df,
                        x="topic_document_count",
                        y="topic_purity",
                        size="topic_document_count",
                        hover_name="bertopic_topic_id_label",
                        hover_data=[col for col in ["dominant_manual_selective_theme", "top_keywords"] if col in topic_quality_df.columns],
                        title="Ukuran Topik vs Topic Purity",
                        labels={
                            "topic_document_count": "Jumlah Chunk",
                            "topic_purity": "Topic Purity"
                        }
                    )

                    fig_quality.update_layout(height=520)
                    st.plotly_chart(fig_quality, use_container_width=True)
                else:
                    st.info("Data kualitas topik belum tersedia.")

            plot_scatter_probability(filtered_comparative_df)

        with tab4:
            if "chunk_word_count" in filtered_comparative_df.columns:
                fig_hist = px.histogram(
                    filtered_comparative_df,
                    x="chunk_word_count",
                    nbins=20,
                    title="Distribusi Panjang Chunk",
                    labels={"chunk_word_count": "Jumlah Kata per Chunk"}
                )

                fig_hist.update_layout(height=500)
                st.plotly_chart(fig_hist, use_container_width=True)

            if "forum_scope_inferred" in filtered_comparative_df.columns:
                forum_dist_df = value_count_df(
                    filtered_comparative_df,
                    "forum_scope_inferred",
                    "Forum",
                    "Jumlah Chunk"
                )

                plot_pie(
                    forum_dist_df,
                    names="Forum",
                    values="Jumlah Chunk",
                    title="Komposisi Chunk berdasarkan Forum"
                )


# ============================================================
# Page 3 — Dataset dan Metrik
# ============================================================

elif menu == "Dataset dan Metrik":
    st.header("Dataset dan Metrik Evaluasi")

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
        "Ringkasan Metrik Komparatif",
        comparative_metrics_df,
        PATHS["comparative_metrics_summary"],
        height=260
    )

    render_dataframe_section(
        "Dataset Komparatif",
        filtered_comparative_df,
        PATHS["comparative_analysis"],
        height=420
    )


# ============================================================
# Page 4 — Manual Coding
# ============================================================

elif menu == "Manual Coding":
    st.header("Hasil Manual Coding")

    st.markdown(
        """
        Manual Coding membaca setiap chunk teks, kemudian memberi open code,
        axial category, dan selective theme.
        """
    )

    tab1, tab2, tab3 = st.tabs(["Visualisasi", "Tabel Ringkasan", "Open Code"])

    with tab1:
        if not filtered_comparative_df.empty:
            manual_theme_dist_df = value_count_df(
                filtered_comparative_df,
                "manual_selective_theme_clean",
                "Tema Manual",
                "Jumlah Chunk"
            )

            plot_bar(
                manual_theme_dist_df,
                x="Tema Manual",
                y="Jumlah Chunk",
                title="Distribusi Tema Manual",
                labels={"Tema Manual": "Tema Manual", "Jumlah Chunk": "Jumlah Chunk"}
            )

            if len(manual_theme_dist_df) <= 7:
                plot_pie(
                    manual_theme_dist_df,
                    names="Tema Manual",
                    values="Jumlah Chunk",
                    title="Proporsi Tema Manual"
                )

    with tab2:
        render_dataframe_section(
            "Ringkasan Tema Manual",
            final_manual_theme_summary_df,
            PATHS["final_manual_theme_summary"],
            height=360
        )

        make_download_button_for_dataframe(
            final_manual_theme_summary_df,
            "final_manual_theme_summary.csv",
            "Unduh Ringkasan Manual Coding"
        )

    with tab3:
        if "manual_open_code_1_clean" in filtered_comparative_df.columns:
            open_code_df = value_count_df(
                filtered_comparative_df,
                "manual_open_code_1_clean",
                "Open Code",
                "Jumlah Chunk"
            ).head(15)

            plot_bar(
                open_code_df,
                x="Jumlah Chunk",
                y="Open Code",
                title="Top Open Code Manual Coding",
                labels={"Jumlah Chunk": "Jumlah Chunk", "Open Code": "Open Code"},
                orientation="h"
            )


# ============================================================
# Page 5 — BERTopic
# ============================================================

elif menu == "BERTopic":
    st.header("Hasil BERTopic")

    st.markdown(
        """
        BERTopic membentuk topik berdasarkan representasi semantik teks dan clustering.
        """
    )

    tab1, tab2, tab3 = st.tabs(["Distribusi Topik", "Topic Purity", "Tabel Topik"])

    with tab1:
        topic_dist_df = value_count_df(
            filtered_comparative_df,
            "bertopic_topic_id",
            "Topik BERTopic",
            "Jumlah Chunk"
        )

        plot_bar(
            topic_dist_df,
            x="Topik BERTopic",
            y="Jumlah Chunk",
            title="Distribusi Topik BERTopic",
            labels={"Topik BERTopic": "Topik BERTopic", "Jumlah Chunk": "Jumlah Chunk"}
        )

    with tab2:
        if final_bertopic_topic_summary_df is not None and "topic_purity" in final_bertopic_topic_summary_df.columns:
            purity_df = final_bertopic_topic_summary_df.copy()
            purity_df["bertopic_topic_id"] = purity_df["bertopic_topic_id"].astype(str)

            plot_bar(
                purity_df,
                x="bertopic_topic_id",
                y="topic_purity",
                title="Topic Purity BERTopic",
                labels={"bertopic_topic_id": "Topik BERTopic", "topic_purity": "Topic Purity"}
            )

        render_html_figure(PATHS["fig_topic_purity"], height=520)

    with tab3:
        render_dataframe_section(
            "Ringkasan Topik BERTopic",
            final_bertopic_topic_summary_df,
            PATHS["final_bertopic_topic_summary"],
            height=420
        )

        make_download_button_for_dataframe(
            final_bertopic_topic_summary_df,
            "final_bertopic_topic_summary.csv",
            "Unduh Ringkasan BERTopic"
        )


# ============================================================
# Page 6 — Perbandingan Metode
# ============================================================

elif menu == "Perbandingan Metode":
    st.header("Perbandingan Manual Coding dan BERTopic")

    st.markdown(
        """
        Perbandingan dilakukan untuk melihat hubungan antara tema hasil Manual Coding
        dan topik hasil BERTopic.
        """
    )

    tab1, tab2, tab3 = st.tabs(["Heatmap", "Stacked Bar", "Interpretasi"])

    with tab1:
        plot_heatmap_from_filtered(filtered_comparative_df)

    with tab2:
        if {"manual_selective_theme_clean", "bertopic_topic_id", "doc_id"}.issubset(filtered_comparative_df.columns):
            stacked_df = (
                filtered_comparative_df
                .groupby(["bertopic_topic_id", "manual_selective_theme_clean"], dropna=False)
                .agg(Jumlah=("doc_id", "count"))
                .reset_index()
            )

            fig_stacked = px.bar(
                stacked_df,
                x="bertopic_topic_id",
                y="Jumlah",
                color="manual_selective_theme_clean",
                title="Komposisi Tema Manual pada Setiap Topik BERTopic",
                labels={
                    "bertopic_topic_id": "Topik BERTopic",
                    "Jumlah": "Jumlah Chunk",
                    "manual_selective_theme_clean": "Tema Manual"
                }
            )

            fig_stacked.update_layout(height=580)
            st.plotly_chart(fig_stacked, use_container_width=True)

    with tab3:
        render_dataframe_section(
            "Interpretasi Komparatif",
            final_comparative_interpretation_df,
            PATHS["final_comparative_interpretation"],
            height=420
        )

        make_download_button_for_dataframe(
            final_comparative_interpretation_df,
            "final_comparative_interpretation.csv",
            "Unduh Interpretasi Komparatif"
        )


# ============================================================
# Page 7 — WordCloud
# ============================================================

elif menu == "WordCloud":
    st.header("WordCloud")

    st.markdown(
        """
        WordCloud digunakan sebagai visualisasi eksploratif untuk melihat kata-kata
        dominan dalam korpus.
        """
    )

    render_png_image(
        PATHS["wordcloud_all"],
        caption="Kata-kata dominan dalam korpus pidato"
    )


# ============================================================
# Page 8 — Evidence Teks
# ============================================================

elif menu == "Evidence Teks":
    st.header("Evidence Teks Representatif")

    if final_representative_evidence_df is None:
        render_missing_file_warning(PATHS["final_representative_evidence"])
    else:
        topic_options = ["Semua Topik"] + sorted(
            final_representative_evidence_df["bertopic_topic_id"].astype(str).unique().tolist(),
            key=lambda x: int(x) if x.lstrip("-").isdigit() else x
        )

        selected_topic_evidence = st.selectbox("Pilih Topik BERTopic", topic_options)

        filtered_evidence_df = final_representative_evidence_df.copy()

        if selected_topic_evidence != "Semua Topik":
            filtered_evidence_df = filtered_evidence_df[
                filtered_evidence_df["bertopic_topic_id"].astype(str) == selected_topic_evidence
            ]

        st.dataframe(filtered_evidence_df, use_container_width=True, height=520)

        st.subheader("Cuplikan Teks")
        for _, row in filtered_evidence_df.head(5).iterrows():
            topic_id = row.get("bertopic_topic_id", "-")
            manual_theme = row.get("manual_selective_theme", "-")
            text_excerpt = row.get("text_excerpt", row.get("text", ""))

            with st.expander(f"Topik {topic_id} — {manual_theme}", expanded=False):
                st.write(shorten_text(text_excerpt, max_chars=900))


# ============================================================
# Page 9 — Ringkasan Laporan
# ============================================================

elif menu == "Ringkasan Laporan":
    st.header("Ringkasan Laporan")

    if final_report_summary_md is None:
        render_missing_file_warning(PATHS["final_report_summary_md"])
    else:
        st.markdown(final_report_summary_md)


# ============================================================
# Footer
# ============================================================

st.divider()
st.caption(
    "Dashboard ini menampilkan output final analisis dan tidak menjalankan ulang proses modeling."
)
