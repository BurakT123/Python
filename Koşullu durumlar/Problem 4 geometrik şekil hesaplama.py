print(""""
************************
1. Şekil Dörtgen

2. Şekil Üçgen 

************************
""")

sec = int(input("Dörtgen hesaplaması için 1 ,Üçgen hesaplaması için 2 yazınız :  "))

if sec==1:
    k1=int(input("1.Kenar değerini giriniz : "))
    k2=int(input("2.Kenar değerini giriniz : "))
    k3=int(input("3.Kenar değerini giriniz : "))
    k4=int(input("4.Kenar değerini iriniz : "))
    dortgen=k1+k2+k3+k4
    if dortgen>360:
        print("Dörtgen belirtmez...")
    elif dortgen<0:
        print("Dörtgen belirtmez")
    elif k1==90:
        if k2==90:
            print("BU BİR DİKDÖRTGENDİR...")
        elif k3==90:
            print("BU BİR KAREDİR...")
        elif k4==90:
            print("BU BİR KAREDİR...")
    elif k2==90:
        if k3==90:
            print("BU BİR DİKDÖRTGENDİR...")
        else:
            print("DEĞERLER KONTROL EDİLİYOR...")
            if k4 ==90:
                print("BU BİR DİKDÖRTGENDİR...")
    elif k3==90:
        if k4==90:
            print("BU BİR DİKDÖRTGENDİR...")
        else:
            print("BU BİR SIRADAN DÖRTGENDİR...")
    else:
        print("BU BİR SIRADAN DİKDÖRTGENDİR...")

elif sec==2:
    k5=int(input("1.Kenar değerini giriniz : "))
    if k5<=0:
        print("Üçgen belirtmez...")
        k6=int(input("2.Kenar değerini giriniz : "))
        if k6<=0:
            print("Üçgen belirtmez...")
        k7=int(input("3.Kenar değerini giriniz : "))
        if k7<=0:
            print("Üçgen belirtmez...")
        if k5 ==k6:
            if k6==k7:
                print("BU BİR EŞKENAR ÜÇGENDİR...")
            else:
                print("BU BİR İKİZKENAR ÜÇGENDİR...")
        elif k6==k7:
            if k7!=k5:
                print("BU BİR İKİZKENAR ÜÇGENDİR...")
        elif k7==k5:
            if k5!=k6:
                print("BU BİR İKİZKENAR ÜÇGENDİR...")

        else:
            print("BU BİR SIRADAN ÜÇGENDİR...")
