N = int(input())
array = [tuple(input().split()) for _ in range(N)]

array.sort(key=lambda x: int(x[0])) # 나이순 (또다른 기준 안 넣으면 인덱스 순으로 정렬됨)

for t in array:
    print(' '.join(t))