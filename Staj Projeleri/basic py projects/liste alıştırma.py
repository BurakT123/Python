
liste1=[1,3,2,5,6]
print(liste1)

liste2=[7,8,95,4]
print(liste2)

liste3=[liste1+liste2]
print(type(liste3),liste3)

print(len(liste2))


liste4="merhaba"
print(list("merhaba"))

print(liste4[1])

print(liste4[:3])
print(liste4[2::-1])
print(liste4[::3])
print(liste4[::2])
print(liste3*2)

liste2[1]=9
print(liste2)


liste5=[0,1,2,3]


print(liste5.pop(1))
print(liste5.append(99))


liste6=["selam","merhaba","naber"]
print(liste6.sort(reverse=True))
