import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/-/zh_TW/dp/B082WNTTYL/ref=sr_1_12?dchild=1&keywords=apple+adapter&qid=1624172833&s=pc&sr=1-12"
headers = {
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
MY_EMAIL = "doe622134@gmail.com"
MY_PASSWORD = "4ea53766"

BUY_PRICE = 1548

response = requests.get(url=URL, headers=headers)


soup = BeautifulSoup(response.text, 'lxml')

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()
price_with_out_currency = price.split("US$")[1].replace(',',"")
print(price_with_out_currency)
price_as_float = float(price_with_out_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()


if price_as_float <= BUY_PRICE:

    price_string = str(price_as_float)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr="doe622134@gmail.com",
            to_addrs="doe622134@gmail.com",
            msg=f"Subject:Amazon Price Alert:\n\n{title} is now {price_string}"
    )