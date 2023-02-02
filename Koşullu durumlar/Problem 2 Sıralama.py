a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz : "))
c = int(input("Üçüncü sayıyı giriniz : "))

if a>b :
    if b>c:
        print("a>b>c")
    else:
        print("a>c>b")
elif b>a:
    if a>c:
        print("b>a>c")
    else:
        print("b>c>a")
elif c>a:
    if a>b:
        print("c>a>b")
    else:
        print("c>b>a")
