from collections import deque

N, k = map(int, input().split())
arr = deque([x+1 for x in range(N)])
ans = []

for _ in range(N):
    arr.rotate(-k+1)
    ans.append(arr.popleft())

for i in range(N):
    if (N==1):
        print("<"+str(ans[i])+">")
        break
    if (i==0):
        print("<"+str(ans[i]), end=", ")
    elif (i==N-1):
        print(ans[i], end=">")
    else:
        print(ans[i], end=", ")