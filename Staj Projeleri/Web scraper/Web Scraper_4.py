import requests
from bs4 import BeautifulSoup

url = "https://www.python.org"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#üst_baslik_etiket = soup.find('a', class_='current_item selectedcurrent_branch selected')

üst_baslik_etiket = soup.find('ul', class_='menu')
üst_baslik_etiket_= üst_baslik_etiket.find('a', class_ ='current_item selectedcurrent_branch selected').text

print("Üst Başlık:",üst_baslik_etiket_)
