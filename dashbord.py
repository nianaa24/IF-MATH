rimport streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Analisis_Pelanggan(df_customer) :
    count_customer_state = df_customer['customer_state'].value_counts().reset_index()
    count_customer_state.columns = ['Negara','Jumlah']

    Negara_Teratas = count_customer_state.head(10)

    st.header("10122247 - Rania Shahinaz")
    st.header("Grafik 10 Negara dengan Customer Terbanyak")
    st.dataframe(Negara_Teratas)

    # Buat bar chart
    label = Negara_Teratas['Negara']
    data = Negara_Teratas['Jumlah']

    fig, ax = plt.subplots()
    ax.bar(label, data, color=['purple' if jumlah <= 10000 else 'red' for jumlah in data])
    ax.set_xlabel('Negara')
    ax.set_ylabel('Jumlah')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)                    
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Negara dengan Member Terbanyak") :
        st.write('Pembelian yang banyak di suatu negara dapat dipengaruhi oleh sejumlah faktor, termasuk stabilitas ekonomi, pertumbuhan pasar, kemudahan berbisnis, demografi yang menguntungkan, infrastruktur yang baik, ketidakstabilan di negara lain, ketersediaan sumber daya alam, dan kebijakan pemerintah yang mendukung investasi dan perdagangan. Kombinasi dari faktor-faktor ini dapat membuat suatu negara menjadi destinasi yang menarik bagi perusahaan untuk melakukan investasi dan berkontribusi pada peningkatan volume pembelian. hal-hal tersebutlah yang membuat suatu negara memiliki banyak member di suatu e-commerce.')

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    # Ambil 10 kota teratas berdasarkan kolom yang sesuai
    bottom_cities = df_customer['customer_city'].value_counts().tail(5)
    bottom_cities.columns = ['Seller_City','Jumlah']

    Kota_Terbawah = bottom_cities.tail(5)

    st.header("Diagram Member Paling Sedikit di 5 Kota")
    st.dataframe(Kota_Terbawah)

    # Buat pie chart
    fig, ax = plt.subplots()
    ax.pie(bottom_cities, labels=bottom_cities.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Pastikan pie chart terlihat seperti lingkaran
    
    # Tampilkan pie chart di Streamlit
    st.pyplot(fig)

    
    #Expander Grafik
    with st.expander("Penjelasan Kota dengan Member paling sedikit") :
        st.write('Kota-kota dengan pembelian sangat sedikit cenderung memiliki kondisi ekonomi yang lemah, tingkat pengangguran tinggi, ketidakpastian politik, kurangnya akses ke sumber daya, atau masalah kemiskinan dan kesenjangan ekonomi. Faktor-faktor ini dapat bersama-sama menyebabkan rendahnya daya beli masyarakat dan aktivitas ekonomi di kota tersebut.hal-hal tersebutlah yang membuat kota - kota tersebut kurangnya minat untuk menjadi member di suatu e-commerce.')

def Analisis_Pembayaran(df_payment):
    # Mengelompokkan data pembayaran berdasarkan urutan pembayaran dan menghitung jumlah pembayaran untuk setiap urutan
    payment_by_sequence = df_payment.groupby('payment_sequential')['payment_value'].sum().reset_index()

    st.header("10122481-ARISKA DIYANGKU SUWANDI HILALA")
    st.header("Grafik Urutan Pembayaran")
    st.dataframe(payment_by_sequence)

    # Menampilkan tabel data pembayaran
    payment_by_sequence = df_payment.head()

    payment_by_type = df_payment.groupby('payment_type')['payment_value'].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(payment_by_type['payment_type'], payment_by_type['payment_value'], color='blue')
    ax.set_xlabel('Metode Pembayaran')
    ax.set_ylabel('Total Pembayaran')
    plt.title('Analisis Pembayaran Berdasarkan Metode Pembayaran')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(payment_by_type['payment_type'])) :
        ax.text(payment_by_type['payment_type'][i], payment_by_type['payment_value'][i], str(payment_by_type['payment_value'][i]), ha='center', va='bottom' )

    # Pengelompokkan data pembayaran berdasarkan urutan pembayaran dan menghitung jumlah pembayaran untuk setiap urutan
    payment_by_sequence = df_payment.groupby('payment_sequential')['payment_value'].sum().reset_index()

    label = [1, 2, 3, 4, 5]
    data = [4.0623, 6.467, 17.672, 24.390, 157.323]

    # Buat bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(label, data, color=['skyblue' if jumlah == 1000000 else 'blue' for jumlah in label])
    ax.set_xlabel('payment_value')
    ax.set_ylabel('payment_sequential')

    # Menambahkan Label Pada Setiap Bar
    for i in range(len(label)):
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom')

    # Rotasi Label 45 derajat
    plt.xticks(rotation=45)
    st.pyplot(fig)
     


