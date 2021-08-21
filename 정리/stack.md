# 1. 스택

## 스택(Stack) 의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조: 자료 간의 관계가 1 대 1
  - 비선형구조 : 자료 간의 관계가 1대 N (예: 트리)
- 마지막에 삽입한 자료를 가장 먼저 꺼냄. 후입선출(LIFO, Last-in-First-out)

---

## 스택 구현을 위한 자료구조와 연산

- 자료구조 : 자료를 선형으로 저장할 저장소
  - 저장소 자체를 스택이라 부르기도 한다.
  - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.

- 연산
  - 삽입 : 저장소에 자료 저장(push)
  - 삭제 : 저장소에서 자료를 꺼냄(pop)
  - `isEmpty` : 스택이 공백인지 아닌지
  - `peek` : 스택의 top에 있는 item 반환

---

## 스택 구현

### push 알고리즘

`append()` method로 리스트의 마지막에 데이터 삽입

```python
def push(item):
	s.append(item) 
```

### pop 알고리즘

```python
def pop():
	if len(s) == 0:
		# underflow
		return
	else:
		return s.pop(-1):
```

---

## 스택 구형 고려 사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하지만 스택의 크기를 변경하기 어렵다.
  - **Python은 해당 x**
- 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다.
  - 동적 연결리스트를 이용하여 구현하는 방법
  - 구현이 복잡하지만 메모리를 효율적으로 사용
  - 알고리즘에서는 사용에서는 첫 번째 방법이 효율적

---

# 2. 재귀호출

- 자기 자신을 호출하여 순환 수행

- ex) 피보나치 수

  ```python
  def fibo(n):
  	if n < 2:  #breakpoint
  		return n
  	else:
  		return fibo(n-1) + fibo(n-2)
  ```

---

# 3. Memoization

- **Memoization**은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법의 핵심이 되는 기술

- 앞의 예에서 `fibo(n)`을 계산하자마자 저장하면, 실행시간을 O(n)으로 줄일 수 있다.

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화
def fibo1(n):
	global memo
	if n < 2 and len(memo) <= n:  
		memo.append(fibo1(n-1) + fibo1(n-2))
	return memo[n]

memo = [0, 1]
```

# 4. DP

# 5. DFS

## 인접표현방식

1.  1차원 list

```python
#1  비효율적
lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 방법1
def findW(v):
    for i in range(0, len(lst), 2):
        if v == lst[i] and visited[lst[i+1]]==False:
            return lst[i+1]
        if v == lst[i+1] and visited[lst[i]]==False:
            return lst[i]

    return -1
```

2. dictionary

```python
#2  파이썬에 유리, 직관적
G = {0: [], 1:[2, 3],2:[1,4,5], 3:[1,7],4:[2,6],5:[2,6],6:[4,5,7],7:[3,6]}
#방법2
def findG(v):
    for w in G[v]:
        if visited[w]==False:
            return w
    return -1
```

3. 2차원 list

```python
#3 일반적인 알고리즘은 이방식을 많이 씀씀
dj = [[0,0,0,0,0,0,0,0],
       [0,0,1,1,0,0,0,0],  #1
       [0,1,0,0,1,1,0,0],  #2
       [0,1,0,0,0,0,0,1],  #3
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]
#방법3
def findADG(v):
    for i in range(len(adj[v])):
        if adj[v][i] == 1 and visited[i]==False:
            return i
    return -1
```



## DFS 구현

```python
n = 7
visited = [False] * (n + 1)  # 0번 비워놓기
ST = []   #스택
def dfs(v):
    visited[v] = True
    print(v)
    ST.append(v)
    while len(ST) > 0:
        # w = findW(v)
        w = findG(v)
        if w != -1:
            ST.append(v)
            visited[w] = True
            print(w)
            v = w
        else:
            v = ST.pop(-1)
```