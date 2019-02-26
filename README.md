# boj_algorithm_python
PYTHON X ALGORITHM  
### 1. 자료형  
#### 1.1 딕셔너리
      1) 해시테이블 구조 key - value
      2) 선언은 간단 dic = {"a" : 1, "b" : 2} 이런 식으로 ..
      3) key 로 value 호출시 dic[key]
         * 근데 값 없으면 에러 뱉음에 주의
         * 값 있는지 판별해야 할 때는, key in dic 이런식으로 찾음
      4) 값 넣을때는 dic[key] = val 이런 식으로 꽂아넣음  

### 2. 모듈  
#### 2.1 collections
      1) Deque : 그냥 리스트 보다 훨씬 빠름 
         import collections
         queue = deque([])
         queue.append(sth)
         queue.popleft()
