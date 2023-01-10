import sys

N=int(input())
s = []

for _ in range (N):
    cmd = sys.stdin.readline().split()
    if (cmd[0]=="top"):
        print(-1 if not s else s[-1])
    elif (cmd[0]=="size"):
        print(len(s))
    elif (cmd[0]=="empty"):
        print(1 if not s else 0)
    elif (cmd[0]=="pop"):
        print(-1 if not s else s.pop())
    else:
        s.append(int(cmd[1]))