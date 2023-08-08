import requests
import pandas as pd
#from urllib.request.Request  둘중하나 사용하기 import requests를 사용해도된다.

from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
# requests.get(), requests.post()
# response.text
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

exchangeList = soup.select("#exchangeList > li")


#4개 데이터 수집
exchange_datas = []
baseUrl = "https://finance.naver.com"

for item in exchangeList: #4개국의 환율 정보 담긴 상위 변수  exchangeList
    data = {
        "title": item.select_one(".h_lst").text,
        "exchange": item.select_one(".value").text,
        "change": item.select_one(".change").text,
        "updown": item.select_one(".head_info.point_up > .blind").text,
        "link": baseUrl+ item.select_one("a").get("href")
    }
    exchange_datas.append(data)
df = pd.DataFrame(exchange_datas)
df.to_excel("./naverfinance.xlsx", encoding="utf-8")
