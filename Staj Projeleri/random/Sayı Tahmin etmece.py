from random import randint

rand = randint(1, 55)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 55 arasında bir sayı giriniz (0 çıkış): "))

    if sayi == 0:
        print("Oyunu iptal ettiniz.\nOyundan çıkılıyor ...")
        break
    elif sayi > 55:
        print("1 ile 55 arasında bir sayı giriniz lütfen!!!")
        continue   
    elif sayi < 0 :
        print("1 ile 55 arasında bir sayı giriniz lütfen!!!")
        continue   

    elif sayi < rand:
        print("Daha yüksek bir sayı giriniz.")
    elif sayi == rand:
        print(f"Doğru tahmin ettiniz. ({rand}) Tebrikler!!!")
        print(f"Oyun bitti. Toplam {sayac} tahminde bulundunuz.".format(sayac&rand))
        break
    elif sayi > rand:
        print("Daha düşük bir sayı giriniz.")
    else:
        print("Geçersiz giriş! Lütfen 1 ile 55 arasında bir sayı giriniz.")
    continue
