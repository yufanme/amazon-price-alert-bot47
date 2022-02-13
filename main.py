import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/Kindle-Paperwhite-Waterproof-International/dp/B07741S7Y8/ref=sr_1_2?crid=" \
      "3MO08AY697FAM&keywords=kindle+paperwhite&qid=1644749815&sprefix=kindle%2Caps%2C355&sr=8-2"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50",
           "Accept-Language": "en"}

response = requests.get(url=URL, headers=headers)
amazon_web = response.text
# print(amazon_web)

soup = BeautifulSoup(amazon_web, "lxml")
# print(soup.prettify())
price = soup.find(name="span", class_="a-size-medium")
# class="a-price a-text-price  "
print(price)
