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
      * 5) key,val 둘이 iterate 하고 싶다면
      for key,val in Dic.items(): 
      이런식으로 고고
      

### 2. 모듈  
#### 2.1 collections
      1) Deque : 그냥 리스트 보다 훨씬 빠름 
         import collections
         queue = deque([])
         queue.append(sth)
         queue.popleft()
         
#### 2.1 copy
      1) Deepcopy
      리스트 그냥 복사했다가는 제대로 복사 안먹음 (조심)
      따라서 딥카피를 해야한다.
      리스트 딥카피는 아래와 같다.
      new_one = copy.deepcopy(old_one)
      
      그러나, deque는 그냥 
      new_one = collections.deque(list(old_one)) 
      하면 됨
