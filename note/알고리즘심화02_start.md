# Start

## 0. 학습목표

- SW문제 해결 역량이란 무엇인가를 이해하고 역량을 강화하는 방법을 이해한다.
- 효율적인 알고리즘의 필요성을 이해하고 알고리즘의 성능 측정 방법 중 하나인 **시간복잡도**에 대해 이해한다.
- 프로그램을 작성하기 위한 기본 중 **표준 입출력 방법**에 대해 이해한다.
- 비트 수준의 연산과 알고리즘에 대해 이해한다.
- 컴퓨터에서의 실수 표현 방법에 대해 이해한다.

## 1. SW 문제 해결

### SW 문제 해결 역량이란?

- 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 방법
- 프로그래머가 사용하는 언어나 라이브러리, 자료구조, 알고리즘에 대한 지식을 적재적소에 퍼즐을 배치하듯 이들을 연결하여 큰 그림을 만드는 능력

## 2. 복잡도 분석

### 2-1.알고리즘이란?

- 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법
- 주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 간단하게 다시 말하면 **어떠한 문제를 해결하기 위한 절차**라고 볼 수 있다.

### 2-2. 표기

- O-표기는 복잡도의 점근적 상한을 나타냄
- $Ω$(Big-Omega)- 표기는 복잡도의 점근적 하한을 의미
  - 최소한 이만한 시간은 걸린다
- Θ(Theta)- 표기
  - O, Ω 가 같은 경우에 사용
  - 동일한 증가율을 가진다.

### O(Big-Oh)- 표기

- O-표기는 복잡도의 점근적 상한을 나타낸다.
- 복잡도가 $f(n) = 2n^2 -7n + 4$ d이라면, f(n)의 O-표기는 $O(n^2)$이다.

⇒ 단순히 "**실행시간이 $n^2$에 비례**" 하는 알고리즘이라고 말함

### O표기

O(1) : 상수 시간

O(logn) : 로그(대수) 시간  ex) 이진탐색

O(n) : 선형시간       ex)선형 탐색

O(nlogn) : 로그 선형시간  ex) 병합정렬

$O(n^2)$  : 제곱 시간    ex) 버블정렬

$O(n^3)$ : 세제곱 시간

$O(2^n)$ : 지수 시간     ex) 부분집합

## 3. 비트 연산

참고자료([코딩도장](https://dojang.io/mod/page/view.php?id=2460))

| &    | AND                                      |
| ---- | ---------------------------------------- |
| \|   | OR                                       |
| ^    | XOR(같으면 0, 다르면 1)                  |
| ~    | 단항 연산자, 피연산자의 모든 비트를 반전 |
| <<   | 비트 열을 왼쪽으로 이동                  |
| >>   | 비트 열을 오른쪽으로 이동                |



### `1<<n`

- 2^n 의 값을 갖는다.
- **원소가 n개일 경우의 모든 부분집합의 수**를 의미
- Poswer set(모든 부분 집합)
  - 공집합과 자기 자신을 포함한 모든 부분집합
  - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.

### **`i&(1<<j)`**

- 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.

### **1의보수, 2의보수**

5 = 00000101

- 5 = 00000011

### **<연습문제1>**

0 과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기

- 입력 예

lst = '0000000111100000011000000111100110000110000111100111100111111001100111'

### **엔디안(endianness)**

- 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법

- HW아키텍처마다 다름

- **주의 :** 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산 할 때 올바로 이해하지 않으면 오류를 발생 시킬 수 있다.

- 빅 엔디안

  - 보통 큰 단위가 앞에 나옴. 네트워크.

- 리틀 엔디안

  - 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터.

    ![endianness.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3e0d9aa8-3fa3-4344-9476-51ea8bb5d227/endianness.png)

------

## **5. 진수**

## **6. 실수**

### **실수의 표현**

- 컴퓨터는 실수를 표현하기 위해 부동 소수점(floating-point) 표기법을 사용
- 부동 소수점 표기 방법은 소수점의 위치를 고정시켜 표현하는 방식
  - 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밑수의 지수승으로 표현
  - 1001.0011 → 1.0010011 x $2^3$

### **실수를 저장하기 위한 형식**

- 단정도 실수(32비트)
- 배정도 실수(64비트)
- 