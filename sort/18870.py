import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
sorted_array = sorted(set(array))

dic = {}
for i in range (len(sorted_array)):
    dic[sorted_array[i]] = i

for x in array:
    print(dic[x], end=" ")

"""
시간초과
1. input관련 -> sys.stdin.readline() 사용
2. .index()연산은 O(N)의 시간복잡도 -> for문 돌리면 O(N^2) 시간복잡도
3. dictionary 사용
"""