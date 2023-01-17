import sys
import heapq

N = int(input())
arr = []

for _ in range(N):
    line = map(int, sys.stdin.readline().split())
    for x in line:
        heapq.heappush(arr, x)
        if (len(arr)>N):
            heapq.heappop(arr)

print(heapq.heappop(arr))

"""
기존코드
import sys
import heapq

N = int(input())
arr = []

for _ in range(N):
    line = map(int, sys.stdin.readline().split())
    for x in line:
        heapq.heappush(arr, -x)

for _ in range(N-1):
    heapq.heappop(arr)
print(-heapq.heappop(arr))

--------------

메모리 초과
원인 : list의 메모리가 커져서 메모리 초과 발생
해결 : heap의 길이가 n보다 크면 heappop(가장 작은 원소를 pop)해줘서 heap길이 조절
(문제에서 n번째 큰 수를 원하기 때문에 n밖의 숫자들 버려도 된다)
"""