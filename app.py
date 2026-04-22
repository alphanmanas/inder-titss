import streamlit as st

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sınıflandırma Sistemi",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------
DATA = {
    "01 – Genel & Şantiye": {
        "Geçici Yapılar": ["Konteyner Ofis", "Geçici Depo", "Geçici Barınma Ünitesi"],
        "İskele": ["Cephe İskelesi", "Mobil İskele", "Kalıp İskelesi"],
        "Şantiye Ekipmanları": ["Jeneratör", "Kompresör", "Aydınlatma Kulesi"],
    },
    "02 – Zemin & Temel": {
        "Kazı": ["Genel Kazı", "Kaya Kazısı", "Makinalı Kazı"],
        "Dolgu": ["Kırmataş Dolgu", "Stabilize Dolgu", "Sıkıştırılmış Dolgu"],
        "Zemin İyileştirme": ["Jet Grout", "Fore Kazık", "Enjeksiyon"],
    },
    "03 – Beton": {
        "Hazır Beton": ["C25", "C30", "C35", "C40"],
        "Prekast": ["Prekast Kiriş", "Prekast Döşeme", "Prekast Panel"],
        "Katkı Kimyasalları": ["Akışkanlaştırıcı", "Priz Geciktirici", "Su Yalıtım Katkısı"],
    },
    "04 – Duvar & Masonry": {
        "Tuğla": ["Dolu Tuğla", "Delikli Tuğla", "Asmolen"],
        "Gazbeton": ["Blok", "Panel", "Lento"],
        "Taş": ["Doğal Taş Kaplama", "Kesme Taş", "Dekoratif Taş"],
    },
    "05 – Metal & Çelik": {
        "İnşaat Demiri": ["B420C", "Nervürlü Demir", "Hasır Çelik"],
        "Profil Çelik": ["IPE", "HEA", "Kutu Profil"],
        "Ankraj": ["Kimyasal Ankraj", "Mekanik Ankraj", "Ağır Yük Ankrajı"],
    },
    "06 – Ahşap & Kompozit": {
        "Ahşap Yapı": ["Lamine Ahşap", "Masif Ahşap", "Çatı Kirişi"],
        "MDF": ["Ham MDF", "Lamine MDF", "Neme Dayanıklı MDF"],
        "CLT": ["CLT Panel", "CLT Döşeme", "CLT Duvar"],
    },
    "07 – İzolasyon & Su Yalıtımı": {
        "Membran": ["PVC Membran", "Bitümlü Membran", "EPDM Membran"],
        "Poliüretan": ["Sprey Köpük", "Likit Membran", "Dolgu Köpüğü"],
        "Bitüm": ["Bitümlü Örtü", "Soğuk Uygulama", "Sıcak Uygulama"],
    },
    "08 – Kapı & Pencere": {
        "Alüminyum": ["Alüminyum Doğrama", "Sürme Sistem", "Isı Yalıtımlı Doğrama"],
        "PVC": ["PVC Pencere", "PVC Kapı", "Sürme PVC"],
        "Çelik Kapı": ["Daire Kapısı", "Yangın Kapısı", "Villa Kapısı"],
    },
    "09 – İç Kaplama (Finishes)": {
        "Boya": ["İç Cephe Boyası", "Dış Cephe Boyası", "Epoksi Boya"],
        "Seramik": ["Duvar Seramiği", "Zemin Seramiği", "Porselen"],
        "Parke": ["Laminat Parke", "Lamine Parke", "Masif Parke"],
    },
    "10 – Sabit Donatılar": {
        "Dolap": ["Gömme Dolap", "Vestiyer", "Arşiv Dolabı"],
        "Mutfak": ["Mutfak Dolabı", "Tezgâh", "Ankastre Modül"],
        "Banyo": ["Lavabo Ünitesi", "Duş Sistemi", "Gömme Rezervuar"],
    },
    "11 – Özel Sistemler": {
        "Asansör": ["Yolcu Asansörü", "Yük Asansörü", "Panoramik Asansör"],
        "Yürüyen Merdiven": ["İç Mekân", "Dış Mekân", "AVM Tipi"],
    },
    "12 – Mobilya": {
        "Ofis": ["Masa", "Toplantı Masası", "Dosya Dolabı"],
        "Sabit Mobilya": ["Resepsiyon Bankosu", "Sabit Tezgâh", "Özel Üretim Raf"],
    },
    "13 – Endüstriyel Sistemler": {
        "Fabrika Ekipmanları": ["Konveyör", "Endüstriyel Raf", "Makine Kaidesi"],
    },
    "14 – Dış Cephe": {
        "Giydirme Cephe": ["Stick Sistem", "Panel Sistem", "Spider Sistem"],
        "Cam Sistemleri": ["Low-E Cam", "Temperli Cam", "Lamine Cam"],
    },
    "15 – Mekanik (HVAC)": {
        "Chiller": ["Hava Soğutmalı", "Su Soğutmalı", "Scroll Chiller"],
        "VRF": ["Heat Pump", "Heat Recovery", "Mini VRF"],
        "Klima": ["Split Klima", "Kaset Tipi", "Salon Tipi"],
    },
    "16 – Tesisat": {
        "Boru": ["PPRC", "Çelik Boru", "PE Boru"],
        "Armatür": ["Batarya", "Vana", "Mix Armatür"],
        "Yangın": ["Sprinkler", "Yangın Dolabı", "Pompa"],
    },
    "17 – Elektrik": {
        "Kablo": ["NYY", "TTR", "Data Kablosu"],
        "Trafo": ["Kuru Tip", "Yağlı Tip", "Dağıtım Trafosu"],
        "Pano": ["Ana Dağıtım Panosu", "Kat Panosu", "Kompanzasyon Panosu"],
    },
    "18 – Zayıf Akım & Dijital": {
        "CCTV": ["IP Kamera", "NVR", "PTZ Kamera"],
        "Fiber": ["Fiber Kablo", "Patch Panel", "ODF"],
        "IoT": ["Sensör", "Gateway", "Akıllı Sayaç"],
    },
    "19 – Peyzaj & Altyapı": {
        "Bordür": ["Beton Bordür", "Granit Bordür", "Dekoratif Bordür"],
        "Sulama": ["Damla Sulama", "Sprink Sulama", "Kontrol Ünitesi"],
        "Kanalizasyon": ["Koruge Boru", "Muayene Bacası", "Rögar Kapağı"],
    },
    "20 – Enerji & Yeni Nesil": {
        "Güneş": ["PV Panel", "İnverter", "Taşıyıcı Konstrüksiyon"],
        "Batarya (MCAP dahil)": ["LFP Batarya", "MCAP Modül", "Enerji Depolama Kabini"],
        "Şarj Altyapısı": ["AC Şarj Ünitesi", "DC Hızlı Şarj", "Yük Yönetim Sistemi"],
    },
}