#Expander Grafik
    with st.expander("Penjelasan Tentang Urutan Pembayaran") :
        st.write('Grafik garis menunjukkan tren jumlah pembayaran berdasarkan urutan pembayaran. Dari grafik tersebut, kita dapat melihat apakah jumlah pembayaran cenderung meningkat, menurun, atau tetap stabil seiring dengan urutan pembayaran. Ini membantu kita dalam memahami perilaku pembayaran pelanggan dan pola yang mungkin ada dalam proses pembayaran.')

def Analisis_Barang(df_item) :
    st.header("10122253 - Hana Mar'atul Afifah Rambe")

    # Mengambil data penjualan dari dataframe df_item
    count_product_sales = df_item.groupby('product_id').size().reset_index(name='Jumlah Penjualan')
    Product_Terlaris = count_product_sales.nlargest(7, 'Jumlah Penjualan')  # Mengambil 7 produk terlaris

    # Menampilkan tabel
    st.header('Grafik 7 Produk Terlaris Berdasarkan Jumlah Penjualannya')
    st.dataframe(Product_Terlaris)

    # Menampilkan Bar Chart menggunakan Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(Product_Terlaris['product_id'], Product_Terlaris['Jumlah Penjualan'], color='blue')
    plt.xticks(rotation=90)
    plt.xlabel('Product ID')
    plt.ylabel('Jumlah Penjualan')
    plt.title('Grafik 7 Produk Terlaris Berdasarkan Jumlah Penjualannya')
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan diagram Produk terlaris berdasarkan jumlah penjualannya") :
        st.write('Grafik di atas menampilkan 7 produk terlaris berdasarkan jumlah penjualannya. Setiap batang mewakili satu produk, sedangkan tinggi batang menunjukkan jumlah penjualan produk tersebut. Semakin tinggi batang, semakin tinggi jumlah penjualan produk.')

    # Menghitung jumlah penjualan dari dataframe df_item
    count_product_sales = df_item.groupby('product_id').size().reset_index(name='Jumlah Penjualan')

    # Mengambil 7 produk terbawah berdasarkan jumlah penjualan
    Product_Terendah = count_product_sales.nsmallest(7, 'Jumlah Penjualan')

    # Menampilkan tabel
    st.header('7 Produk Terbawah Berdasarkan Jumlah Penjualannya')
    st.dataframe(Product_Terendah)

    # Menampilkan Diagram Grafik (Line Chart)
    plt.figure(figsize=(10, 6))
    plt.plot(Product_Terendah['product_id'], Product_Terendah['Jumlah Penjualan'], marker='o', linestyle='-')
    plt.xlabel('Product ID')
    plt.ylabel('Jumlah Penjualan')
    plt.title('Grafik Jumlah Penjualan 7 Produk Terbawah')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan grafik penjualan terbawah") :
        st.write('menampilkan jumlah penjualan dari 7 produk terbawah dalam bentuk garis yang menghubungkan titik data setiap produk. Setiap titik mewakili satu produk dan jumlah penjualan yang terkait dengannya.produk penjualan terendah tersebut ada pada angka 1.')

