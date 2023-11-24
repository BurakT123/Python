import requests
from bs4 import BeautifulSoup

def get_clinic_name(clinic_id):
    url = 'https://tr.wikipedia.org/wiki/Anasayfa'

    response = requests.get(url)

    html = response.text

    soup  = BeautifulSoup(html, 'html.parser')

    #len(soup.find_all('h1'))
    #soup.find_all('h1')[1].text.strip()
    clinic_name = soup.find_all('div')
    return clinic_name

get_clinic_name()

start = (1)
end = (5)
for clinic_id in range (start,end):
    print(clinic_id)