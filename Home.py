import streamlit as st

st.set_page_config(
    page_title="Home"
)
# Logo


st.markdown("<h1 style= 'text-align: center;'>Selamat Datang di ISPA Diagnosis System </h1>" , unsafe_allow_html=True)

col1,col2,col3 = st.columns([3,6,2])
with col2:
    st.image("Isp.png", width=300)
    
st.write("---")

st.subheader("Apa itu ISPA ?")

st.write("infeksi yang menyerang saluran pernapasan, baik saluran atas maupun bawah. Kondisi ini dapat terjadi pada beberapa organ pernapasan seperti sinus, faring, laring hingga hidung.")

st.write("ISPA adalah penyebab utama morbiditas dan mortalitas penyakit menular di dunia. Hampir empat juta orang meninggal akibat ISPA setiap tahun, 98%-nya disebabkan oleh infeksi saluran pernapasan bawah. Tingkat mortalitas sangat tinggi pada anak dibawah umur, dan orang lanjut usia. ISPA di Indonesia menempati urutan pertama penyebab kematian pada anak dan dewasa.")

st.write(" Situasi saat ini perlakuan Dinas Kesehatan perlu melakukan penanganan yang efektif terhadap penyakit ISPA. oleh karena itu, diperlukan suatu metode dalam  klasifikasi penyakit ISPA menggunakan algoritma SVM")

st.write("Dengan adanya permasalahan diatas, kami membuat suatu sistem untuk mendiagnosa penyakit ISPA atau Pneunomia, silahkan Diagnosis penyakit anda.")


