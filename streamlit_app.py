import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Latihan Asesmen — Pelaksanaan Anggaran",
    page_icon="📘",
    layout="centered",
)

# Sembunyikan padding default Streamlit supaya kuis tampil penuh
st.markdown(
    """
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 1rem;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "assets" / "latihan_pelaksanaan_anggaran.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1000, scrolling=True)
