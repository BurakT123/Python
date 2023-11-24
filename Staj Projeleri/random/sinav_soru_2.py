
a =int(input("BİR SAYI DEĞERİ GİRİNİZ : "))
asal = True
if a == 1:
    print("Asal değildir")
for i in range(2,a):
    if (a % i ==0):
        print("Asal değil")
        break
    else:
        print("Asal")
        break
b= int(input("BİR SAYI DEĞERİ GİRİNİZ : "))
if b == 1:
     print("Asal değildir")

for i in range(2,a):
    if (b % i ==0):
        print("Asal değil")
        break
    else:
        print("Asal")
        break
c = int(input("BİR SAYI DEĞERİ GİRİNİZ : "))
if c == 1:
    print("Asal değildir")
for i in range(2,a):
    if (c % i ==0):
        print("Asal değil")
        break
    else:
        print("Asal")
        break


