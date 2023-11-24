print(""""
******************************
MÜKEMMEL SAYI HEPSALAMA
******************************
""")

sayi = int(input("LÜTFEN BİR SAYI GİRİNİZ : "))
i =1
toplam =0
while i<sayi:
    if sayi % i ==0:
        toplam +=i
    i +=1
if toplam == sayi:
    print(sayi,"MÜKEMMEL BİR SAYI...")
else:
    print(sayi,"MÜKEMMEL BİR SAYI DEĞİLDİR...")


