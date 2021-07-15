 # https://nationalize.io/
import requests

names = ['tak', 'tony', 'eric', 'musk']
# url = f'https://api.nationalize.io/?name=michael'
url = 'https://api.nationalize.io/?'

for name in names:
    url += f'name[]={name}&'
    # print(url)
responses = requests.get(url).json()  # json() -> dict 형식으로 변환
for response in responses:
    # print(response)
    if len(response['country']) > 0:
        nation = response['country'][0]['country_id']
        name = response['name']
        print(name, nation)

    else:
        print(response['name'], '화성 갈끄니까~')


### 
#list는 index 번호로 
#dict는 key로 접근
'''

url = 'https://api.nationalize.io/?name=michael'

response = requests.get(url)
print(response)
result = response.json()
print(result)
print(result['country'][0]['country_id'])

'''