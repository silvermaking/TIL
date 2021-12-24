# Java의 특징

- 모든 운영체제에서 실행 가능
- 객체 지향 프로그래밍
- 메모리 자동 정리
  - 자바는 메모리(RAM)를 자동 관리함
- 라이브러리 풍부



# JDK 설치

- 자바 개발도구(JDK, Java Development Kit) 설치

- [oracle](https://www.oracle.com/java/technologies/downloads/#jdk17-windows) 에서 다운로드



## 환경변수 설정

- JDK가 설치된 폴더를 일반적으로 JAVA_HOME 이라고 함

- 어떤 프로그램은 설치된 JDK의 위치를 찾을 때 JAVA_HOME 환경 변수를 이용

- 환경변수로 jdk 경로를 JAVA_HOME으로 등록해주는 것이 좋음

![image](https://user-images.githubusercontent.com/68841702/147345693-673b503f-cdc3-4f73-97c0-79e1ae280ae2.png)

- java/bin 경로 path에 추가
  - 자바소스 파일을 컴파일해주는 javac 명령어와 컴파일된 파일을 실행해주는 java명령어가 bin폴더에 있음
  - bin 폴더를 path에 추가해주어야 다른 폴더에서 실행 가능

![image](https://user-images.githubusercontent.com/68841702/147345853-9cf46a16-a6a8-4e39-821e-f6a75e6d5425.png)



# 이클립스 IDE 설치

- [이클립스](https://www.eclipse.org/downloads/)
- eclipse IDE for Enterprise Java and Web Developers 설치



### workspace 변경

- [file] - [Switch Workspace] - [Other]



### 이클립스 초기화 방법

- [Workspace]로 지정한 경로의 .metadata 삭제 후 재시작

> metadata
>
> - 색상, 테마, 폰트 등을 저장한 파일



### 퍼스펙티브 변경

- 초기는 JAVA EE 퍼스펙티브로 설정되어 있음
- 자바를 처음 할때는 JAVA로 해놓기
  - [window] - [perspective] -[open perspective] - [java]