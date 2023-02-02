liste = [1,2,3,4,5]

liste2= list()

for i in liste:
    liste2.append(i)
print(liste2)


print("                                                                     ")


liste3=[1,2,3,4,5,6]

liste4 = [b for b in liste3]
print(liste4)


print("                                                                     ")


liste1 = [1,2,3,4,5,6]

liste5 = [a*2 for a in liste1]
print(liste5)

print("                                                                     ")

liste6 = [(1,2),(3,4),(5,6)]
liste7 =[i *j for i,j in liste6]

print(liste7)

print("                                                                     ")

s = "Python"
liste8 =[i*3 for i in s]
print(liste8)

print("                                                                     ")


liste9=[(1,2,3),(4,5,6,7,8),(9,10,11,12,13,14,15)]
liste10 = list()
for d in liste9:
    for x in d:
        print(x)
        liste10.append(x)
print(liste10)

print("                                                                     ")

#List COMPREHENSİON

liste11=[[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste12 =[e for k in liste11 for e in k]
print(liste12)
