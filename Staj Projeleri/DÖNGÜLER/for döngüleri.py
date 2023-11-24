liste = [1,2,3,4,5,6,7]

for eleman in liste:
    print(eleman)
print("                                                                         ")





liste1 =[1,2,3,4,5,6,7,8]
toplam=0
for eleman1 in liste1:
    toplam=toplam+eleman1
    print("Toplam : {} Eleman : {}".format(toplam,eleman1))
print("TOPLAM : ",toplam)
print("                                                                         ")


liste2=[1,2,3,4,34,54,63,72]
for eleman2 in liste2:
    if eleman2 % 2==0:
        print(eleman2)
print("                                                                         ")


s = "Python"

for i in s:
    print(i)
print("                                                                         ")

for i in s:
    print(i *3)
print("                                                                         ")

demet =(1,2,3,4,5,6)
for a in demet:
    print(a)
print("                                                                         ")
liste3 =[(1,2),(3,4),(5,6),(7,8)]
for eleman3 in liste3:
    print(eleman3)
print("                                                                         ")
for (i,j) in liste3:
    print("i : {}  j : {}".format(i,j))
print("                                                                         ")


liste4 = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for (i,j,k) in liste4:
    print("i : {} j : {}  k : {}")
print("                                                                         ")

liste5 = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for (i,j,k) in liste5:
    print(i * j *k)

print("                                                                        ")

sözlük = {"bir":1 ,"iki":2,"üç":3,"dört":4}
sözlük.keys()

sözlük.values()

print("                                                                         ")

#BÖYLE YAPILINCA OLMAZ SADECE ANAHTAR KELİMELERİ VERİR
for eleman5 in sözlük:
    print(eleman5)

print("                                                                         ")
for eleman6 in sözlük.values():
    print(eleman6)

print("                                                                         ")

sözlük.items()
for i,j in sözlük.items():
    print("Anahtar : ",i,"Değer : ",j)
