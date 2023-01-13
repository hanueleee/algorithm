K = int(input())
s = []

for _ in range(K):
    n = int(input())
    if (n!=0):
        s.append(n)
    else:
        s.pop()
        
print(sum(s))