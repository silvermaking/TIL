# 알고리즘1. 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
  - step1. 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)
  - step2. 후위 표기법의 수식을 스택을 이용하여 계산

### Step1. 중위 표기법에서 후위 표기법으로의 변환 알고리즘

1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4. 토큰이 `)` 이면 스택 top에 `(`이 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력 `(` 을 만나면 pop만 하고 출력하지 않음
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽은 것이 있다면 1부터 다시 반복
6. 스택에 남아 있는 연산자를 모두 pop하여 출력
   - 스택 밖의 `(`는 우선 순위가 가장 높으며, 스택 안의 `(` 우선 순위가 가장 낮다.

### step2. 후위 표기법의 수식을 스택을 이용하여 계산

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를  다시 스택에 push
3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

# 알고리즘2. 백트래킹

- 백트래킹 기법은 해를 찾는 도중에 '막히면' 되돌아가서 다시 해를 찾아 가는 기법
- 최적화, 결정 문제 해결
  - 결정문제: 문제의 조건을 만족하는 해가 존재하는지의 여부 판단하는 문제
  - 미로찾기, n-Queen, Map coloring, 부분 집합의 합 등

### 백트래킹 vs DFS

- prunning 가지치기를 통해 해결책으로 이어지지 않는 경로는 더 이상 고려하지 않는다.
- DFS하기에 경우의 수가 너무 많은 경우⇒ 백트래킹 사용
- 최악의 경우는 여전히 지수함수 시간이다.

## 순열

```python
def per(k):
    if k == 3:
        print(t)
        for i in range(3):
            pos = t[i]
            print(a[pos], end=' ')
        print()
    else:
        for i in range(3):
            if not visited[i]: #사용 안한 경우에
                t[k] = i
                visited[i] = True
                per(k+1)    
                visited[i] = False  # per(k)는 방문안한 순열형태로 남겨놓기 위해

visited = [False] * 3
a = [28, 31, 78]
t = [-1] * 3
per(0)
```