import streamlit as st

st.set_page_config(
    page_title="Biblical Reflection Tool",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Biblical Reflection Tool")
st.caption("Aplikasi sederhana untuk membantu refleksi Injil, Perjanjian Lama, homili, kisah inspiratif, dan doa umat.")

st.markdown("---")

# =========================
# INPUT BACAAN
# =========================

injil = st.text_area(
    "Masukkan Bacaan Injil",
    placeholder="Contoh: Matius 6:24-34",
    height=100
)

pl = st.text_area(
    "Masukkan Bacaan Perjanjian Lama / Bacaan Pertama",
    placeholder="Contoh: 2 Tawarikh 24:17-25",
    height=100
)

menu = st.selectbox(
    "Pilih Menu Refleksi",
    [
        "Analisis Bacaan",
        "Homili 3 Menit",
        "Kisah / Cerita Inspiratif",
        "Doa Umat Katolik",
        "Semua Output"
    ]
)

tema = "Kesetiaan kepada Allah sebagai pusat hidup yang mengalahkan kecemasan dan ketergantungan pada dunia."


# =========================
# FUNGSI ANALISIS
# =========================

def makna_injil(text):
    return f"""
### 📖 Makna Bacaan Injil

Bacaan Injil **{text}** mengajak manusia untuk menempatkan Allah sebagai pusat utama dalam hidup. Yesus menegaskan bahwa manusia tidak dapat mengabdi kepada dua tuan, sebab hati yang terbagi akan mudah dikuasai oleh kecemasan. Kekhawatiran tentang makanan, minuman, pakaian, dan masa depan tidak boleh menggeser iman kepada pemeliharaan Allah. Melalui gambaran burung di udara dan bunga di ladang, Yesus menunjukkan bahwa Allah mengetahui kebutuhan manusia dan memelihara ciptaan-Nya dengan setia. Karena itu, orang beriman dipanggil untuk mencari dahulu Kerajaan Allah dan kebenaran-Nya sebelum mengejar hal-hal duniawi.
"""


def makna_pl(text):
    return f"""
### 📜 Makna Bacaan Perjanjian Lama / Bacaan Pertama

Bacaan pertama **{text}** menunjukkan bagaimana kesetiaan manusia kepada Allah dapat melemah ketika hati mulai dipengaruhi oleh kepentingan duniawi. Kisah ini mengingatkan bahwa manusia dapat jatuh ketika tidak lagi mendengarkan suara Tuhan dan menolak teguran yang membawa kebenaran. Dalam sejarah umat Allah, ketidaktaatan sering membawa kekacauan, perpecahan, dan kehancuran moral. Namun, Allah tetap mengutus suara profetik untuk menegur, membimbing, dan memanggil umat-Nya kembali kepada jalan yang benar. Maka, bacaan ini menekankan pentingnya kesetiaan yang teguh, bukan iman yang hanya bertahan ketika keadaan nyaman.
"""


def relevansi_bacaan():
    return """
### 🔗 Relevansi Kedua Bacaan

Kedua bacaan memiliki hubungan yang kuat karena sama-sama berbicara tentang kesetiaan manusia kepada Allah. Bacaan pertama memperlihatkan akibat ketika manusia meninggalkan Tuhan dan lebih mengikuti pengaruh duniawi. Injil menunjukkan ajaran Yesus bahwa hati manusia tidak boleh terbagi antara Allah dan mammon. Jika Allah tidak lagi menjadi pusat, maka hidup mudah dikuasai oleh kecemasan, keserakahan, dan keputusan yang salah. Sebaliknya, ketika manusia mencari dahulu Kerajaan Allah, hidupnya memperoleh arah, ketenangan, dan keberanian untuk tetap setia.
"""


def call_to_action():
    return """
### ✅ Call to Action

Hari ini kita diajak untuk memeriksa kembali apa yang benar-benar menjadi pusat hidup kita. Jangan sampai pekerjaan, uang, ambisi, atau kecemasan masa depan diam-diam menggantikan posisi Allah dalam hati kita. Mulailah dengan langkah sederhana: berdoa sebelum mengambil keputusan, bersyukur atas hal kecil, dan tidak membiarkan kekhawatiran menguasai pikiran. Ketika menghadapi tekanan hidup, ingatlah bahwa Allah tidak pernah meninggalkan orang yang mencari Dia dengan tulus. Jadikan hari ini sebagai kesempatan untuk memilih Allah sebagai pusat hidup, bukan sekadar pelengkap hidup.
"""


# =========================
# FUNGSI HOMILI
# =========================

def homili_3_menit():
    return f"""
### 🎙️ Homili 3 Menit

Saudara-saudari yang terkasih dalam Kristus,

Tema utama dari Sabda Tuhan hari ini adalah **{tema}** Bacaan pertama mengingatkan kita bahwa manusia bisa berubah arah ketika hatinya tidak lagi berpaut kepada Tuhan. Ketika manusia mulai menolak suara kebenaran, ia perlahan kehilangan kepekaan rohani dan mudah mengikuti pengaruh yang menjauhkan dirinya dari Allah. Kisah ini menjadi peringatan bagi kita bahwa iman tidak cukup hanya dimiliki, tetapi harus terus dijaga, dipelihara, dan diperbarui.

Dalam Injil, Yesus berkata bahwa manusia tidak dapat mengabdi kepada dua tuan. Kita tidak dapat sekaligus menjadikan Allah sebagai pusat hidup, tetapi pada saat yang sama menggantungkan rasa aman sepenuhnya pada uang, jabatan, rencana, atau kekuatan sendiri. Yesus tidak melarang kita bekerja, merencanakan masa depan, atau memenuhi kebutuhan hidup. Namun, Yesus menegur ketika semua itu menjadi tuan baru yang menguasai hati kita dan membuat kita hidup dalam kecemasan.

Saudara-saudari, dalam kehidupan sehari-hari kita sering mengalami hal ini. Ada orang yang terlalu khawatir tentang masa depan sampai lupa bersyukur atas berkat hari ini. Ada keluarga yang sibuk mengejar kebutuhan materi, tetapi perlahan kehilangan waktu doa dan kehangatan kasih. Ada mahasiswa atau pekerja yang begitu takut gagal sehingga lupa bahwa hidupnya tetap berada dalam penyertaan Tuhan.

Karena itu, Sabda Tuhan hari ini mengajak kita kembali kepada prioritas yang benar. Yesus berkata, “Carilah dahulu Kerajaan Allah dan kebenarannya, maka semuanya itu akan ditambahkan kepadamu.” Artinya, ketika Allah menjadi pusat, hal-hal lain dalam hidup akan menemukan tempatnya secara benar. Kita tetap bekerja, tetap belajar, tetap berjuang, tetapi tidak lagi diperbudak oleh rasa takut.

Maka marilah kita memohon rahmat Tuhan agar hati kita tidak terbagi. Jangan biarkan mammon, kecemasan, atau ambisi menjadi tuan atas hidup kita. Pilihlah Allah sebagai pusat, sebab hanya di dalam Dia kita menemukan damai, arah, dan kekuatan untuk menjalani hari esok.

Amin.
"""


# =========================
# FUNGSI CERITA INSPIRATIF
# =========================

def kisah_burung_berkicau():
    return """
### 🐦 Kisah Inspiratif: Burung yang Tetap Berkicau

Suatu pagi, seekor burung kecil bertengger di dahan pohon setelah semalaman diterpa angin dan hujan. Sayapnya masih basah, sarangnya hampir rusak, dan langit belum sepenuhnya cerah. Namun ketika matahari mulai muncul, burung itu tetap berkicau. Seekor anak kecil yang melihatnya bertanya kepada ayahnya, “Mengapa burung itu masih bernyanyi padahal semalam ia hampir kehilangan sarangnya?” Ayahnya menjawab, “Karena burung itu tidak menunggu hidup sempurna untuk mulai bersyukur.”

Kisah kecil ini mengingatkan kita pada Injil hari ini. Yesus menunjuk burung-burung di udara bukan untuk mengajarkan kemalasan, tetapi untuk menunjukkan kepercayaan yang sederhana kepada pemeliharaan Allah. Burung tetap mencari makan, tetap terbang, tetap membangun sarang, tetapi tidak hidup dalam kecemasan seperti manusia yang lupa percaya. Begitu juga kita, tetaplah bekerja dan berjuang, tetapi jangan biarkan kekhawatiran mencuri nyanyian syukur dari hati kita.
"""


def kisah_gaya_doa_sang_katak():
    return """
### 🐸 Kisah Inspiratif Bergaya Reflektif: Katak yang Ingin Didengar Tuhan

Di sebuah kolam kecil, seekor katak selalu merasa doanya tidak seindah suara burung, tidak setenang desir angin, dan tidak semerdu nyanyian manusia di rumah ibadat. Setiap malam ia mencoba diam agar tidak mengganggu, tetapi hatinya tetap ingin memuji Tuhan. Suatu hari ia berkata, “Tuhan, suaraku hanya kroak-kroak kecil, mungkin tidak pantas sampai kepada-Mu.” Lalu dari kedalaman hatinya ia merasa seolah Tuhan berkata, “Aku menciptakanmu dengan suara itu; mengapa engkau takut memuji-Ku dengan apa yang Kuberikan?”

Kisah ini mengingatkan kita bahwa Tuhan tidak meminta kita datang dengan hidup yang sempurna, melainkan dengan hati yang percaya. Banyak orang terlalu cemas karena merasa kurang mampu, kurang pantas, atau kurang berhasil. Padahal, Allah tidak pertama-tama melihat kehebatan kita, tetapi kesetiaan hati kita. Seperti katak kecil itu, kita diajak untuk datang kepada Tuhan apa adanya, bukan dengan hati yang dikuasai kecemasan, tetapi dengan iman yang sederhana.
"""


def cerita_lucu_reflektif():
    return """
### 😄 Cerita Lucu Reflektif: Orang yang Terlalu Khawatir

Ada seorang bapak yang setiap malam sulit tidur karena terlalu banyak memikirkan masa depan. Ia khawatir tentang pekerjaan, biaya hidup, cuaca besok, bahkan khawatir kalau nanti ia lupa mengunci pintu. Suatu malam istrinya berkata, “Pak, sudah tidur saja. Tuhan yang menjaga kita.” Bapak itu menjawab, “Iya, Bu. Tapi saya khawatir Tuhan juga sedang sibuk menjaga orang lain.”

Cerita ini lucu, tetapi menyentuh kenyataan hidup kita. Kadang kita percaya kepada Tuhan, tetapi tetap merasa seolah-olah semuanya harus kita kendalikan sendiri. Kita berdoa, tetapi setelah berdoa tetap mengambil kembali semua kecemasan itu. Injil hari ini mengingatkan bahwa percaya kepada Allah berarti berani menyerahkan apa yang memang berada di luar kendali kita, sambil tetap melakukan bagian kita dengan setia.
"""


def menu_kisah():
    pilihan_kisah = st.radio(
        "Pilih jenis kisah inspiratif",
        [
            "Burung Berkicau",
            "Gaya Doa Sang Katak",
            "Cerita Lucu Reflektif"
        ]
    )

    if pilihan_kisah == "Burung Berkicau":
        return kisah_burung_berkicau()
    elif pilihan_kisah == "Gaya Doa Sang Katak":
        return kisah_gaya_doa_sang_katak()
    else:
        return cerita_lucu_reflektif()


# =========================
# FUNGSI DOA UMAT
# =========================

def doa_umat():
    return """
### 🙏 Doa Umat Katolik

**Pemimpin:**  
Saudara-saudari terkasih, setelah mendengarkan Sabda Tuhan yang mengajak kita untuk tidak mengabdi kepada dua tuan dan untuk mencari dahulu Kerajaan Allah, marilah kita menyampaikan doa-doa permohonan kepada Bapa yang memelihara hidup kita.

**1. Bagi Gereja Kudus**  
Ya Bapa, dampingilah Gereja-Mu agar selalu setia mewartakan Kerajaan Allah di tengah dunia yang sering dikuasai oleh kekhawatiran, keserakahan, dan kepentingan diri. Semoga Gereja menjadi tanda harapan bagi semua orang yang sedang kehilangan arah hidup.  
**Marilah kita mohon: Kabulkanlah doa kami, ya Tuhan.**

**2. Bagi para pemimpin bangsa dan masyarakat**  
Ya Bapa, bimbinglah para pemimpin agar tidak dikuasai oleh ambisi, kekuasaan, dan kepentingan materi. Semoga mereka menjalankan tugas dengan kejujuran, keadilan, dan keberpihakan kepada mereka yang lemah.  
**Marilah kita mohon: Kabulkanlah doa kami, ya Tuhan.**

**3. Bagi mereka yang sedang cemas dan takut akan masa depan**  
Ya Bapa, kuatkanlah saudara-saudari kami yang sedang mengalami kekhawatiran karena pekerjaan, ekonomi, studi, keluarga, atau kesehatan. Semoga mereka mengalami penghiburan-Mu dan percaya bahwa Engkau tidak pernah meninggalkan mereka.  
**Marilah kita mohon: Kabulkanlah doa kami, ya Tuhan.**

**4. Bagi keluarga-keluarga Kristiani**  
Ya Bapa, bantulah setiap keluarga agar tidak hanya mengejar kebutuhan duniawi, tetapi juga membangun hidup doa, kasih, dan kesetiaan kepada-Mu. Semoga keluarga menjadi tempat pertama untuk belajar percaya kepada penyelenggaraan-Mu.  
**Marilah kita mohon: Kabulkanlah doa kami, ya Tuhan.**

**5. Bagi kita semua yang hadir dan merenungkan Sabda Tuhan hari ini**  
Ya Bapa, ajarlah kami untuk tidak membagi hati antara Engkau dan hal-hal duniawi. Semoga kami mampu mencari dahulu Kerajaan-Mu dan menjalani hidup dengan iman, syukur, serta keberanian untuk percaya.  
**Marilah kita mohon: Kabulkanlah doa kami, ya Tuhan.**

**Pemimpin:**  
Allah Bapa yang penuh kasih, Engkau mengetahui setiap kebutuhan hidup kami. Dengarkanlah doa-doa yang kami sampaikan kepada-Mu, dan bentuklah hati kami agar selalu setia mencari Kerajaan-Mu. Demi Kristus, Tuhan dan Pengantara kami.

**Amin.**
"""


# =========================
# TAMPILAN OUTPUT
# =========================

if st.button("Buat Refleksi"):
    if injil.strip() and pl.strip():
        st.markdown("---")

        if menu == "Analisis Bacaan":
            st.markdown(makna_injil(injil))
            st.markdown(makna_pl(pl))
            st.markdown(relevansi_bacaan())
            st.markdown(call_to_action())

        elif menu == "Homili 3 Menit":
            st.markdown(homili_3_menit())

        elif menu == "Kisah / Cerita Inspiratif":
            st.info("Kisah yang ditampilkan adalah cerita orisinal untuk refleksi, bukan kutipan langsung dari buku tertentu.")
            st.markdown(menu_kisah())

        elif menu == "Doa Umat Katolik":
            st.markdown(doa_umat())

        elif menu == "Semua Output":
            st.markdown(makna_injil(injil))
            st.markdown(makna_pl(pl))
            st.markdown(relevansi_bacaan())
            st.markdown(call_to_action())
            st.markdown(homili_3_menit())
            st.info("Kisah berikut adalah cerita orisinal untuk refleksi, bukan kutipan langsung dari buku tertentu.")
            st.markdown(kisah_burung_berkicau())
            st.markdown(doa_umat())

    else:
        st.warning("Silakan isi Bacaan Injil dan Bacaan Perjanjian Lama terlebih dahulu.")
