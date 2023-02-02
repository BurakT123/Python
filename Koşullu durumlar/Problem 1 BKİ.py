boy = float(input("Boyunuzu m cinsinden giriniz : "))
kilo=int(input("Kilonuzu sayı cinsinden girinniz : "))

BKI=kilo/boy*boy

if BKI < 18.5 :
    print("Zayıf")
elif BKI<25:
    print("Normal")
elif BKI< 30:
    print("Fazla kilolu")
elif BKI>30:
    print("Obez")

