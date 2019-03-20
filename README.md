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
      
#### 1.2 리스트 
      1) 리스트 중복 제거시 
        list(set(arr)) 이런식으로 하면 중복 제거됨
      2) 리스트에 빈 문자열 지우기
        arr = [x for x in old_arr if x] 
        이렇게 하면 빈 문자열 조져줌
        
#### 1.3 집합 (set)
      1) 집합객체 생성 
        myset = set()
      2) 집합은 중복과 순서가 없음, 대신 검색이 좀 빠른듯
        2-1) 1.2 1)과 같이 리스트를 집합으로 변환 했다가 다시 리스트로 바꿔주면 중복이 제거됨

##### 유용한 집합 연산들
~~~python
# 집합 선언
set1 = set([1,2,3])
set2 = set([2,4,5,6])
set3 = set() # 공집합
 
# set1과 set2의 교집합
print(set1 & set2)
 
# set1과 set2의 합집합
print(set1 | set2)
 
# set1과 set2의 차집합
print(set1 - set2)

# set1과 set2의 합집합에서 교집합을 뺀 차집합
print(set1 ^ set2)
  
~~~

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
      
#### 2.2 itertools
      1) Combinations, Permutations
      import itertools 하고
      itertools.combinations(arr,3) 
      이런식으로 쓰면 조합 다 구해줌 개꿀