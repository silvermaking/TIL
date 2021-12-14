# bash: jupyter: command not found

- window 환경에서 git bash 에서 위와 같은 에러가 발생



## 에러의 원인

- 다른 윈도우 사용자 계정에서 jupyter notebook을 설치했기 때문
  - c\사용자\ 경로에 설치됨
- 환경변수에서 jupyter을 찾지 못함



## 해결

- 윈도우 계정의 관리자 계정이 아닐 경우 jupyter notebook은보통 아래와 같은 경로에 설치됨
  - `C:\Users\SSAFY_eunseong\AppData\Roaming\Python\Python39\Scripts`
  - `C:\Users\SSAFY_eunseong\AppData\Local\Python\Python39\Scripts`

- 이 경로를 시스템 환경 변수 편집에서 Path에 추가

![image](md-images/146025738-388ad116-e1a0-413f-9fb7-587b2934b380.png)

