from collections import deque

N = int(input())
b = list(map(int, input().split()))
balloon = deque((b[idx], idx+1) for idx in range(len(b)))

for _ in range(N):
    pick = balloon.popleft()
    print(pick[1], end=" ")

    if (pick[0]>0):
        balloon.rotate(1-pick[0])
    else:
        balloon.rotate(-pick[0])

"""
1번째 시도 : pop따로 하지 않고 해당 idx의 값을 'x'로 세팅 -> 실패 ..
2번째 시도 : 종이에 적혀있는 값만큼 popleft&append / pop&appendleft
3번째 시도 : 종이에 적혀있는 값만큼 rotate

자꾸 틀리길래 반례 찾다보니 ..
나는 딕셔너리를 이용해 {종이에 적혀있는 값 : 풍선의 위치} 저장해뒀는데
종이에 적혀있는 값이 중복될 경우 문제 발생 (딕셔너리는 키가 중복되는 것을 허용하지 않는다)
=> 중복된 위치 출력
"""