# -----------------------------
# SESSION
# -----------------------------
if "selected_group" not in st.session_state:
    st.session_state.selected_group = None

if "selected_sub" not in st.session_state:
    st.session_state.selected_sub = None

# -----------------------------
# HELPERS
# -----------------------------
def total_sub_count():
    return sum(len(subs) for subs in DATA.values())

def total_var_count():
    return sum(len(vars_list) for subs in DATA.values() for vars_list in subs.values())

def filter_data(query: str):
    if not query:
        return DATA

    q = query.lower().strip()
    filtered = {}

    for group, subs in DATA.items():
        group_match = q in group.lower()
        matched_subs = {}

        for sub, vars_list in subs.items():
            sub_match = q in sub.lower()
            matched_vars = [v for v in vars_list if q in v.lower()]

            if sub_match:
                matched_subs[sub] = vars_list
            elif matched_vars:
                matched_subs[sub] = matched_vars

        if group_match:
            filtered[group] = subs
        elif matched_subs:
            filtered[group] = matched_subs

    return filtered

# -----------------------------
# STYLE
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

.main-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 0.25rem;
}

.main-subtitle {
    font-size: 1.0rem;
    color: #6b7280;
    margin-bottom: 1.5rem;
}

.metric-box {
    background: white;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    border: 1px solid #eef2f7;
}

