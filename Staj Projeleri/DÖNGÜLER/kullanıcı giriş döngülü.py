print("""
***********************************
KULLANICI GİRİŞİ PROGRAMI 
***********************************
""")

sys_kullanici_adi="murat"
sys_parola="12345"
giris_hakkı=3
while True:
    kullanici_adi=input("Kullanıcı Adı : ")
    parola =input("Parolanız : ")
    if kullanici_adi != sys_kullanici_adi and parola==sys_parola:
        print("KULLANICI ADI HATALI!!!")
        giris_hakkı -= 1
    elif kullanici_adi==sys_kullanici_adi and parola != sys_parola:
        print("PAROLA HATALI!!!")
        giris_hakkı -=1
    elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
        print("KULLANICI ADI VE PAROLA HATALI !!!")
        giris_hakkı -=1
    elif kullanici_adi==sys_kullanici_adi and parola ==sys_parola:
        print("SİSTEME BAŞARIYLA GİRİŞ YAPILDI...")
        break
    if giris_hakkı == 0:
        print("Giriş Hakkınız Bitti")
        break