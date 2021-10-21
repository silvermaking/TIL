# DB_05_HomeWork

## 1. MTV

MTV 는 Model-Template-View의 약자이다.

- Model
  - MVC 패턴의 모델에 대응되며 **DB에 저장되는 데이터**를 의미
  - 모델은 클래스로 정의되며 하나의 클래스가 하나의 DB Table
  - ORM기능을 지원하기 때문에 파이썬 코드로만 DB 조작 가능
- Template
  - MVC 패턴의 View에 대응되며 **유저에게 보여지는 화면**을 의미
  - 장고는 view에서 로직을 처리한 후 html 파일을 context와 함께 렌더링한다
  - html 파일을 템플릿이라고 지칭
  - django template 문법을 지원해서 context로 받은 데이터를 활용할 수 있음

- View
  - MVC 패턴의 컨트롤러에 대응되며 **요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답함**
  - URL 설계를 통해 URL과 View를 매핑하는 단계가 있음



## 2. 404 Page not found

(a) : articles

(b) : views

(c) : views.index



## 3. templates and static

(a) : settings.py

(b) : TEMPLATES

(c) : STATICFILES_DIRS



## 4. migration

1) makemigrations : 마이그레이션 생성
2) showmigrations : 마이그레이션 DB 반영 여부 확인
3) sqlmigrate : 마이그레이션에 대응되는 SQL 문 출력
4) migrate : 마이그레이션 파일의 내용을 DB 에 최종 반영



## 5. ModelForm T or F

1)  POST 와 GET 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다. (F) ,  동작 방식에도 차이가 있다.
   - GET 은 데이터를 URL에 붙여서 보냄
   - POST 방식은 BODY에 데이터를 넣어서 보냄

2. ModelForm 과 Form Class 의 핵심 차이는 Model 의 정보를 알고 있는지의 여부이다. (T)
3. AuthenticationForm 은 User 모델과 관련된 정보를 이미 알고 있는 ModelForm 으로
   구성되어 있다. (F)
   - Form 으로 구성되어있다.
4. ModelForm 을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다. (T)
   - fields 나 exclude 를 작성해야 함

## 6. media 파일 경로

사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 crud) 내부의
/uploaded_files 폴더로 지정하고자 한다 .
이 때 , settings.py 에 작성해야 하는 설정 2 가지를 작성하시오

```python
MEDIA_ROOT = BASE_DIR / 'uploaded_files'

MEDIA_URL = '/uploaded_files/'
```



## 7. DB T or F

1) RDBMS 를 조작하기 위해서 SQL 문을 사용한다. (T)
2) SQL 에서 명령어는 반드시 대문자로 작성해야 동작한다 . (F)
   - SQL 명령어를 명시하기 위해 대문자를 권장하지만 소문자도 동작한다.
3) 일반적인 SQL 문에서는 세미콜론 ( ; )까지를 하나의 명령어로 간주한다. (True)
4) SQLite 에서 tables, .headers on 과 같은 dot( . ) 로 시작하는 명령어는 SQL 문이 아니다 . (T)
5) 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다. (F)
   - 자료구조에 따라 N개의 테이블이 존재할 수 있다.



## 8. on_delete

(a) : PROTECT

- PROTECT : 해당 요소가 같이 삭제되지 않도록 ProtectedError를 발생시킨다.



## 9. Like in models

(a) : ManyToManyField

(b) : related_name



## 10. Follow in models

- 중개 테이블 이름 : accounts_user_followings

- from_user_id, to_user_id
