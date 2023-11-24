import tkinter as tk
from tkinter import filedialog, messagebox
import pytube

def download_video():
    # Video indirme fonksiyonu
    url = url_entry.get()
    download_path = filedialog.askdirectory()
    
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(download_path)
        status_label.config(text="İndirme tamamlandı!")
    except Exception as e:
        status_label.config(text=f"Hata: {str(e)}")

def open_application():
    response = messagebox.askquestion("Sorumluluk Kabulü", "Yapılan indirmeler sizin sorumluluğunuzdadır. Onaylıyor musunuz?")
    if response == 'yes':
        root.after(100, open_app)  # Uygulama açma işlemi
    else:
        messagebox.showinfo("Giriş İptal Edildi", "Uygulama açılmadı.")
        root.destroy()  # Uygulama kapatma

def open_app():
    # Uygulama açma işlemi burada yapılacak
    # ...
    pass  # Uygulama açma işlemi için gerçek kod buraya gelecek

root = tk.Tk()
root.geometry('600x400')
root.title("YouTube Video İndirici")

# Url yolu
Path_label = tk.Label(root, text="Adım 1 : İndirmek istediğiniz videoya gidin")
Path_label.pack(pady=3)
Path_label_2 = tk.Label(root, text="Adım 2 : Videonun alt kısmında bulunan paylaş butonuna basın")
Path_label_2.pack(pady=3)
Path_label_3 = tk.Label(root, text="Adım 3 : Orada çıkan urlyi kopyala butonuna tıklayıp uygulamaya yapıştırınız")
Path_label_3.pack(pady=3)

# URL giriş kutusu
url_label = tk.Label(root, text="Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# İndirme klasörü seçimi
def select_download_path():
    download_path = filedialog.askdirectory()
    download_path_label.config(text=f"İndirme Klasörü: {download_path}")

select_path_button = tk.Button(root, text="İndirme Klasörü Seç", command=select_download_path)
select_path_button.pack(pady=10)

download_path_label = tk.Label(root, text=f"İndirme Klasörü: Varsayılan")
download_path_label.pack(pady=10)

# İndirme butonu
download_button = tk.Button(root, text="Videoyu İndir", command=download_video)
download_button.pack()

Path_label_4 = tk.Label(root, text="İndirme süresi, indirmek istediğiniz videonun uzunluğuna göre değişiklik gösterebilir. \nSADECE BEKLEYİN LÜTFEN")
Path_label_4.pack(pady=25)
# İndirme durumu
status_label = tk.Label(root, text="")
status_label.pack()

# Uygulama açılırken onay mesajı gösterme
root.after(100, open_application)

root.mainloop()
