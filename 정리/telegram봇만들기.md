https://core.telegram.org/bots/api#authorizing-your-bot

# 1. **B**ot token

## 기본주소

```
<https://api.telegram.org/bot><token>
```

# 2. 요청 URL

메서드 : 내가 텔레그램에게 요청할 내용

[https://api.telegram.org/bot<token>/](https://api.telegram.org/bot<token>/)`getme`

## 챗봇 최신 내역 가져오기

> base주소/getUpdates 중요! 여기에 있는 chat id 를 메시지에 사용해야함

[https://api.telegram.org/bot<token>/](https://api.telegram.org/bot<token>/`getme`)`getUpdates`

## 메세지 보내기

> base주소/sendMessage?chat_id={}&text={}

https://api.telegram.org/bot<token>/sendMessage?chat_id={}&text={}

# 3. 실습

### 실습 1 - lotto 모듈 이용해보기

- 내가 만든 

  lotto.py

   활용하기

  - 모듈화를 하려면 함수로 만들어주기

```python
#로또 번호 6개 추첨 코드 
from random import sample

def get_lotto_num():
    numbers = range(1, 46)
    pick = sorted(sample(numbers, 6))
    return pick
```

- 챗봇 실습
  - `import lotto` 로 [lotto.py](http://lotto.py) 모듈 요청
  - `lotto.get_lotto_num()` 로 로또 번호 부르기

```python
# 요청
import requests
# 내가 만든 lotto.py 요청
import lotto

# 1. 사용자 정보 가져오기
url = f'<https://api.telegram.org/bot1882036665:AAGtsYH6YOQvXNglv8VcV6mwIyWYTzIrAp4/>'

# /getUpdates로 요청 보내서,
url_getup = url + f'getUpdates'
response = requests.get(url_getup).json()

# chat_id에 해당하는 값을 저장
chat_id = response['result'][0]['message']['from']['id']

# 2. 메세지 보내기
# /sendMessage?chat_id={위에서가져온값}&text={원하는 값}

message  = f'오늘의 로또번호는 {lotto.get_lotto_num()} 입니다'
# message = input()
url_send = url + f'sendMessage?chat_id={chat_id}&text={message}'
response_send = requests.get(url_send).json()

# 챗봇에서 확인 가능
```

## 실습2 - 명언 번역

- https://www.pythonanywhere.com/ 가입
- https://developers.naver.com/apps/#/wizard/register  네이버 api 신청

> **배포(deployment)** : 서버/웹페이지 를 외부(서버)에 올리는 행위 pythonanywhere, heroku, AWS EC2 등이 있다.