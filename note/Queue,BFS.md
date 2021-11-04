# 큐(Queue)의 특성

- 스택처럼 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만, 큐의 앞에서는 삭제만
- 선입선출구조(FIFO : First in First Out)
- 삽입 : `enQueue(item)`  , 삭제 : `deQueue()`
- `createQueue()` : 공백상태의 큐 생성
- `isEmpty()` `isFull()` : 큐가 공백, 포화인지 확인하는 연산
- `Qpeek()` : 큐의 앞쪽에서 원소를 삭제 없이 반환\

# 큐의 구현

- python과 달리 다른언어는 배열의 사이즈가 동적으로 조절x
  - 선형큐, 원형큐 ( python은 `.append()` 로 늘릴 수가 있다)
  - → 연결큐가 나옴

## 1. 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫 번째 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front = rear
  - 포화 상태 : rear = n-1
- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front와 rear를 -1로 초기화

## 2. 원형큐

- 초기 공백 상태 : front = rear = 0
- Index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야함
  - 이를 위해 나머지 연산자 `mod`를 사용함
- front 변수 : 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위취 및 삭제 위치

|        | 삽입 위치                    | 삭제 위치                 |
| ------ | ---------------------------- | ------------------------- |
| 선형큐 | rear = rear +1               | front = front + 1         |
| 원형큐 | rear = (rear + 1) mod n (%n) | front = (front + 1) mod n |




## 3. 연결 큐의 구조

주소관리에 좋음 (linked list)

### 단순 연결 리스트(Linked List)를 이용한 큐

- 큐의 원소 : 단순 연결 리스트의 노드
- 큐의 원소 순서 : 노드의 연결 순서, 링크로 연결되어 있음
- front : 첫 번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크

### 상태 표현

- 초기 상태 : front = rear = null
- 공백 상태 : front = rear = null

[A, 0x1008] : 데이터 , 공간주소(다음데이터)

### 연산 과정

1. `createLinkedQueue()`
2. 원소 A삽입 : `enQueue(A)`

[A(0x1000), NULL]

1. 원소 B 삽입

[A(0x1000), 0x1008] [B(0x1008), NULL]

## 4. 우선순위 큐(Priority Queue)

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO순서가 아니라 우선순위가 높은 순서대로 먼저 나감
- ex) 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 테스크 스케줄링

## 5. 큐의 활용 : 버퍼(Buffer)

### 버퍼

- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버버링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.

### 버퍼의 자료 구조

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다.

### 6. 연습문제 : 마이쮸

```python
''' 마이쮸 나눠주기 시뮬레이션
		1번이 한개의 마이쮸를 받는다
		1번이 다시 줄을 선다
----------------------
	  2번이 줄을 선다
		1번이 두개의 마이쮸를 받는다
	  1번이 다시 줄을 선다
-----------------------
		3번이 들어와 줄을 선다
		2번이 한개의 마이쮸를 받는다
		2번이 다시 줄을 선다
-----------------------
		4번이 들어와 줄을 선다
	  1번이 세개의 마이쮸를받는다
		1번이 다시줄을 선다
-----------------------
		5번이 줄을 선다
		3번이 한개의 마이쮸를 받는다'''
N = 20  #마이쮸 갯수
persons = 1
Queue = []
cnt = 0
while True:
    Queue.append((persons, 1))
    a, jelly = Queue.pop(0)
    cnt += jelly
    if cnt >= N:
        print(a)
        break
    Queue.append((a,jelly+1))
    persons += 1
```

------

# BFS(Breadth First Search)

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함
- 경로 중에 짧은 경로를 찾을 떄는 BFS가 효율적이다.

## 2가지 방법

### 1. 인접리스트

- O(인접정점의수)

```python
lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
#1
G = [[] for _ in range(8)]

def bfs_G(v):
    q = []
    visited = [False] * 8
    q.append(v)     #첫번째 것 무조건 큐에 넣기
    visited[v] = True
    while q:
        v = q.pop(0)    #큐에서 정보 추출
        print(v)#v에 대해 처리(출력)
        for w in G[v]:#v와 인접한 w 중에 대해 안한 것들
            if not visited[w]:
                q.append(w) # 큐에 넣는다.
                visited[w] = True

for i in range(0, 16, 2):
    v1 = lst[i]
    v2 = lst[i+1]
    #1 방향이 없으므로 양방향으로 넣어주기
    G[v1].append(v2)
    G[v2].append(v1)

bfs_G(1)
```

### 2. 인접행렬

- O(|V|)
- 하나의 간선 유무를 확인할 때 좋음

```python
lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
#2
adj = [[0] *8 for _ in range(8)]

def bfs_adj(v):
    q = []
    visited = [False] * 8
    q.append(v)     #첫번째 것 무조건 큐에 넣기
    visited[v] = True
    while q:
        v = q.pop(0)    #큐에서 정보 추출
        print(v)#v에 대해 처리(출력)
        for w in range(len(adj[v])):#v와 인접한 w 중에 대해 안한 것들
            if adj[v][w] == 1 and not visited[w]:
                q.append(w) # 큐에 넣는다.
                visited[w] = True

for i in range(0, 16, 2):
    v1 = lst[i]
    v2 = lst[i+1]
#2
    adj[v1][v2] = 1
    adj[v2][v1] = 1

bfs_adj(1)
```