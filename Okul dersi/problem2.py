"""bir öğrencinn vize ve final notları girildiğinde ortalamasını hesap ederek
 ortalama 50nin altında ise öğrencinin durumunu ve ortalamasını gösterecek"""
"""ortalama değeri 0-49 ise ff  50-57 ise dd 58-64 dc 65-74 cc"""







x = int(input("Lütfen 1. dersi yazınız:  \n"))
y = int(input("Lütfen 2. dersi yazınız:  \n"))


ort = int((x + y ) / 2)
if ort < 50:
    durum = "Kaldı"
elif ort == 50:
    durum = "50 ile geçti..."
else:
    durum = "Geçti"

if ort < 50:
    kod= "FF"
elif ort < 58:
    kod = "DD"
elif ort < 65:
    kod = "DC"
elif ort < 75:
    kod = "CC"

print("Durum:", durum)
print("Ortalaması:", ort)
print("Ortalamasının puanı:",kod)