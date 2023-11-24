print("""
**********************
PROGRAMDAN ÇIKMAK İÇİN q YA BASINIZ!!! 
**********************
""")


toplam=0
while True:
    sayi=input("Sayı giriniz : ")


    if sayi=="q":
        break
    sayi = int(sayi)
    toplam += sayi


print("TOPLAM :",toplam)
