a = int(input("Vize notu 1 giriniz : "))
b= int(input("Vize notu 2 giriniz : "))
c = int(input("Final notu giriniz : "))

vize1=a*30/100
vize2=b*30/100
final=c*40/100

ort=final+vize1+vize2

if ort>=90:
    print("AA")
elif ort>=85:
    print("AB")
elif ort>=80:
    print("BB")
elif ort>=75:
    print("CB")
elif ort>=70:
    print("CC")
elif ort>=65:
    print("DC")
elif ort>=60:
    print("DD")
elif ort>=55:
    print("FD")
elif ort<55:
    print("FF")
