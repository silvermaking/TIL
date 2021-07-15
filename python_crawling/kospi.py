#0. requests 패키지를 가져온다.
import requests
from bs4 import BeautifulSoup

# 1. url 을 준비한다.
url = 'https://finance.naver.com/sise/'

# 2. 파이썬으로 요청을 보낸 결과를 저장
response = requests.get(url).text

# 3. 정보 추출을 위해서, 
data = BeautifulSoup(response)
kospi = data.select_one('#KOSPI_now')
print(kospi.text)

# #환율 추가
# url2 = 'https://finance.naver.com/marketindex/'
# response2 = requests.get(url2).text
# data1 = BeautifulSoup(response2)
# exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(exchange.text)
# #exchangeList > li.on > a.head.usd > div > span.value