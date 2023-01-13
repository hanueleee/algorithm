def f(N):
    s = []
    ans = ""

    cnt = 1
    for _ in range(N):
        x = int(input())
        while (cnt <= x):
            s.append(cnt)
            cnt+=1
            ans+='+'
        if (x == s[-1]):
            s.pop()
            ans+='-'
        else:
            print("NO")
            return
    while(s):
        s.pop()
        ans+='-'
    for c in ans:
        print(c)

N = int(input())
f(N)
