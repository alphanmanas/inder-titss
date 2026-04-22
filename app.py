import streamlit as st

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sistemi",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------
DATA = {
    "01 - Genel & Santiye": {
        "Gecici Yapilar": ["Konteyner Ofis", "Gecici Depo", "Gecici Barinma"],
        "Iskele": ["Cephe Iskelesi", "Mobil Iskele", "Kalıp Iskelesi"],
        "Santiye Ekipmanlari": ["Jenerator", "Kompresor", "Aydinlatma Kulesi"],
    },
    "02 - Zemin & Temel": {
        "Kazi": ["Genel Kazi", "Kaya Kazi", "Makinali Kazi"],
        "Dolgu": ["Kirmatas Dolgu", "Stabilize Dolgu"],
        "Zemin Iyilestirme": ["Jet Grout", "Fore Kazik"],
    },
    "03 - Beton": {
        "Hazir Beton": ["C25", "C30", "C35"],
        "Prekast": ["Prekast Kiris", "Prekast Panel"],
        "Katki": ["Akiskanlastirici", "Priz Geciktirici"],
    },
    "04 - Duvar": {
        "Tugla": ["Dolu Tugla", "Delikli Tugla"],
        "Gazbeton": ["Blok", "Panel"],
    },
    "05 - Metal & Celik": {
        "Demir": ["B420C", "Nervurlu Demir"],
        "Profil": ["IPE", "HEA"],
    }
}

# -----------------------------
# SESSION
# -----------------------------
if "group" not in st.session_state:
    st.session_state.group = None

if "sub" not in st.session_state:
    st.session_state.sub = None

# -----------------------------
# STYLE
# -----------------------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: 800;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="big-title">Türkiye İnşaat Tedarik Sistemi</div>', unsafe_allow_html=True)

# -----------------------------
# GROUPS
# -----------------------------
st.markdown("### Ana Gruplar")

cols = st.columns(3)

for i, group in enumerate(DATA.keys()):
    with cols[i % 3]:
        if st.button(group):
            st.session_state.group = group
            st.session_state.sub = None

# -----------------------------
# SUB GROUPS
# -----------------------------
if st.session_state.group:
    st.markdown(f"## {st.session_state.group}")

    cols = st.columns(3)

    for i, sub in enumerate(DATA[st.session_state.group]):
        with cols[i % 3]:
            if st.button(sub):
                st.session_state.sub = sub

# -----------------------------
# VARS
# -----------------------------
if st.session_state.group and st.session_state.sub:
    st.markdown(f"### {st.session_state.sub}")

    for item in DATA[st.session_state.group][st.session_state.sub]:
        st.markdown(f'<div class="card">{item}</div>', unsafe_allow_html=True)
