"""başlangıç ve bitiş değeri girilen 1-100 arasındaki sayıların toplamını bulun"""

i =int(input("başlangıç değerini giriniz: "))
c =int(input("bitiş değeri giriniz: "))
t=0
for a in range(i,c):
    t = t+a
print("Toplam = ",t)
if i>c:
    for a in range(i,c,-1):
        t = t + a
    print("Toplam = ", t)
