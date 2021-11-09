- # Vue_02_CLI,Router

  # 1. SFC

  ## 1-1. Component

  - 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌
  - CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
  - 유지보수성, 재사용성성

  > Vue 컴포넌트 === Vue 인스턴스 === .vue 파일

  - 데이터와 processing(로직) 을 같이 할 수 있는 programing 방법으로서 class가 나옴
  - component based programming 방법론도 나왔지만 크게 성공 x
  - 현재는 컴포넌트로 구성된 프레임워크로 많이 사용

  ## 1-2. SFC(Single File Component)

  - Vue의 컴포넌트 기반 개발의 핵심 특징
  - 하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
  - 화면의 특정 영역에 대한 HTML, CSS, JS 코드를 하나의 파일(.vue)에서 관리
  - 즉, .vue 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식

  ## 1-3. Vue Component

  - 한 화면 안에서도 기능 별로 각기 다른 컴포넌트가 존재
    - 하나의 컴포넌트는 여러 개의 하위 컴포넌트를 가질 수 있음
    - Vue는 컴포넌트 기반의 개발 환경 제공
  - Vue 컴포넌트는 `const app = new Vue({...})` 의 app을 의미하며 이는 Vue 인스턴스

  # 2. Vue CLI

  - [DOC](https://cli.vuejs.org/)
  - Vue.js 개발을 위한 표준 도구
  - 프로젝트의 구성을 도와주는 역할 Vue 개발 생태계에서 표준 tool 기준을 목표로 함
  - 확장 플러그인, GUI, ES2015 구성 요소 제공 등 다양한 tool 제공

  ## 2-1. Node.js

  ## 2-2. NPM (Node Package Manage)

  - pakge-lock.json
    - node_modules 에 대한 패키지 정보들
    - `$ npm i`
  - package.json ([참고](https://velog.io/@skyepodium/package.json))([참고2](https://developer88.tistory.com/270))
    - 패키지를 설치하면 자동으로 추가

  # 3. Babel & Webpack

  ## Babel

  - JS compiler
  - ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구

  ## Webpack

  - "static module bundler"
  - 모듈 간의 의존성 문제를 해결하기 위한 도구
  - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

  ### **Stataic Module Bundler**

  - 모듈은 단지 파일 하나를 의미 (ex. 스크립트 하나 === 모듈 하나)

  > Module  의존성 문제

  - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워짐
  - 즉, Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

  ### Bundler

  - 모듈 의존성 문제를 해결해주는 작업을 Bundling이라 함

  > node_modules의 의존성 깊이

  - [출처](https://www.reddit.com/r/ProgrammerHumor/comments/6s0wov/heaviest_objects_in_the_universe/)

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68b31aa5-b1a4-4af7-952a-e00530f262ae/Untitled.png)

  > Webpack

  - https://webpack.js.org/

  ![1.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e71fe189-32f2-46f8-a1eb-b956b7813b00/1.png)

  ------

  # 4. Pass Props & Emit Events

  ## Props 이름 컨벤션

  - during declaration (선언 시)
    - camelCase
  - in template(HTML)
    - kebab-case
    - 카멜케이스를 지원하지 않음

  > **컴포넌트의 'data'는 반드시 function 이여야 함**

  - [DOC](https://kr.vuejs.org/v2/guide/components.html#data-는-반드시-함수여야합니다)
  - 일반적인 key: value 형태로 작성하면 에러 발생

  # 5. Router

  - 라우트(route)에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
  - SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

  > [참고] router

  - 위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치

  ## index.js

  - 라우트에 관련된 정보 및 설정이 작성 되는 곳
  - django의 url 느낌
