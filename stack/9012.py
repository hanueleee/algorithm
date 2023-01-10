def check(s):
    cnt = 0 #스택의 크기
    for i in range(len(s)):
        if (s[i]=='('): # 여는 괄호
            cnt += 1
        else: # 닫는 괄호
            cnt -= 1
        if (cnt < 0): # 여 없는데 닫 한경우 (여 부족)
            return "NO"
    if (cnt==0): # 스택 비어있다 = 잘 끝남
        return "YES"
    else: # 스택 비어있지 않다 = 닫 부족
        return "NO"

N = int(input())
for _ in range(N):
    s = input()
    print(check(s))