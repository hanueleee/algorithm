## 스택

- 가장 최근에 저장된 데이터가 가장 먼저 추출되는 방식의 자료구조
- 후입선출 또는 LIFO(Last In First Out) 방식
- 예시 : 인터넷 브라우저의 뒤로가기 / 재귀함수 호출 / Ctrl+Z (실행 취소)
 
<img width="500" alt="image" src="https://user-images.githubusercontent.com/91522259/211515269-d1c03d1a-cc79-4cd3-b8b2-cf3a324198b4.png">

스택은 배열로 구현할 수 있다.  
배열의 한쪽 끝에서만 자료를 넣고 뺄 수 있으며 이 지점을 **top**이라고 부른다.  
top에 자료를 push하고, top에서 자료를 pop한다.  


> push(data) : 값을 스택 맨 위에 삽입  
> pop() : 스택 맨 위에 있는 값 삭제 후 해당 값 반환  
> top : 스택 맨 위에 있는 데이터를 반환    
<br>

## python에서의 구현
- 파이썬에는 스택을 별도로 구현한 모듈이 없다.
- list 자료형에 이미 append, pop 함수 존재 => list를 스택처럼 사용 가능
```
stack = []            
stack.append("a") // push  
stack.pop() // pop
stack[-1] // top
```
