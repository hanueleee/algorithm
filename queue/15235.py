import sys

def finish(pizza_map):
    for x in pizza_map:
        if (x[0]!=0):
            return False
    return True

def print_ans(pizza_map):
    for x in pizza_map:
        print(x[1], end=" ")
        
N = int(input())
pizza = list(map(int, sys.stdin.readline().split()))
pizza_map = [ [p, 0] for p in pizza]

cnt = 0
while (True):
    for x in pizza_map:
        if (x[0]==0):
            continue
        if (x[0]>0):
            x[0] -= 1
            cnt += 1
            if (x[0]==0):
                x[1] = cnt
    if (finish(pizza_map)):
        break
print_ans(pizza_map)