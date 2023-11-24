from random import *
import os
u_pwd =input ("Şifrenizi giriniz :")
pwd=['a','b','c','d','e','f','g','h','i','ı','j','k','l','m','n','o','ö','p','r','s','ş','u','ü','v','y','z','q','w','x','1','2','3'
,'4','5','6','7','8','9','0','*','_','-','?','&','%','+','^','!','/',',',':','.',';','¨¨','~','<','>','|','é',]

pw =""
while (pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd =pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)

        os.system("cls")
    print("Şifreniz :",pw)