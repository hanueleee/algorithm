import sys

N=int(input())
q = []

for _ in range (N):
    cmd = sys.stdin.readline().split()
    if (cmd[0]=="front"):
        print(-1 if not q else q[0])
    elif (cmd[0]=="back"):
        print(-1 if not q else q[-1])
    elif (cmd[0]=="size"):
        print(len(q))
    elif (cmd[0]=="empty"):
        print(1 if not q else 0)
    elif (cmd[0]=="pop"):
        print(-1 if not q else q.pop(0))
    else:
        q.append(int(cmd[1]))