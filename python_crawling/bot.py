# 요청
import requests
# import lotto

# 1. 사용자 정보 가져오기
url = 'https://api.telegram.org/bot1882036665:AAGtsYH6YOQvXNglv8VcV6mwIyWYTzIrAp4/'

# /getUpdates로 요청 보내서,
url_getup = url + 'getUpdates'
response = requests.get(url_getup).json()

# chat_id에 해당하는 값을 저장
chat_id = response['result'][0]['message']['from']['id']

# 2. 메세지 보내기
# /sendMessage?chat_id={위에서가져온값}&text={원하는 값}

# message  = f'오늘의 로또번호는 {lotto.get_lotto_num()} 입니다'
message = '안녕하세요'
url_send = url + f'sendMessage?chat_id={chat_id}&text={message}'
response_send = requests.get(url_send).json()
