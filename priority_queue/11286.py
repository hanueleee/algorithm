import sys
import heapq

N = int(sys.stdin.readline().split()[0])
arr=[]

for _ in range(N):
    x = int(sys.stdin.readline().split()[0])
    if (x==0):
        if (len(arr)==0):
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(x),x))

"""
시간초과 떠서 input을 sys.stdin.readline().split()[0]로 바꿨더니 통과
sys.stdin.readline()은 기본으로 써야하나보다
"""