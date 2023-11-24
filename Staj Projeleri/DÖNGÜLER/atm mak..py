print(""""
***************************
ATM MAKİNESİNE HOŞGELDİNİZ

1. BAKİYE SORGULAMA

2. PARA YATIRMA

3. PARA ÇEKME

PROGRAMDAN ÇIKMAK İÇİN q YA BASINIZ
***************************
""")

bakiye =1000
while True:
    işlem = input("İşlemi Seçiniz : ")
    if işlem =="q":
        print("YİNE BEKLERİZ")
        break
    elif işlem=="1":
        print("Bakiyeniz {} TL dir".format(bakiye))
    elif işlem=="2":
        miktar=int(input("Miktarı giriniz : "))
        bakiye += miktar
    elif işlem=="3":
        miktar = int(input("Miktarı giriniz : "))
        if bakiye - miktar<0:
            print("Böyle bir miktar çekemezsiniz")
            continue
        bakiye -= miktar
    else:
        print("GEÇERSİZ İŞLEM")