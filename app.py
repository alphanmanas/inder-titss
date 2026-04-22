import streamlit as st

st.set_page_config(layout="wide")

st.title("Türkiye İnşaat Tedarik Sınıflandırma Sistemi")

data = {
    "03 – Beton": {
        "Hazır Beton": ["C25","C30","C35","C40"],
        "Prekast": ["Kiriş","Panel"],
        "Katkı": ["Akışkanlaştırıcı","Priz Geciktirici"]
    },
    "05 – Metal & Çelik": {
        "Demir": ["B420C","Hasır Çelik"],
        "Profil": ["IPE","HEA"],
        "Ankraj": ["Kimyasal Ankraj"]
    },
    "07 – İzolasyon": {
        "Membran": ["PVC","Bitümlü"],
        "Poliüretan": ["Sprey Köpük"],
        "Bitüm": ["Sıcak Bitüm"]
    }
}

col1, col2, col3 = st.columns(3)

groups = list(data.keys())

for i, group in enumerate(groups):
    col = [col1, col2, col3][i % 3]
    with col:
        if st.button(group):
            st.session_state["group"] = group

if "group" in st.session_state:
    st.subheader(st.session_state["group"])

    subs = data[st.session_state["group"]]

    for sub in subs:
        if st.button(sub):
            st.session_state["sub"] = sub

if "sub" in st.session_state:
    st.write("### " + st.session_state["sub"])

    vars = data[st.session_state["group"]][st.session_state["sub"]]

    for v in vars:
        st.write("- " + v)
