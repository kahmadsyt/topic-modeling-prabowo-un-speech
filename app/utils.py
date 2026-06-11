from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


def get_project_root() -> Path:
    """
    Mengembalikan root project berdasarkan lokasi file app.py.
    """
    return Path(__file__).resolve().parents[1]


def resolve_path(relative_path: str) -> Path:
    """
    Mengubah path relatif dari root project menjadi path absolut.
    """
    return get_project_root() / relative_path


@st.cache_data(show_spinner=False)
def load_csv(relative_path: str) -> Optional[pd.DataFrame]:
    """
    Membaca CSV dari path relatif terhadap root project.
    """
    file_path = resolve_path(relative_path)

    if not file_path.exists():
        return None

    return pd.read_csv(file_path)


@st.cache_data(show_spinner=False)
def load_markdown(relative_path: str) -> Optional[str]:
    """
    Membaca file Markdown dari path relatif terhadap root project.
    """
    file_path = resolve_path(relative_path)

    if not file_path.exists():
        return None

    return file_path.read_text(encoding="utf-8")


def render_missing_file_warning(relative_path: str) -> None:
    """
    Menampilkan informasi jika file belum tersedia.
    """
    st.warning(
        f"File `{relative_path}` belum tersedia. "
        "Pastikan output analisis sudah tersedia di repository."
    )


def render_dataframe_section(title: str, df: Optional[pd.DataFrame], relative_path: str, height: int = 360) -> None:
    """
    Menampilkan tabel dengan keterangan sumber file.
    """
    st.subheader(title)

    if df is None:
        render_missing_file_warning(relative_path)
        return

    st.caption(f"Sumber data: `{relative_path}`")
    st.dataframe(df, use_container_width=True, height=height)


def render_metric_from_df(df: Optional[pd.DataFrame], label: str, metric_name: str, default_value: str = "-") -> None:
    """
    Menampilkan nilai metrik dari tabel metric-value.
    """
    value = default_value

    if df is not None and {"metric", "value"}.issubset(df.columns):
        matched = df.loc[df["metric"] == metric_name, "value"]
        if not matched.empty:
            value = matched.iloc[0]

    st.metric(label, value)


def render_html_figure(relative_path: str, height: int = 620) -> None:
    """
    Menampilkan file HTML Plotly.
    """
    file_path = resolve_path(relative_path)

    if not file_path.exists():
        render_missing_file_warning(relative_path)
        return

    html_content = file_path.read_text(encoding="utf-8")
    components.html(html_content, height=height, scrolling=True)


def render_png_image(relative_path: str, caption: Optional[str] = None, use_container_width: bool = True) -> None:
    """
    Menampilkan file gambar PNG.
    """
    file_path = resolve_path(relative_path)

    if not file_path.exists():
        render_missing_file_warning(relative_path)
        return

    image = Image.open(file_path)
    st.image(image, caption=caption or relative_path, use_container_width=use_container_width)


def make_download_button_for_dataframe(df: Optional[pd.DataFrame], file_name: str, label: str) -> None:
    """
    Membuat tombol unduh CSV.
    """
    if df is None:
        return

    csv_data = df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label=label,
        data=csv_data,
        file_name=file_name,
        mime="text/csv"
    )


def shorten_text(text: str, max_chars: int = 350) -> str:
    """
    Memotong teks panjang untuk tampilan ringkas.
    """
    text = str(text).strip()

    if len(text) <= max_chars:
        return text

    return text[:max_chars].rstrip() + "..."


def value_count_df(df: pd.DataFrame, column: str, label_name: str, count_name: str = "Jumlah") -> pd.DataFrame:
    """
    Membuat tabel value counts yang stabil lintas versi Pandas.
    """
    if df is None or column not in df.columns:
        return pd.DataFrame(columns=[label_name, count_name])

    result = (
        df[column]
        .fillna("Tidak tersedia")
        .astype(str)
        .str.strip()
        .replace("", "Tidak tersedia")
        .value_counts()
        .rename_axis(label_name)
        .reset_index(name=count_name)
    )

    return result

def value_count_df(df, column, label_name, count_name="Jumlah"):
    """
    Membuat tabel value counts yang stabil lintas versi Pandas.
    Digunakan untuk membuat distribusi kategori pada dashboard.
    """
    import pandas as pd

    if df is None or column not in df.columns:
        return pd.DataFrame(columns=[label_name, count_name])

    result = (
        df[column]
        .fillna("Tidak tersedia")
        .astype(str)
        .str.strip()
        .replace("", "Tidak tersedia")
        .value_counts()
        .rename_axis(label_name)
        .reset_index(name=count_name)
    )

    return result