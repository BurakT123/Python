yas = input("Kaç yaşındasın ? :")

if int(yas) <= 18:
    print("18 Yaşından Küçüksün.")

else:
    print("18 Yaşından Büyüksün.")

""""if 18 yaşından küçük eşitse doğru else(değilse) yanlış"""

sayi = int(input("Bir sayı giriniz"))

if (sayi / 2 == 0):
    print("Girilen sayı çifttir.")

else:
    print("Girilen sayı tektir.")

""""girilen sayının 2 ile bölümünden kalan 0 ise çift değilse tektir"""



print("Bölme işlemi için iki sayı giriniz")
bolum = int(input("1. Sayıyı giriniz = "))
bolen = int(input("2. Sayıyı giriniz = "))

if bolen != 0:
    print(bolum, "/", bolen, "=", bolum / bolen)

if bolen == 0:
    print("Sıfır ile bölme yapılamaz !")

""""Bölme işlemini  yaparken != operatörünü kullanarak sorgulamasını yaptırıyoruz. Eğer bölen, sıfırdan farklı ise doğrudur, değilse yanlıştır."""


soru = input("Karnın acıktı mı?")
if soru == "evet":
    print("O zaman yemek ye")

elif soru == "hayır":
    print("Acıkınca geri gel")

"""Birden fazla sorgulama yapmamız gerekiyorsa bu sefer “değilse eğer” sorgulamasını yapmamız gerekiyor."""





