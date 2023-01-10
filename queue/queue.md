## 큐
- 가장 먼저 들어온 데이터부터 추출하는 자료구조
- 선입선출 또는 FIFO(First In First Out) 방식
- 예시 : 프린터의 인쇄 대기열 / 은행의 번호표 등 일상 속에서 우리가 대기하는 모든 상황

<br>
<img width="600" alt="image" src="https://user-images.githubusercontent.com/91522259/211523527-5fc7561c-2da4-4a24-a478-7063f1040574.png">



스택에서는 top이라는 인덱스만 알고 있으면 top에서 자료를 넣고 빼는 모든 작업을 할 수 있었지만  
큐에서는 **front와 rear**(또는 back)이라는 두개의 인덱스를 활용해 자료구조의 시작과 끝을 모두 지켜보고 있어야한다.

> enqueue(data) : 큐 맨 뒤(rear)에 데이터 삽입  
> dequeue() : 큐 맨 처음(front) 데이터 삭제하면서 해당 데이터 반환
<br>

## python에서의 구현
### 1) list 사용
```
queue = []            
queue.append("a") // enqueue 
queue.pop(0) // dequeue
```
- 스택과 마찬가지로 list로 구현할 수 있으나 성능적으로 좋지 않다.
- append(data)의 시간복잡도 : O(1)
- pop(0)의 시간복잡도 : O(N)

### 2) deque 사용
```
from collections import deqeue
dq = deque()
dq.append("a") // enqueue
dq.popleft() // dequeue
```
- 보통 deque를 사용해 구현한다.
- append(data)의 시간복잡도 : O(1)
- popleft()의 시간복잡도 : O(1)
