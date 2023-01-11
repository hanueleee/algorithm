import sys

N=int(input())
d = []

for _ in range (N):
    cmd = sys.stdin.readline().split()
    if (cmd[0]=="front"):
        print(-1 if not d else d[0])
    elif (cmd[0]=="back"):
        print(-1 if not d else d[-1])
    elif (cmd[0]=="size"):
        print(len(d))
    elif (cmd[0]=="empty"):
        print(1 if not d else 0)
    elif (cmd[0]=="pop_front"):
        print(-1 if not d else d.pop(0))
    elif (cmd[0]=="pop_back"):
        print(-1 if not d else d.pop(-1))
    elif (cmd[0]=="push_front"):
        d.insert(0, int(cmd[1]))
    else:
        d.append(int(cmd[1]))