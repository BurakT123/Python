print(""""
***************************
FAKTÖRİYEL BULMA PROGRAMI



ÇIKMAK İÇİN q YA BASINIZ!!!
***************************
""")

while True:
    sayi = input("Sayı : ")
    if sayi =="q":
        print("PROGRAM SONLANDIRILIYOR...")
        break
    else:
        sayi =int(sayi)

        faktoriyel =1

        for i in range(2,sayi+1):

            faktoriyel *= i

            print("Faktöriyel :  ",faktoriyel)



        