.metric-title {
    font-size: 0.9rem;
    color: #6b7280;
    margin-bottom: 8px;
    font-weight: 600;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #e63946;
}

.section-box {
    background: white;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    border: 1px solid #eef2f7;
    margin-top: 18px;
}

.section-title {
    font-size: 1.3rem;
    font-weight: 800;
    margin-bottom: 14px;
    color: #1f2937;
}

.path-text {
    color: #6b7280;
    font-size: 0.92rem;
    margin-bottom: 10px;
}

.var-box {
    background: #f8fafc;
    border-left: 6px solid #e63946;
    padding: 14px 16px;
    border-radius: 10px;
    margin-bottom: 10px;
    font-weight: 600;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    min-height: 78px;
    font-weight: 700;
    font-size: 1rem;
    border: none;
    background: linear-gradient(135deg, #e63946, #457b9d);
    color: white;
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
}

.stButton > button:hover {
    color: white;
    border: none;
    opacity: 0.95;
}

input {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="main-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">MasterFormat Tabanlı Demo Dashboard</div>', unsafe_allow_html=True)

# -----------------------------
# METRICS
# -----------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f'<div class="metric-box"><div class="metric-title">Ana Grup</div><div class="metric-value">{len(DATA)}</div></div>',
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        f'<div class="metric-box"><div class="metric-title">SUB Sayısı</div><div class="metric-value">{total_sub_count()}</div></div>',
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        f'<div class="metric-box"><div class="metric-title">VAR Sayısı</div><div class="metric-value">{total_var_count()}</div></div>',
        unsafe_allow_html=True
    )

selected_code = "-"
if st.session_state.selected_group:
    selected_code = st.session_state.selected_group.split(" – ")[0]

with m4:
    st.markdown(
        f'<div class="metric-box"><div class="metric-title">Seçilen Grup</div><div class="metric-value">{selected_code}</div></div>',
        unsafe_allow_html=True
    )

# -----------------------------
# SEARCH
# -----------------------------
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">20 Ana Grup</div>', unsafe_allow_html=True)

search = st.text_input("Ara", placeholder="Grup, SUB veya VAR ara", label_visibility="collapsed")
filtered_data = filter_data(search)

group_names = list(filtered_data.keys())

for i in range(0, len(group_names), 4):
    cols = st.columns(4)
    row_groups = group_names[i:i+4]

    for j, group in enumerate(row_groups):
        with cols[j]:
            if st.button(group, key=f"group_{group}"):
                st.session_state.selected_group = group
                st.session_state.selected_sub = None

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# SUBS
# -----------------------------
if st.session_state.selected_group and st.session_state.selected_group in DATA:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path-text">Ana Grup > {st.session_state.selected_group}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="section-title">SUB Gruplar</div>', unsafe_allow_html=True)

    sub_names = list(DATA[st.session_state.selected_group].keys())

    for i in range(0, len(sub_names), 3):
        cols = st.columns(3)
        row_subs = sub_names[i:i+3]

        for j, sub in enumerate(row_subs):
            with cols[j]:
                if st.button(sub, key=f"sub_{sub}"):
                    st.session_state.selected_sub = sub

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# VARS
# -----------------------------
if (
    st.session_state.selected_group
    and st.session_state.selected_sub
    and st.session_state.selected_group in DATA
    and st.session_state.selected_sub in DATA[st.session_state.selected_group]
):
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path-text">Ana Grup > {st.session_state.selected_group} > {st.session_state.selected_sub}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="section-title">VAR Listesi</div>', unsafe_allow_html=True)

    for item in DATA[st.session_state.selected_group][st.session_state.selected_sub]:
        st.markdown(f'<div class="var-box">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
