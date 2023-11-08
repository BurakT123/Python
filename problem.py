"""a ve b gibi 2 farklı sayının 4 işlemini yapıp sonuçları ekrana çıkartan"""
a=int(input("Bir sayı giriniz: "))
b=int(input("Bir sayı giriniz: "))

if a>b :
    toplam = a + b
    cıkarma = a - b
    carpma = a * b
    bolme = a / b
else:
    if a<b:
        toplam = a + b
        cıkarma = a - b
        carpma = a * b
        bolme = a / b
    else:
        b = int(input("Lütfen farklı bir sayı giriniz: "))
        toplam = a + b
        cıkarma = a - b
        carpma = a * b
        bolme = a / b
print(toplam)
print(cıkarma)
print(carpma)
print(bolme)