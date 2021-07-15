import requests
from bs4 import BeautifulSoup

# 1. url 요청 및 response 
url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text

# 2. 문서를 구조화
data = BeautifulSoup(response, 'html.parser')

# 3. 선택자를 활용하여 정보 가져오기
dollar = data.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value').text

print(f'달러 환율은 {dollar}입니다')
# string-interpolation (문자열 보간법)
# 문자열 사이에 변수 값을 넣는 방법
# f-string : python 3.6 + 동작
# SWEA에서는 동작하지 않습니다. 