import requests
from bs4 import BeautifulSoup

# Veri toplanacak web sayfasının URL'si
url ='https://www.plus.nl/product/plus-kruimige-aardappel-zak-3-kilo-792983'

# Web sayfasını almak için GET isteği yapılır
response = requests.get(url)

# Web sayfasının içeriği BeautifulSoup ile parse edilir
soup = BeautifulSoup(response.text,'html.parser')

# Tüm başlıkları (h1 etiketleri) bul
basliklar = soup.find('h1')

# Her başlığı ekrana yazdır
for baslik in basliklar:
    print(baslik.text)

