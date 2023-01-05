N = int(input())
array = [tuple(input().split()) for _ in range(N)]

array.sort(key = lambda x: (int(x[1]), int(x[0])))

for p in array:
    print(" ".join(p))