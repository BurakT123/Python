for a in range(1,11):
    print(a)
""""a bir değer değil tanım sadece"""

for i in range(1, 20, 2):
    print(i)
""""2 Atlama değerini ifade ediyor"""

for i in range(30, 3, -3):
    print(i)
"""" -3 tersten 3'lü başla anlamına geliyor"""

sehirler = ["Denizli", "Sakarya", "Konya"]
for i in sehirler:
  print(i)

toplam = 0
for i in range(1, 100):
    toplam += i
print(toplam)

"""" 1 den 100e kadar olan sayıların toplamı 100 hariç"""



kelime = input("Bir kelime giriniz = ")
for harf in kelime:
    print(harf)

""""Girilen kelimeyi alt alta harf harf yazıyor"""