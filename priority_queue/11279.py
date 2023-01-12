import sys
import heapq

N = int(input())
arr = []

for _ in range(N):
    x = int(sys.stdin.readline().split()[0])
    if (x==0):
        print(0 if not arr else -heapq.heappop(arr))
    else:
        heapq.heappush(arr, -x)

"""
<최대 힙 만들기>
파이썬의 heapq 모듈은 최소 힙으로 구현되어 있기 때문에 최대 힙 구현을 위해서는 트릭이 필요
y=-x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다.
"""

""" 초반코드
힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.

for _ in range(N):
    x = int(sys.stdin.readline().split()[0])
    if (x==0):
        print(0 if not arr else heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (-x,x))
"""