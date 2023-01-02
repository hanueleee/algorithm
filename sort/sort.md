# 정렬 (Sorting)

- 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
- 데이터를 정렬하면 이진 탐색이 가능해짐 (정렬은 이진탐색의 전처리과정)  
  
# 1. 선택 정렬 (Selection Sort)

- 선택 정렬 : 가장 작은 것을 선택해서 앞으로 보낸다
- 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료됨

1️⃣ 현재 정렬되지 않은 가장 맨 앞의 인덱스를 선택한다

2️⃣ 현재 인덱스의 다음 인덱스부터 끝까지 가장 작은 값을 찾으면 현재 인덱스의 값과 바꿔준다

3️⃣ 다음 인덱스에서 위 과정을 반복한다

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i   # 가장 작은 원소의 인덱스
	for j in range(i+1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i] # swap
```

- 시간복잡도 : O(N^2)
- N + (N-1) + (N-2) + … + 2 ⇒ N \* (N+1) / 2 ⇒ (N^2 + N) / 2 ⇒ O(N^2)
- 반복문이 얼마나 중첩되었는지를 기준으로 간단히 시간 복잡도 판단 가능
  → 여기서는 2중 반복문이니까 O(N^2)

# 2. 삽입 정렬 (Insertion Sort)

- 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입한다
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
- 특히 ‘데이터가 거의 정렬 되어 있을 때' 매우 효율적

1️⃣ 두 번째 원소부터 시작

2️⃣ 그 앞의 원소들과 비교하여 삽입할 위치를 지정

3️⃣ 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입하여 정렬

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
			array[j], array[j-1] = array[j-1], array[j]
		else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
			break
```

- 시간복잡도 : O(N^2)
- 반복문 2번 중첩
- 삽입정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작 → 최선의 경우 O(N)
  ⇒ 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 삽입 정렬을 이용해라  

# 3. 퀵 정렬 (Quick Sort)

- 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다
- pivot을 기준으로 pivot보다 작은 요소들은 모두 pivot의 왼쪽으로 옮기고 pivot보다 큰 요소들은 모두 pivot의 오른쪽으로 옮긴다
- 분할정복 알고리즘

1️⃣ 분할

피벗(교환하기 위한 기준) 설정 → 왼쪽에서부터 피벗보다 큰 데이터 찾고, 오른쪽에서부터 피벗보다 작은 데이터 찾기 → 큰 데이터와 작은 데이터의 위치를 서로 교환 → … → 두 값이 엇갈린 경우 작은 데이터와 피벗의 위치를 서로 변경

2️⃣ 왼쪽 리스트 똑같은 방식으로 정렬

3️⃣ 오른쪽 리스트 똑같은 방식으로 정렬

⇒ 재귀 (종료 조건 : 현재 리스트의 데이터 개수가 1인 경우)

- 퀵 정렬 소스코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start # 피벗은 첫번째 원소
	left = start + 1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1
		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right >= start and array[right] >= array[pivot]:
			right -= 1
		if left > right : # 엇갈렸다면 작은 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
			array[left], array[right] = array[right], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

- 파이썬의 장점을 살린 퀵 정렬 소스코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	# 리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array

	pivot = array[0] # 피벗은 첫 번째 원소
	tail = array[1:] # 피벗을 제외한 리스트

	left_side = [x for x in tail if x<= pivot] # 분할된 왼쪽 부분
	right_side = [x for x in tatil if x>= pibot] # 분할된 오른쪽 부분

	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
	return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
```

- 시간 복잡도 : O(NlogN)
- 데이터 개수가 많을수록 퀵 정렬은 선택 정렬, 삽입 정렬에 비해 압도적으로 빠르다
- 하지만 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작. O(N^2) ↔ 삽입정렬은 이 경우에 빠름

# 4. 계수 정렬 (Count Sort)

- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
- 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능
- 모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언해야 한다
- 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다

1️⃣ 처음에는 리스트의 모든 데이터가 0이 되도록 초기화

2️⃣ 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가 -> 반복

3️⃣ 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 인덱스 출력

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
	count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
	for j in range(count[i]):
		print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

- 시간 복잡도 : O(N+K) // N : 데이터의 개수, K : 데이터 중 최대값의 크기
  ⇒ 데이터의 범위만 한정되어 있으면 효과적으로 사용할 수 있으며 항상 빠르게 동작
- 공간 복잡도 : O(N+K)
  ⇒ 때에 따라서 심각한 비효율성을 초래할 수 있다 (ex. 데이터가 0과 999999 단 2개만 존재할때)
  ⇒ 항상 사용할 수 있는 알고리즘x. 동일한 값을 가지는 데이터가 여러개 등장할 때 적합.
  (↔ 퀵정렬 : 일반적인 경우에서 평균적으로 빠르게 동작하므로 데이터의 특성을 파악하기 어렵다면
  퀵 정렬 사용하는것이 유리)
- 데이터의 크기가 한정되어 있고 데이터의 크기가 많이 중복되어 있을수록 유리. 항상 사용할 수는 x

# 그 외

### 1) 버블 정렬 (Bubble Sort)

- 현재 원소와 다음 원소를 비교하여 조건에 맞으면 교환하는 식의 정렬

```python
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]: # 인접한 두 원소 비교
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

### 2) 병합 정렬 (Merge Sort)

- 분할정복의 대표적인 예
  Divide(분할) : n개의 원소를 갖는 배열을 n/2개의 원소를 갖는 작은배열 2개로 나눈다
  Conquer(정복) : 각각의 작은 배열들을 정렬한다
  Combine(병합) : 정렬된 작은 배열들을 병합한다

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

```python
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
```

# 파이썬의 정렬 라이브러리

- 우리가 알고리즘 문제를 풀 때는 앞서 다루었던 예제처럼 정렬 알고리즘을 직접 작성하게 되는 경우도 있지만,
  미리 만들어진 라이브러리를 이용하는 것이 효과적인 경우가 더 많다
- 시간복잡도 : O(NlogN)

```python
# sorted() : 리스트, 딕셔너리, 집합 등을 입력받아 정렬 .. 반환되는 결과는 리스트
array = [7, 5, 9, 3, 1]
result = sorted(array)
print(result) // [1, 3, 5, 7, 9]

# list의 sort()
array = [7, 5, 9, 3, 1]
array.sort()
print(array)

# sorted()나 sort()는 key 매개변수를 입력으로 받을 수 있다
# key값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다
array = [('바나나',2), ('사과',5), ('당근',3)]

def setting(data):
	return data[1]

result = sorted(array, key=setting)

print(result) // [('바나나',2), ('당근',3), ('사과',5)]
```

- 단순히 정렬해야 하는 상황 → 기본 정렬 라이브러리 사용
- 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때 → 계수 정렬 사용

💡 코딩 테스트에서 정렬 알고리즘이 사용되는 경우

1. 정렬 라이브러리로 풀 수 있는 문제
   단순히 정렬 기법을 알고 있는지 물어보는 문제로, 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
   선택정렬, 삽입정렬, 퀵정렬 등의 원리를 알고 있어야 문제를 풀 수 있다
3. 더 빠른 정렬이 필요한 문제
   퀵정렬 기반의 정렬 기법으로는 풀 수 없으며 계수정렬 등의 다른 정렬 알고리즘을 이용하거나
   문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다

📑 참고

이것이 취업을 위한 코딩 테스트다 with 파이썬

https://code-lab1.tistory.com/24
