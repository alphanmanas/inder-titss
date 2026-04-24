import os
import base64
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sınıflandırma Sistemi",
    page_icon="🏗️",
    layout="wide"
)

EXCEL_PATH = "Ulusal İnşaat Tedarik Sistemi v01.xlsx"
LOGO_PATH = "İNDER Logo.jpg"

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #f1f5f9;
}
.header-box {
    background: white;
    border-radius: 18px;
    padding: 22px;
    display: flex;
    align-items: center;
    gap: 24px;
    margin-bottom: 24px;
}
.main-title {
    font-size: 30px;
    font-weight: 800;
    color: #0f172a;
}
.sub-title {
    font-size: 18px;
    color: #475569;
}
.metric-box {
    background: white;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    margin-bottom: 20px;
}
.metric-label {
    font-size: 16px;
    color: #0f172a;
}
.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #ef3340;
}
.section-box {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin-top: 20px;
}
.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 18px;
}
.stButton > button {
    width: 100%;
    min-height: 90px;
    border-radius: 14px;
    border: none;
    color: white;
    font-weight: 800;
    font-size: 16px;
    background: linear-gradient(135deg, #ef3340, #457b9d);
}
.stButton > button:hover {
    color: white;
    border: none;
    opacity: 0.92;
}
.alt-box {
    background: #f8fafc;
    border-left: 6px solid #ef3340;
    border-radius: 12px;
    padding: 14px 16px;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


def image_to_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def clean_text(value):
    if pd.isna(value):
        return ""
    return str(value).strip()


def find_column(columns, keywords):
    for col in columns:
        c = str(col).lower()
        for keyword in keywords:
            if keyword.lower() in c:
                return col
    return None


@st.cache_data
def load_data(path):
    df = pd.read_excel(path)
    df.columns = [str(c).strip() for c in df.columns]

    ana_col = find_column(df.columns, ["ana grup", "div", "division", "ana"])
    grup_col = find_column(df.columns, ["grup", "grp", "group"])
    alt_col = find_column(df.columns, ["alt grup", "sub", "sub group", "alt"])

    if not ana_col or not grup_col or not alt_col:
        st.error("Excel içinde Ana Grup, Grup ve Alt Grup kolonları bulunamadı.")
        st.stop()

    data = df[[ana_col, grup_col, alt_col]].copy()
    data.columns = ["Ana Grup", "Grup", "Alt Grup"]

    for col in data.columns:
        data[col] = data[col].apply(clean_text)

    data = data[
        (data["Ana Grup"] != "") &
        (data["Grup"] != "") &
        (data["Alt Grup"] != "")
    ].drop_duplicates()

    return data


logo_b64 = image_to_base64(LOGO_PATH)

st.markdown(
    f"""
    <div class="header-box">
        <img src="data:image/jpeg;base64,{logo_b64}" width="170">
        <div>
            <div class="main-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>
            <div class="sub-title">(MasterFormat Tabanlı)</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

df = load_data(EXCEL_PATH)

if "secilen_ana_grup" not in st.session_state:
    st.session_state.secilen_ana_grup = None

if "secilen_grup" not in st.session_state:
    st.session_state.secilen_grup = None

ana_gruplar = sorted(df["Ana Grup"].unique())
gruplar = sorted(df["Grup"].unique())
alt_gruplar = sorted(df["Alt Grup"].unique())

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Ana Grup</div>
        <div class="metric-value">{len(ana_gruplar)}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Grup Sayısı</div>
        <div class="metric-value">{len(gruplar)}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Alt Grup Sayısı</div>
        <div class="metric-value">{len(alt_gruplar)}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    secim = st.session_state.secilen_ana_grup or "-"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Seçim</div>
        <div class="metric-value">{secim}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">20 Ana Grup</div>', unsafe_allow_html=True)

for i in range(0, len(ana_gruplar), 4):
    cols = st.columns(4)
    for j, ana_grup in enumerate(ana_gruplar[i:i + 4]):
        with cols[j]:
            if st.button(ana_grup, key=f"ana_{ana_grup}"):
                st.session_state.secilen_ana_grup = ana_grup
                st.session_state.secilen_grup = None

st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.secilen_ana_grup:
    secilen_df = df[df["Ana Grup"] == st.session_state.secilen_ana_grup]
    secilen_gruplar = sorted(secilen_df["Grup"].unique())

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="section-title">{st.session_state.secilen_ana_grup} İçindeki Gruplar</div>',
        unsafe_allow_html=True
    )

    for i in range(0, len(secilen_gruplar), 5):
        cols = st.columns(5)
        for j, grup in enumerate(secilen_gruplar[i:i + 5]):
            with cols[j]:
                if st.button(grup, key=f"grup_{st.session_state.secilen_ana_grup}_{grup}"):
                    st.session_state.secilen_grup = grup

    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.secilen_ana_grup and st.session_state.secilen_grup:
    alt_df = df[
        (df["Ana Grup"] == st.session_state.secilen_ana_grup) &
        (df["Grup"] == st.session_state.secilen_grup)
    ]

    secilen_alt_gruplar = sorted(alt_df["Alt Grup"].unique())

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="section-title">{st.session_state.secilen_grup} İçindeki Alt Gruplar</div>',
        unsafe_allow_html=True
    )

    for alt_grup in secilen_alt_gruplar:
        st.markdown(f'<div class="alt-box">{alt_grup}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
