# 요청 보내주는 requests 를 가져온다.
# 링크 https://agify.io/
import requests

# 1. url로 요청을 보낸 결과를 저장한다.
url = 'https://api.agify.io/?name=Jeongguk&country_id=KR'
response = requests.get(url).json()
response_text = requests.get(url).text

print(response)
print(type(response))  # dict이다.
print(response['age'])
print('===========')
print(response_text)
print(type(response_text))# type 이 str 이다. dict가 아님