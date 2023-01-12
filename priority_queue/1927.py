import sys
import heapq

N = int(input())
arr = []

for _ in range(N):
    x = int(sys.stdin.readline().split()[0])
    if (x==0):
        print(0 if not arr else heapq.heappop(arr))
    else:
        heapq.heappush(arr, x)

"""
파이썬의 heapq 모듈 : heapq (priority queue) 알고리즘 자공
- 모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리 구조
- 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2)보다 작거나 같은 최소 힙의 형태로 정렬

- heapq.heappush(h, item) : item을 h에 추가
- heapq.heappop(h) : h에서 가장 작은 원소를 pop하고 반환 (비어 있는 경우 indexError)
- heapq.heapify(x) : 리스트 x를 즉시 heap으로 변환 <- 시간복잡도 O(N)
"""