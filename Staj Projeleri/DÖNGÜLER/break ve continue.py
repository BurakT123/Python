i =0

while i<10:
    if i ==5:
        break
    print("i : ",i)
    i += 1

print("                                                                     ")
liste = [1,2,3,4,5]

for i in liste:
    if i == 3:
        break
    print("İ nin değerleri : ",i)
    i +=1

print("                                                                     ")

#EĞER PROGRAMDA BİR DURDURMA KOMUTU YOK İSE SONSUZA KADAR TERKAR EDER TRUE
while True:
    isim = input("İsminizi giriniz (Çıkmak için q basınız) : ")
    if isim == "q":
        print("PROGRAMDAN ÇIKILIYOR...")
        break

print("                                                                     ")


print("                                                                     ")

liste =list[range(11)]
print(liste)

for i in liste:
    if i ==3 or i ==5:
        continue
    print("i : ",i)

print("                                                                     ")

#EĞER ÇALIŞTIRIRSAK SONSUZ DÖNGÜYE GİREBİLİR "KERNEL" TAKILI KALIR VE İLERLEMEZ
i = 0

while i<10:
    if i ==2:
        continue
    print("İ : ",i)
    i +=1

print("                                                                     ")


a = 0

while a<10 :
    if a ==2:
        a +=1  #ARTIRMA İŞLEMİ
        continue
    print("A : ",a)
    a +=1