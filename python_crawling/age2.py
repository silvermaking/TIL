'''
 tak, tony, eric, musk
4명의 나이 확인하는 코드
'''

# import requests

# url = ['https://api.agify.io/?name=tak', 'https://api.agify.io/?name=tony',
# 'https://api.agify.io/?name=eric', 'https://api.agify.io/?name=musk']

# for name in range(4):
#     response = requests.get(url[name]).json()
#     #print(response['age'])
#     print(f"{response['name']}의 나이는 {response['age']} 입니다")

# 상진수님 꺼 good!
import requests
# name = input('영문 이름 입력: ')
names = ['tak', 'tony', 'eric', 'musk']
# url = f'https://api.agify.io?name={name}&country_id=KR'
url = 'https://api.agify.io?'
for name in names:
    url += f'name[]={name}&'
responses = requests.get(url).json()  # json() -> dict 형식으로 변환
for response in responses:
    age = response.get('age')
    name = response.get('name')
    print(name, age)
