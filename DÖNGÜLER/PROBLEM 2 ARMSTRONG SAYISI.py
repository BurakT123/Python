sayi= input("Sayı : ")
basamak_sayisi=len(sayi)
sayi =int(sayi)
basamak=0
toplam =0

gecici_sayi=sayi

while gecici_sayi>0:
    basamak = gecici_sayi % 10
    toplam +=basamak ** basamak_sayisi
    gecici_sayi //=10

if toplam ==sayi:
    print(sayi,"ARMSTRONG SAYI")
elif toplam !=sayi:
    print(sayi,"ARMSTRON SAYI DEĞİL")


