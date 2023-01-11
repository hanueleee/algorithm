from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])
ans = [0]*1001

cnt = 1
while (len(cards)):
    for k in range(cnt):
        first = cards.popleft()
        cards.append(first)
    ans[cards.popleft()] = cnt
    cnt+=1

for a in ans:
    if (a!=0):
        print(a, end=" ")