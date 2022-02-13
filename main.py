import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

URL = "https://www.amazon.com/Kindle-Paperwhite-Waterproof-International/dp/B07741S7Y8/ref=sr_1_2?crid=" \
      "3MO08AY697FAM&keywords=kindle+paperwhite&qid=1644749815&sprefix=kindle%2Caps%2C355&sr=8-2"
BUY_PRICE = 100


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50",
           "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,zh-TW;q=0.5"}

response = requests.get(url=URL, headers=headers)
amazon_web = response.text
# print(amazon_web)

soup = BeautifulSoup(amazon_web, "lxml")
# print(soup.prettify())
price_int = soup.find(name="span", class_="a-price-whole").getText()
price_decimal = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_int + price_decimal)
# print(price, type(price))
title = soup.find(name="span", id="productTitle").getText().strip()
# print(title)

if price <= BUY_PRICE:
    # send email
    EMAIL = "562937707@qq.com"
    PASSWORD = "bpyjiqjylklcbdhe"

    email_content = f"{title}.\nNow price is: {price}$.\nlink:{URL}".encode('ascii', errors='replace').decode('ascii')
    with smtplib.SMTP("smtp.qq.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Kindle's price is good!From bot.\n\n\n{email_content}")
        print("Email Sent.")
else:
    print(f"price is {price}.Too high!")


