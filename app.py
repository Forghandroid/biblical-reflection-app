import streamlit as st

st.title("Biblical Reflection Tool")

injil = st.text_area("Bacaan Injil")
pl = st.text_area("Bacaan Perjanjian Lama")

def tafsir_injil(text):
    return f"Makna Injil:\n{text}\n\nFokus: iman, ketenangan, Allah pusat hidup"

def tafsir_pl(text):
    return f"Makna Perjanjian Lama:\n{text}\n\nFokus: kesetiaan dan konsekuensi hidup"

def relevansi():
    return "Keduanya menekankan kesetiaan kepada Allah"

def cta():
    return "Jadikan Tuhan pusat hidupmu, bukan materi"

if st.button("Analisis"):
    st.write(tafsir_injil(injil))
    st.write(tafsir_pl(pl))
    st.write(relevansi())
    st.write(cta())
