import sys

N = int(sys.stdin.readline())
count = [0] * 10001 # 모든 범위를 담을 수 있는 크기의 리스트 선언

for i in range(N):
    x = int(sys.stdin.readline()) # 빠른 입출력
    count[x] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)

"""
*** https://www.acmicpc.net/board/view/26132 FAQ 참고

1. 메모리 초과
문제의 메모리 제한은 겨우 8MB
-> 아무리 작은 자료형으로 저장해도, 모든 입력(최대 10,000,000개)을 배열에 저장하면 메모리 초과
-> 입력을 저장하지 않고 풀어야 한다

힌트 : 입력되는 정수의 범위가 제한되어 있다 (10,000보다 작거나 같은 지연수) => 계수 정렬 사용 가능

2. 시간초과
느린 입출력
-> 데이터의 개수가 많을 때는 sys.stdin.readline()를 사용
"""