import streamlit as st

st.title("Biblical Reflection Tool")

injil = st.text_area("Bacaan Injil")
pl = st.text_area("Bacaan Perjanjian Lama")

def tafsir_injil(text):
    return f"""
### MAKNA INJIL
{text}

Bacaan ini menegaskan bahwa manusia dipanggil untuk menaruh kepercayaan penuh kepada Allah dalam seluruh aspek kehidupan. Yesus mengajarkan bahwa kekhawatiran terhadap kebutuhan hidup tidak seharusnya menguasai hati manusia. Sebaliknya, hidup harus diarahkan pada pencarian Kerajaan Allah sebagai prioritas utama. Melalui perumpamaan dan ajaran-Nya, manusia diingatkan bahwa Allah adalah pemelihara kehidupan yang setia. Karena itu, iman menjadi dasar untuk menjalani hidup dengan tenang dan tidak dikuasai kecemasan.
"""

def tafsir_pl(text):
    return f"""
### MAKNA PERJANJIAN LAMA
{text}

Bacaan ini menggambarkan dinamika hubungan antara manusia dengan Allah dalam sejarah umat Israel. Terlihat bagaimana kesetiaan kepada Allah membawa keberkahan, sedangkan penyimpangan membawa kehancuran. Peristiwa dalam teks menunjukkan bahwa manusia sering mudah dipengaruhi dan meninggalkan jalan Tuhan. Namun Allah tetap berbicara melalui nabi untuk mengingatkan umat-Nya agar kembali kepada kebenaran. Oleh karena itu, bacaan ini menekankan pentingnya ketaatan dan kesetiaan yang konsisten kepada Allah.
"""

def relevansi():
    return "Keduanya menekankan kesetiaan kepada Allah"

def cta():
    return """
### CALL TO ACTION
Renungkan kembali apa yang menjadi pusat hidupmu saat ini dan apakah itu sudah selaras dengan kehendak Tuhan. Lepaskan ketergantungan berlebihan pada hal-hal duniawi yang sering menimbulkan kecemasan. Bangun kebiasaan untuk berdoa dan membaca firman sebagai dasar pengambilan keputusan harian. Belajarlah untuk mempercayakan masa depan kepada penyertaan Allah, bukan pada kekuatan sendiri. Jadikan setiap hari sebagai kesempatan untuk hidup dalam iman yang nyata dan konsisten.
"""

if st.button("Analisis Bacaan"):
    if injil.strip() and pl.strip():
        st.markdown("---")
        st.markdown(tafsir_injil(injil))

        st.markdown("---")
        st.markdown(tafsir_pl(pl))

        st.markdown("---")
        st.markdown(relevansi())

        st.markdown("---")
        st.markdown(cta())
    else:
        st.warning("Silakan isi kedua bacaan terlebih dahulu.")
