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
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text=f"Hata: {str(e)}")

def open_application():
    response = messagebox.askquestion("Acceptance of Responsibility", "Downloads are your responsibility. Do you approve?")
    if response == 'yes':
        root.after(100, open_app)  # Uygulama açma işlemi
    else:
        messagebox.showinfo("Login Canceled", "Application not opened.")
        root.destroy()  # Uygulama kapatma

def open_app():
    # Uygulama açma işlemi burada yapılacak
 
    pass  

root = tk.Tk()
root.geometry('600x400')
root.title("YouTube Video Downloader")

# Url yolu
Path_label = tk.Label(root, text="Step 1: Go to the video you want to download")
Path_label.pack(pady=3)
Path_label_2 = tk.Label(root, text="Step 2: Click the share button below the video")
Path_label_2.pack(pady=3)
Path_label_3 = tk.Label(root, text="Step 3: Copy the url in the Share section and paste it into the application")
Path_label_3.pack(pady=3)


# URL giriş kutusu
url_label = tk.Label(root, text="Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# İndirme klasörü seçimi
def select_download_path():
    download_path = filedialog.askdirectory()
    download_path_label.config(text=f"Download File: {download_path}")

select_path_button = tk.Button(root, text="Select the location to download the video", command=select_download_path)
select_path_button.pack(pady=10)

download_path_label = tk.Label(root, text=f"Download File: Default")
download_path_label.pack(pady=10)

# İndirme butonu
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

Path_label_4 = tk.Label(root, text="Download time may vary depending on the length of the video you want to download. \nJUST WAIT PLEASE")
Path_label_4.pack(pady=25)
# İndirme durumu
status_label = tk.Label(root, text="")
status_label.pack()

# Uygulama açılırken onay mesajı gösterme
root.after(100, open_application)

root.mainloop()
