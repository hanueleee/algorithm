N,K = map(int, input().split())
num = list(map(int, input().split()))

print(sorted(num)[-K])