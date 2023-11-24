import pytube

video_url = input("Video URL'yi girin: ")
download_path = input("Videoyu kaydetmek istediğiniz konumu girin: ")

try:
    yt = pytube.YouTube(video_url)
    stream = yt.streams.get_highest_resolution()

    video_title = yt.title
    print(f"'{video_title}' adlı video {download_path} konumuna indiriliyor...")
    stream.download(output_path=download_path)
    print("Video başarıyla indirildi.")
except pytube.exceptions.RegexMatchError:
    print("Geçersiz video URL'si. Lütfen doğru bir URL girin.")
except Exception as e:
    print(f"Hata oluştu: {e}")