from collections import Counter
import sys

def get_mode(num):
    if(len(num)==1):
        return num[0]
    cnt = Counter(num).most_common()
    if cnt[0][1] != cnt[1][1]:
        return cnt[0][0]
    else:
        array = []
        for t in cnt:
            if t[1] == cnt[0][1]:
                array.append(t[0])
        return sorted(array)[1]
    
N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()

avg = round(sum(num)/N)
mid = num[N//2]
mode = get_mode(num)
diff = num[-1]-num[0]

print(avg)
print(mid)
print(mode)
print(diff)

"""
시간초과
-> 입력 많을 때 무조건 sys.stdin.readline() 쓰기 !!!
"""