def Analisis_Review(df_review) :
    st.header("10122235 - Ryuna Aurelia Putri")

    #Menampilkan tabel review
    count_review_city = df_review['review_score'].value_counts().reset_index()
    count_review_city.columns = ['Review Score', 'Jumlah Review']
    Score_Terbesar = count_review_city.head(5)
    st.header('Grafik 5 Score Terbesar Dari Review')
    st.dataframe(Score_Terbesar)

    #Menampilkan Bar Chart
    plt.figure(figsize=(13, 14))
    plt.bar(Score_Terbesar['Review Score'], Score_Terbesar['Jumlah Review'], color='blue')
    plt.xlabel('Review Score')
    plt.ylabel('Jumlah Review')
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan Score Review Terbesar") :
        st.write('Grafik diatas menunjukkan bahwa review terbanyak yang didapatkan adalah dengan score 5 , dan review terendah dengan score 2. Review dari pembeli merupakan variabel yang sangat berpengaruh dalam keputusan pembelian pada e-commmerce. Review dengan score yang besar tentunya dapat memberikan kesan baik dan memberi peluang lebih besar bagi pembeli untuk membeli suatu barang.')

    #Menampilkan Diagram Garis
    plt.figure(figsize=(10, 6))
    plt.plot(Score_Terbesar['Review Score'], Score_Terbesar['Jumlah Review'], marker='o', linestyle='-', color='blue')
    plt.title('Diagram Garis 5 Score Terbesar Dari Review')
    plt.xlabel('Review Score')
    plt.ylabel('Jumlah Review')
    plt.grid(True)
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan Diagram Garis Score Review") :
        st.write('Diagram garis diatas menunjukan dengan lebih jelas bahwa terdapat perbandingan pada pembeli yang memberi review dengan score 5 juga dengan score lain. terlihat jelas review dengan score 5 memiliki jumlah yang sangat banyak dibandingkan dengan jumlah score yang lain.')
    
def Analisis_Penjual(df_seller):
    st.header("10122258 - Indri Tri Puspita")

    #tabel
    count_seller_city = df_seller['seller_city'].value_counts().reset_index()
    count_seller_city.columns = ['Kota', 'Jumlah Penjual']
    Penjual_Terbanyak = count_seller_city.head(10)

    #Menampilkan tabel
    st.header('Grafik 10 Kota dengan Jumlah Penjual Terbanyak')
    st.dataframe(Penjual_Terbanyak)

    #Diagram Garis
    plt.figure(figsize=(17, 12))
    plt.plot(Penjual_Terbanyak['Kota'], Penjual_Terbanyak['Jumlah Penjual'], marker='o', linestyle='-', color='blue')
    plt.title('Diagram Garis 10 Kota dengan Jumlah Penjual Terbanyak')
    plt.xlabel('Kota')
    plt.ylabel('Jumlah Penjual')
    plt.grid(True)
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan diagram kota dengan jumlah penjual terbanyak") :
        st.write('Diagram diatas menunjukan 10 kota dengan jumlah penjual terbanyak. Kota-kota dengan jumlah penjual yang banyak menunjukkan adanya potensi pasar yang besar dalam industri e-commerce. Dengan mengidentifikasi kota-kota yang banyak penjualnya, dapat dijadikan panduan untuk perluasan jangkauan bisnis.')


    #Bar Chart
    plt.figure(figsize=(16, 12))
    plt.bar(Penjual_Terbanyak['Kota'], Penjual_Terbanyak['Jumlah Penjual'], color='pink')
    plt.title('Diagram Batang 5 Kota dengan Jumlah Penjual Terbanyak')
    plt.xlabel('Asal Kota')
    plt.ylabel('Jumlah Penjual')
    st.pyplot(plt)

    #Expander Grafik
    with st.expander("Penjelasan diagram kota dengan jumlah penjual terbanyak") :
        st.write('Diagram diatas menunjukan 10 kota dengan jumlah penjual terbanyak. Kota Sao Paolo menempati posisi pertama yang memiliki jumlah penjual terbanyak, dan Kota Maringa berada di posisi ke 10. Diagram ini menunjukkan distribusi jumlah penjual di berbagai kota dan memungkinkan kita untuk melihat perbedaan dalam jumlah penjual di antara kota-kota teratas. ')


df_customer = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/customers_dataset.csv")
df_payment = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/order_payments_dataset.csv")
df_item = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/order_items_dataset.csv")
df_review = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/order_reviews_dataset.csv")
df_seller = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/sellers_dataset.csv")


with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce Kelompok IF7-MATH")
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["Analisis Pelanggan", "Analisis Pembayaran", "Analisis Barang", "Analisis Review", "Analisis Penjual"])
    
    with tab1 :
        Analisis_Pelanggan(df_customer)
    with tab2 :
        Analisis_Pembayaran(df_payment)
    with tab3 :
        Analisis_Barang(df_item)
    with tab4 :
        Analisis_Review(df_review)
    with tab5 :
        Analisis_Penjual(df_seller)
    


