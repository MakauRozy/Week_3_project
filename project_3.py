from bs4 import BeautifulSoup
import requests
import json
import re

URL= "https://books.toscrape.com/"
header= {"User-Agent": "Rozie practice cot. contact: rozie@gmail.com"}
response= requests.get(URL, headers=header, timeout=10)
soup= BeautifulSoup(response.content, "html.parser")
cards= soup.select(".product_pod")
#print(len(cards))

Target_currency = input("Convert prices to which currency? (e.g. KES, USD, EUR): ").upper()
url = 'https://v6.exchangerate-api.com/v6/b140136b73b01fe1f1869e24/latest/GBP'
reply = requests.get(url, timeout=10)
#print(reply.status_code)
data = reply.json()
#print(data)
rates = data["conversion_rates"]

if Target_currency not in rates:
    print(f"Sorry, '{Target_currency}' is not a valid currency code.")
    raise SystemExit
 
rate = rates[Target_currency]
print(f"1 GBP = {rate} {Target_currency}\n")


all_products=[]
for card in cards:
    title=card.select_one("h3 a")["title"]
    price = card.select_one(".price_color").text

    number = float(re.sub(r"[^\d.]", "", price))          # "£51.77" -> 51.77
    converted_price = round(number * rate, 2)                   # 51.77 * rate
    all_products.append({"title": title, "original_price": price,"converted_price":converted_price})
    print(f"{title} | {price} -> {converted_price} {Target_currency}")
    
