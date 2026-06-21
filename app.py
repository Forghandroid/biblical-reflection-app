import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
# FUNGSI CERITA INSPIRATIF DARI MEDIA ISNET
# =========================

STORY_SOURCES = [
    {
        "nama": "Burung Berkicau",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Burung/index.html"
    },
    {
        "nama": "Doa Sang Katak",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Katak/index.html"
    }
]

FALLBACK_STORIES = [
    {
        "title": "Penyelenggaraan Ilahi dalam Tiga Perahu Penyelamat",
        "source": "Doa Sang Katak",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Katak/index.html"
    },
    {
        "title": "Gembala Suka Segala Cuaca",
        "source": "Doa Sang Katak",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Katak/index.html"
    },
    {
        "title": "Gereja Hutan",
        "source": "Doa Sang Katak",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Katak/index.html"
    },
    {
        "title": "Rajawali dan Ayam",
        "source": "Doa Sang Katak",
        "url": "https://media.isnet.org/kmi/sufi/Mello/Katak/index.html"
    }
]


@st.cache_data(ttl=86400)
def ambil_daftar_kisah():
    daftar_kisah = []

    for sumber in STORY_SOURCES:
        try:
            response = requests.get(
                sumber["url"],
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for a in soup.find_all("a"):
                judul = a.get_text(" ", strip=True)
                href = a.get("href")

                if not judul or not href:
                    continue

                judul_lower = judul.lower()

                skip_words = [
                    "indeks", "homepage", "tentang penulis",
                    "isnet", "sufi", "islam", "burung berkicau",
                    "doa sang katak"
                ]

                if any(word in judul_lower for word in skip_words):
                    continue

                daftar_kisah.append({
                    "title": judul,
                    "source": sumber["nama"],
                    "url": urljoin(sumber["url"], href)
                })

        except Exception:
            continue

    if not daftar_kisah:
        return FALLBACK_STORIES

    return daftar_kisah


def buat_kata_kunci(injil_text, pl_text):
    teks = f"{injil_text} {pl_text}".lower()

    kata_kunci = [
        "allah", "tuhan", "percaya", "iman", "setia",
        "kekhawatiran", "cemas", "takut", "khawatir",
        "pemeliharaan", "penyelenggaraan", "burung",
        "bunga", "makan", "minum", "pakaian",
        "mammon", "uang", "materi", "kerajaan",
        "lepas", "pelepasan", "cuaca", "damai"
    ]

    if "matius 6" in teks or "mat 6" in teks:
        kata_kunci += [
            "penyelenggaraan",
            "pemeliharaan",
            "burung",
            "khawatir",
            "takut",
            "percaya",
            "cuaca",
            "pelepasan"
        ]

    if "mammon" in teks or "uang" in teks or "harta" in teks:
        kata_kunci += [
            "uang",
            "materi",
            "pelepasan",
            "pendapatan",
            "milik"
        ]

    return kata_kunci


def skor_kisah(kisah, kata_kunci):
    judul = kisah["title"].lower()
    sumber = kisah["source"].lower()

    skor = 0

    for kata in kata_kunci:
        if kata in judul:
            skor += 5

    # Skor tambahan untuk kisah yang sangat cocok dengan Matius 6:24-34
    if "penyelenggaraan" in judul:
        skor += 25

    if "burung" in judul:
        skor += 20

    if "cuaca" in judul:
        skor += 15

    if "pelepasan" in judul:
        skor += 15

    if "doa sang katak" in sumber:
        skor += 2

    if "burung berkicau" in sumber:
        skor += 2

    return skor


def pilih_kisah_terbaik(injil_text, pl_text):
    daftar_kisah = ambil_daftar_kisah()
    kata_kunci = buat_kata_kunci(injil_text, pl_text)

    kisah_terbaik = max(
        daftar_kisah,
        key=lambda kisah: skor_kisah(kisah, kata_kunci)
    )

    return kisah_terbaik


def alasan_kisah(kisah, injil_text):
    judul = kisah["title"].lower()

    if "penyelenggaraan" in judul:
        return """
Kisah ini dipilih karena sangat dekat dengan tema Injil tentang pemeliharaan Allah. Dalam Matius 6:24-34, Yesus mengajak manusia untuk tidak dikuasai kekhawatiran, sebab Bapa mengetahui kebutuhan hidup manusia. Tema penyelenggaraan ilahi membantu umat memahami bahwa percaya kepada Tuhan bukan berarti pasif, melainkan berani melakukan bagian kita sambil menyerahkan hasilnya kepada Allah.
"""

    if "burung" in judul:
        return """
Kisah ini dipilih karena berhubungan langsung dengan gambaran burung dalam Injil. Yesus menunjuk burung-burung di udara sebagai tanda bahwa Allah memelihara ciptaan-Nya. Melalui kisah ini, umat dapat diajak belajar percaya, bersyukur, dan tidak membiarkan kecemasan merampas damai hati.
"""

    if "cuaca" in judul:
        return """
Kisah ini dipilih karena sesuai dengan tema iman yang tetap tenang dalam berbagai keadaan. Injil mengajarkan bahwa manusia tidak perlu hidup dalam kekhawatiran berlebihan terhadap hari esok. Seperti seseorang yang belajar menerima cuaca apa adanya, orang beriman juga diajak menjalani hidup dengan percaya kepada penyertaan Allah.
"""

    if "pelepasan" in judul or "pendapatan" in judul:
        return """
Kisah ini dipilih karena sejalan dengan ajaran Yesus tentang bahaya keterikatan pada mammon. Injil mengingatkan bahwa manusia tidak dapat mengabdi kepada Allah dan harta sekaligus. Kisah ini dapat membantu umat merenungkan apakah hidupnya masih dikuasai oleh kepemilikan, ambisi, atau rasa takut kehilangan.
"""

    return """
Kisah ini dipilih karena memiliki hubungan dengan tema umum bacaan, yaitu kesetiaan, iman, dan perubahan hati manusia. Kisah inspiratif semacam ini dapat membantu umat memahami Sabda Tuhan secara lebih dekat dengan pengalaman hidup sehari-hari. Melalui cerita sederhana, pesan Injil menjadi lebih mudah direnungkan dan diterapkan.
"""


def kisah_inspiratif_otomatis(injil_text, pl_text):
    kisah = pilih_kisah_terbaik(injil_text, pl_text)

    return f"""
### 📚 Kisah Inspiratif yang Dipilih Otomatis

**Judul kisah:** {kisah["title"]}  
**Sumber:** {kisah["source"]}  
**Link asli:** [{kisah["url"]}]({kisah["url"]})

#### Alasan kisah ini sesuai dengan bacaan

{alasan_kisah(kisah, injil_text)}

#### Cara menyisipkan dalam homili

Kisah ini dapat diletakkan setelah penjelasan Injil, sebelum bagian aplikasi hidup. Setelah menceritakan kisah tersebut secara singkat, pengkhotbah dapat menghubungkannya dengan pertanyaan reflektif: *apakah kita sungguh percaya bahwa Allah memelihara hidup kita, atau kita masih lebih sering dikuasai oleh kekhawatiran dan rasa takut akan masa depan?*

> Catatan: Aplikasi ini menampilkan judul, sumber, link, dan refleksi singkat. Untuk membaca isi lengkap kisah, gunakan link asli di atas.
"""


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
    st.info("Aplikasi memilih salah satu kisah dari indeks Burung Berkicau atau Doa Sang Katak berdasarkan kecocokan tema bacaan. Isi lengkap kisah tidak disalin; aplikasi menampilkan judul, sumber, link, dan alasan relevansi.")
    st.markdown(kisah_inspiratif_otomatis(injil, pl))

        elif menu == "Doa Umat Katolik":
            st.markdown(doa_umat())

        elif menu == "Semua Output":
            st.markdown(makna_injil(injil))
            st.markdown(makna_pl(pl))
            st.markdown(relevansi_bacaan())
            st.markdown(call_to_action())
            st.markdown(homili_3_menit())
            st.info("Kisah berikut dipilih otomatis dari indeks Burung Berkicau atau Doa Sang Katak berdasarkan kecocokan tema bacaan.")
st.markdown(kisah_inspiratif_otomatis(injil, pl))
            st.markdown(doa_umat())

    else:
        st.warning("Silakan isi Bacaan Injil dan Bacaan Perjanjian Lama terlebih dahulu.")
