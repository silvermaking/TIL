# DB_01_WS : SQL & ORM

- toc
{:toc}



## 1. SQL Query

### 1) countries 테이블을 생성하시오

```sql
CREATE TABLE countries (
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);
```

### 2) 데이터를 입력하시오

```sql
INSERT INTO countries VALUES 
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);
```

### 3) 테이블의 이름을 hotels 로 변경하시오

```sql
ALTER TABLE countries RENAME TO hotels;

```



### 4) 객실 가격을 내림차순으로 정렬하여 상위 2 개의 room_num 과 price 를 조회하시오
```sql
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

```
### 5) grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오
```sql
SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

```
### 6) 객실의 위치가 지하 혹은 등급이 deluxe 인 객실의 모든 정보를 조회하시오
```sql
SELECT * FROM hotels where grade='deluxe' OR room_num LIKE 'B%';

```
### 7) 지상층 객실이면서 2020 년 1 월 4 일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오
```sql
SELECT room_num FROM hotels where check_in='2020-01-04' 
and room_num NOT LIKE 'B%' ORDER BY price ASC;
```



----

## 2. SQL ORM 비교하기

- 기본셋팅 (`.json` 파일 받아오기)

```bash
$ python manage.py migrate
$ python manage.py loaddata users/users.json
```



### 1. user 테이블 전체 데이터를 조회하시오

- SQL

```sql
SELECT * FROM users_user;
```

- ORM

```shell
User.objects.all()
```

### 2. id 가 19 인 사림의 age 를 조회하시오 .

- SQL

```sql
SELECT age FROM users_user WHERE id = 19;
```

- ORM

```shell
User.objects.filter(pk=19).values('age')
```

### 3. 모든 사림의 age 를 조회하시오 .

- SQL

```sql
SELECT age FROM users_user;
```

- ORM

```shell
User.objects.all().values('age')
```
### 4. age가 40 이하인 사림들의 id 와 balance 를 조회하시오.

- SQL

```sql
SELECT id, balance FROM users_user WHERE age <= 40;
```

- ORM

```shell
User.objects.filter(age__lte=40).values('pk', 'balance')
```

### 5. last_name 이 ‘김’이고 balance 가 500 이상인 사람들의 first_name 을 조회하시오 .

- SQL

```sql
SELECT first_name FROM users_user
WHERE last_name = '김' AND balance >= 500;
```

- ORM

```shell
User.objects.filter(last_name='김', balance__gte=500).values('first_name')
```

### 6. first_name 이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance 를 조회하시오 .

- SQL

```sql
SELECT balance FROM users_user 
WHERE first_name LIKE '%수' AND country = '경기도';
```

- ORM

```shell
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```

### 7. balance 가 2000 이상이거나 age 가 40 이하인 사람의 총 인원수를 구하시오 .

- SQL

```sql
SELECT COUNT(*) FROM users_user 
WHERE balance >= 2000 OR age <= 40;
```

- ORM
  - Q사용

```shell
User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()
```

### 8. phone 앞자리가 010’ 으로 시작하는 사람의 총원을 구하시오 .

- SQL

```sql
SELECT COUNT(*) FROM users_user 
WHERE phone LIKE '010%';
```

- ORM

```shell
User.objects.filter(phone__startswith='010').count()
```

### 9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오

- SQL

```sql
UPDATE users_user SET country = '경기도'
WHERE first_name = '옥자' AND last_name = '김';

SELECT country FROM users_user 
WHERE first_name = '옥자' AND last_name = '김';
```

- ORM

```shell
user = User.objects.get(first_name='옥자', last_name='김')
user.country = '경기도'
user.save()
```

### 10. 이름이 ‘백진호’인 사람을 삭제하시오 .

- SQL

```sql
DELETE FROM users_user
WHERE first_name = '진호' AND last_name = '백';

SELECT country FROM users_user 
WHERE first_name = '진호' AND last_name = '백';
```

- ORM

```shell
user = User.objects.get(first_name='진호', last_name='백').delete()
```

### 11.balance 를 기준으로 상위 4 명의 first_name, last_name, balance 를 조회하시오

- SQL

```sql
SELECT first_name, last_name, balance FROM users_user 
ORDER BY balance DESC LIMIT 4;
```

- ORM
  - 둘다 됨

```shell
User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]
```
```shell
User.objects.order_by('-balance')[:4].values('first_name', 'last_name', 'balance')
```
### 12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오. 

- SQL

```sql
SELECT * FROM users_user
WHERE phone LIKE '%123%' AND age < 30;
```

- ORM

```shell
User.objects.filter(phone__contains='123' ,age__lte=30).values()
```

### 13. phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오. 

- SQL

```sql
SELECT DISTINCT country FROM users_user 
WHERE phone LIKE '010%';
```

- ORM

```shell
User.objects.filter(phone__startswith='010').values('country').distinct()
```

### 14. 모든 인원의 평균 age를 구하시오. 

- SQL

```sql
SELECT AVG(age) FROM users_user;
```

- ORM

```shell
from django.db.models import Avg
User.objects.aggregate(Avg('age'))
```

### 15.  박씨의 평균 balance를 구하시오. 

- SQL

```sql
SELECT AVG(balance) FROM users_user 
WHERE last_name = '박';
```

- ORM

```shell
from django.db.models import Avg
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```

### 16.경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

- SQL

```sql
SELECT MAX(balance) FROM users_user 
WHERE country = '경상북도';
```

- ORM

```shell
from django.db.models import Max
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```

### 17.제주특별자치도에 사는 사람 중 balance 가 가장 많은 사람의 first_name 을 구하시오 .

- SQL

```sql
SELECT first_name FROM users_user 
WHERE country = '제주특별자치도' ORDER BY balance DESC LIMIT 1;
```

- ORM

```shell
User.objects.filter(country='제주특별자치도').order_by('-balance')[:1].values('first_name')
```

