import sys

N = int(input())
n_cards = set(map(int, sys.stdin.readline().split()))

M = int(input())
m_cards = list(map(int, sys.stdin.readline().split()))

for x in m_cards:
    if x in n_cards:
        print(1, end=" ")
    else:
        print(0, end=" ")

"""기존코드
import sys

N = int(input())
n_cards = list(map(int, sys.stdin.readline().split()))

M = int(input())
m_cards = list(map(int, sys.stdin.readline().split()))

for x in m_cards:
    if x in n_cards:
        print(1, end=" ")
    else:
        print(0, end=" ")

** in을 사용할 때
list는 O(N)의 시간복잡도
set은 O(1)의 시간복잡도
=> set을 사용하는게 좋다
"""