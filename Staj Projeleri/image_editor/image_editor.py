from PIL import Image, ImageEnhance, ImageFilter
import os
import glob

# Kullanıcıdan dosya konumunu alın
dosya_yolu = input("Lütfen dosyanın yolunu girin: ")

# Dizin yolundaki tüm resim dosyalarını bul
resimler = []
desteklenen_uzantilar = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

for uzanti in desteklenen_uzantilar:
    arama_yolu = os.path.join(dosya_yolu, uzanti)
    resimler.extend(glob.glob(arama_yolu))

if not resimler:
    print("Belirtilen uzantılara sahip resim dosyası bulunamadı.")
    exit()

for resim_yolu in resimler:
    # Resmi aç
    try:
        img = Image.open(resim_yolu)
    except IOError:
        print(f"{resim_yolu} dosyası açılamadı.")
        continue

    # Resim üzerinde istediğiniz düzenlemeleri yapabilirsiniz
    # Örnek olarak:
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Kaydedilecek dizin ve dosya adını belirtin
    kaydetme_dizini = 'C:/Users/buraq/PycharmProjects/Kodlama Egzersizleri/image_editor/edited'
    dosya_adi = os.path.basename(resim_yolu)

    # Eğer kaydetmek istediğiniz dizin farklı ise, yolunu doğru şekilde ayarlayın
    kaydetme_yolu = os.path.join(kaydetme_dizini, dosya_adi)

    # Düzenlenmiş resmi kaydedin
    edit.save(kaydetme_yolu)

    print(f"{dosya_adi} başarıyla düzenlendi ve {kaydetme_yolu} dizinine kaydedildi.")
