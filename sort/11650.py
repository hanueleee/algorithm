N = int(input())
array = [tuple(input().split()) for _ in range(N)]

array.sort(key = lambda x: (int(x[0]), int(x[1])))

for p in array:
    print(" ".join(p))

"""
lambda
- lambda는 함수를 간단하게 사용하게 해준다 (익명함수)
- lambda 매개변수: 표현식

ex1) 
def hap(x,y):
    return x+y
hap(10,20) // 30 

(lambda x,y: x+y)(10,20) // 30

ex2)
(lambda x: x+1)(3) // 4

ex3)
list(map(lambda x: x**2, range(5))) // [0,1,4,9,16]

** sort의 key로 lambda 사용하기 (lambda의 반환값을 비교하여 순서대로 정렬)
array.sort(key=lambda x:len(x)) // 길이 기준 정렬
array.sort(key=lambda x:x[0]) // 아이템의 첫번째 인자 기준 오름차순 정렬
array.sort(key=lambda x:x[1]) // 아이템의 두번째 인자 기준 오름차순 정렬
array.sort(key=lambda x:(x[0],-x[1])) // 먼저 아이템의 첫번째 인자 기준으로 오름차순 정렬, 그 안에서 두번째 인자 기준으로 내림차순 정렬
"""

"""
join 함수 : 매개변수로 들어온 리스트 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환
ex1) "".join(['a','b','c']) // "abc"
ex2) "_".join(['a','b','c']) // "a_b_c"
"""