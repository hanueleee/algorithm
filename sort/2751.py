import sys

N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(N)]

for i in sorted(array):
    print(i)

"""
파이썬의 다양한 입력함수
1. input()
2. sys.stdin.readline()
- readline()은 개행문자를 포함
- readline().rstrip() : 오른쪽 공백을 삭제
- readline().lstrip() : 왼쪽 공백을 삭제
- readline().strip() : 왼쪽, 오른쪽 공백을 삭제
참고 : https://yang-wistory1009.tistory.com/54
"""