# 1. Git

> 분산 버전 관리 시스템( DVCS, Distributed Version Control System)

윈도우 환경에서는 git 설치 및 실행을 위해 git bash를 다운로드 받아야 한다.

# 2. Git 기본 명령어

### 저장소(repository 생성)

```bash
$ git init
```

- ```
  .git
  ```

   폴더가 숨김 폴더로 생성되고, git bash에서는 

  ```
  (master)
  ```

   라고 표기 됨

  - 저장소 생성시 상위 폴더에 

    ```
    .git
    ```

     저장소가 있지 않은지 확인해야함

    - 예) 바탕화면에 실수로 `git init` 해서 `.git` 이 있는 경우

### 기본 버전 관리 흐름

- git은 저장소 내에 모든 파일의 변경사항을 추적함

- 작업을 완료하고 

  ```
  add
  ```

   → 

  ```
  commit
  ```

   을 통해 버전을 기록할 수 있음

  - `working directory` 에서 `add` 명령어를 통해 `staging area` 상태`(staged)` 로
  - `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 버전 기록

### `add`

```bash
$ git add a.txt # 특정 파일
$ git add test/ # 특정 폴더
$ git add .     # 현재 디렉토리 (하위 디렉토리 포함)
```

### `commit`

> `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 버전 기록

```bash
$ git commit -m '커밋 메시지'
[master b4dba1d] test
 1 file changed, 1 deletion(-)
 delete mode 100644 a.txt
```

- 커밋 메시지는 현재 버전에 대해 알 수 있도록 작성
- 지금까지 커밋을 확인하기 위해서는 `git log` 명령어 사용

## 상태 확인

### `status`

> working directory 와 staging area의 상태를 확인할 수 있다.

특정 파일이 변경되었는지 (추가/수정/삭제), `staged` 상태인지

```bash
$ git status
```

### `log`

> 커밋 로그를 확인

```bash
$ git log
$ git log --oneline # 한줄로 간략히 표기
$ git log -2 # 최근 n개의 로그만 확인
$ git log --oneline -2 #한줄로 최근 n개만 
```

# 3. 연습	 



1. 바탕화면에 first 파일 만들기

2. 우클릭 → git bash here 클릭

3. ```
   $ git init
   ```

    → git 실행, git 로컬 저장소 설정

   1. 각 폴더 별 프로젝트 관리할 때 실행
   2. 바탕화면에서 실행하면 모든 버전들이 관리됨(비추) → .git 파일 제거 하면 해결

4. `$touch a.txt`  a.txt파일 만들기

5. `$ git add a.txt` → git에 `a.txt`을 추가하겠다.

6. `$ git commit -m 'a.txt 추 가 '`

- `$git config —global -l`  → 누군지 확인가능
- `$git config —global user.email ' 이메일'`
- `$git config —global user.email ' Your Name'`
- 하고 `$ git commit -m 'a.txt 추 가 '`  다시 실행

### 문서 수정

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32ee90c1-58fe-4426-9d21-2c67693f737b/__2021-07-15_110959.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32ee90c1-58fe-4426-9d21-2c67693f737b/__2021-07-15_110959.png)

- `$ git status` 사용
- `$ git add a.txt`  커밋할 목록에 추가
- `$ git status`  다시 쳐서 변경 확인
- `$ git commit -m 'A 수 정 '`   버전 저장
- `$ git log` 지금까지 commit한 버전들 확인

### 문서 삭제 후

- `$ git status`  확인

# 4. 실습

------

- 바탕화면에 TIL 폴더 만들기
- TIL 폴더를 Git 저장소로 만들기

```bash
$ git init
```

- [README.md](http://readme.md) 파일을 만드시고, 버전 기록 하기

```bash
$ touch README.md
```

------

- (선택1) 다하신분들은, 마크다운 / git정리 파일을 추가하고 버전 기록
- (선택2) 파이썬 어제 내용 마크다운으로 정리해보고 버전 기록
- 다하면, `git log --oneline` 의 결과를 채팅창에 올리기