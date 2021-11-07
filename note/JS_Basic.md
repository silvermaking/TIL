# JS 기초문법



## 1. 변수와 식별자

- 식별자는 변수를 구분할 수 있는 변수명
- 문자, $, _ 로 시작
- 대소문자 구분, 클래스명 외에 모두 소문자
- 예약어 사용 X , FOR, IF, CASE 등
- 호이스팅 되는 특성 - var
  - 변수 선언 이전에 참조할 수 있음
  - `undefined` 반환



## 2. 데이터 타입

- 모든 값은 데이터 타입 가짐
- primitive type , reference 타입
- 숫자, 불리언, null, undefined, /  objects, array, function 등

- 변수에 복사할 때 실제값  /  찾모 값이 복사
- 숫자 : 부동소수점, NaN 

- `null` 은 원시타입이지만 typeof 는 object로 나옴(버그) - [참고](https://2ality.com/2013/10/typeof-null.html)



## null VS undefined

- null
  - 빈 값
  - 의도적으로 할당

- undefined
  - 빈 값
  - 변수 선언시 아무 값도 할당하지 않을 때 자동으로 할당
  - typeof => undefined
  - NaN => number



## 자동 형변환

- 거짓
  - undefined, null, NaN, string(빈 문자열), 0, -0

## 연산자

### `==` 

- 암묵적 타입 변환을 통해 타입 일치시킨후 같은 값인지 비교
- 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

### `===`

- 엄격한 비교, 타입 변환  X
- 타입, 값 모두 같은지 비교



&&, ||(or), | (not)

- false&&true => false
- true&& flase => true

### 삼항연산자

- console.log(true ? 1: 2)
- 앞에께 조건식이 참이면 : 앞에껄 아니면 뒤에껄 반환



## 3. 조건문

- switch
  - 결과값과 case 문의 오른쪽 값 비교
  - break 문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

### 반복문

- for_in 
  - 객체 속성들을 순회
  - 인덱스 순으로 순회 보장 x
- for_ of
  - 반복 가능한(inerable) 객체를 순회
  - array, map, set,string 등



# 4. 함수

- reference, function 타입
- 일급 객체 , 변수할당, 함수매개변수전달, 반환값사용가능



### 선언식

- 호이스팅
- 익명 함수 x



### 표현식

- 익명함수
- 호이스팅 x
- 변수로 평가, scope규칙 따름



## 5. 배열과 객체

- 참조 타입의 객체

- 메서드 호출시 인자로 callback 함수를 받음
  - 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수



- forEach : 하나씩 실행, 반환값 x
- map: 함수의 반환ㄱ 값을 요소로 하는 새로운 배열, 기존 배열 전체를 다른 형태로 바꿀 때
- filter: 함수의 반환 값이 참인 요소들만 모아서 , 기존 배열 필터링할 때 
- reduce: 하나의 값(acc)에 누적후 반환, 빈 배열의 경우 initialValue 제공하지 않으면 에러 발생
- find: 반환 값이 참이면 해당 요소를 반환,  찾는 값없으면 undefined 반환
- some: 하나라도 판별 함수 통과하면 참 반환, 빈 배열은 거짓
- every: 모든 요소 통과하면 참, 빈배열은 참



## objects

- 속성의 집합, 중괄호 내부에 key, value 쌍으로 표현
- key : 문자열만
  - 띄어쓰기, 구분자 있으면 따옴표쓰기
- value 모든 타입
- 접근 점가능, 대괄호(따옴표쓸때)



### 구조분해할당

- 속성을 변수에 쉽게 할당
- const { name } = 할당할 거   , 여러개도 가능



### JSON

parse : 자바스크립트 객체로

stringify : json으로

