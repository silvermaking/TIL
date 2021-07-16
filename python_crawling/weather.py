#https://www.metaweather.com/api/
import requests

url = 'https://www.metaweather.com/api/location/1132599/'

# 영어 -> 한글을 위한 dict
dic = {'Light Rain' : '약간의 비가 옵니다.', 'Heavy Rain' : '많은 비가 옵니다.',
'Heavy Cloud' : '구름이 많겠습니다.', 'Light Cloud' : '구름이 조금 있겠습니다', 'Showers' : ' 폭우가 옵니다'}

responses = requests.get(url).json()  # json() -> dict 형식으로 변환

daily_wtr = responses['consolidated_weather'] #날씨
for i in range(6):
    wtr = daily_wtr[i]["weather_state_name"]
    wtr_kr = dic[wtr]                       #날씨 한글 변환
    min_temp = daily_wtr[i]["min_temp"]     #온도
    min_temp = round(min_temp, 2)           #소수점 2자리까지
    max_temp = daily_wtr[i]["max_temp"]
    max_temp = round(max_temp, 2)
    date  = daily_wtr[i]['applicable_date']
    
    print(f'{date} 서울 날씨의 최고 기온은 {max_temp}도,\
최저 기온은 {min_temp}도 이며,{wtr_kr}')


# city = responses['title']
# print(date)
