N = int(input())
array = list(set([input() for _ in range(N)]))

array.sort(key = lambda x: (len(x), x)) # 길이가 짧은 것부터, 사전 순으로

for word in array:
    print(word)