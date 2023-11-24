
import requests
from bs4 import BeautifulSoup 
import re
headers = {
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en, en-GB;q=0.9',
}
params = (
('page', '1') 
),
response = requests.get('https://www.porschevancouver.ca/inventory', headers-headers, params=params)
html = response.text
soup = BeautifulSoup (html, "html.parser")










<a class="vehicle-listing-lead-teaser popup-link" data-fancybox-href="/inventory/cta/Porsche+718+Boxster r+British+Columbia+2019+GT+Silver+Metallic+2106243? leadtext=Get+A+Quote &amp; page=1" data-fancybox-type="Quote"></a>

</div>
</div>
listing_colour = a_listing.find("div", {"class": : "vehicle-listing-exterior-color"}) listing_dict["listing_colour"] = re.sub("\t", ",listing_colour.text.strip())
listing_mileage_data listing_mileage_strip
=
=
a_listing.find("div", {"class": "vehicle-listing-mileage"})
listing_mileage_data.text.strip()
listing_mileage = int (listing_mileage_strip[:1])
=
listing_transmission a_listing.find("div", {"class": "vehicle-listing-transmission"}) listing_stock_number a_listing.find("div",{"class": "vehicle-listing-stock-number"}) listing_disp_price_data = a_listing.find("p",{"class": "vehicle-listing-display-price"}) listing_disp_price_strip = listing_disp_price_data.text.strip()
listing_disp_price_rep
listing_display_price =
=
listing_disp_price_strip.replace(", ", " ") float(listing_disp_price_rep[2:])
listing_dict["listing_mileage"]
=
listing_mileage
listing_dict["listing_transmission"] = listing_transmission.text.strip() listing_dict["listing_stock_number"] = listing_stock_number.text.strip() listing_dict["listing_display_price"]
=
listing_display_price