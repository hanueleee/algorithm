from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])

while (len(cards)>1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

"""
기존코드
while (len(cards)>1):
    cards.pop(0)
    cards.append(cards.pop(0))
=> 시간초과
"""

"""
list 시간복잡도
- append() : O(1)
- pop() : O(1)
- pop(idx) : O(n)
- insert(idx, data) : O(n)

deque 시간복잡도
- appendleft(data) : O(1)
- append(data) : O(1)
- popleft() : O(1)
- pop() : O(1)
- remove(data) : O(n)
"""