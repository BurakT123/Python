"""
def fonksiyon_adi(parametre1,parametre2,...(opsiyonel)):
    fonksiyon bloğu
    yapılacak işlemler
    dönüş değeri - Opsiyonel

"""


def selamla():
    print("Merhaba...")
    print("Nasılsınız?")


selamla()


def selamla(isim):
    print("İsminiz : ", isim)


selamla("Kemal")
selamla("Serdar")


def toplama(a, b, c):
    print("Toplamları : ", a + b + c)


toplama(9, 8, 7)


def faktoriyel(sayi):
    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        print("Faktoriyel : ", faktoriyel)
    else:
        while sayi > 1:
            faktoriyel *= sayi
            sayi -= 1

        print("Faktöriyel : ", faktoriyel)


faktoriyel(5)
