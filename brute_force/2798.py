def pick(idx,r):
  if(r == 0):
    if (sum(picked)<=M):           
        ans.append(sum(picked))
    return
  
  for i in range(idx, N):
    picked.append(cards[i])                
    pick(i+1, r-1)         
    picked.pop()

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

picked = []
ans = []

pick(0, 3)
print(max(ans))

"""
옛날에 풀었던 코드
근데 시간복잡도가 위 코드의 2,3배 

from itertools import permutations
N, M = map(int, input().split())
CARD = list(map(int, input().split()))
MAX = 0
for x,y,z in permutations(CARD,3):
    tmp = x+y+z
    if MAX<tmp and tmp<=M:
        MAX = tmp
print(MAX)
"""