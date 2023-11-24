a = 2 # Blok 1 e ait kod


if(a == 2):
    print(a)#Blok 2 ye ait kod
print("merhaba")# Blok 1 e ait kod





# 18 yaş kontrolü


yas = int(input("Yaşınızı giriniz : "))

if yas<18:
    #if bloğu - girinti ile sağlanır
    print("18 YAŞINDAN KÜÇÜK")
else:
    print("18 YAŞINDAN BÜYÜK VEYA 18 YAŞINDA")


sayı = int(input("Sayı giriniz : "))

if sayı <0 :
    print("Negatif")
else:
    print("Pozitif")


# if elif else koşulları
# else yazılması zorunlu değildir
# ne kadar koşul varsa o kadar elif yazılabilir

islem = input("işlem giriniz: ")

if islem == "1":
    print("İşlem bir seçildi")
elif islem == "2":
    print("İşlem bir seçildi")
elif islem== "3":
    print("İşlem bir seçildi")
elif islem=="4":
    print("İşlem bir seçildi")
else:
    print("Geçersiz işlem")




# HARF NOTU HESAPLAMA

note = float(input("Notunuzu giriniz : "))

if note >=90:
    print("AA")
elif note>=85:
    print("BA")
elif note>=80:
    print("BB")
elif note >= 75:
    print("CB")
elif note >=70:
    print("CC")
elif note>=65:
    print("CC")
elif note>=60:
    print("DC")
else:
    print("Kaldınız!!")







