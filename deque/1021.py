from collections import deque

def move(q, tar):
    cnt = 0
    while(q[0] != tar):
        q.rotate(1)
        cnt+=1
    return cnt

N, M = map(int, input().split())
elements = list(map(int, input().split()))

q = deque([i+1 for i in range(N)])
ans = 0

for e in elements:
    tmp = move(q, e)
    ans += min(tmp, len(q)-tmp)
    q.popleft()

print(ans)