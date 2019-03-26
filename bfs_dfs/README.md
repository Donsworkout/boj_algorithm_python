## BFS / DFS
### BFS
- BFS는 층을 기반으로 센다 (거리)
- 따라서 최소 거리 찾기가 쉬움
- Queue를 사용한다.
- Python은 collections 의 Deque 를 사용해야 시간에러 안남
- 층을 셀때는 층마다 대기중인 queue의 length 를 세어주고 거기에 count 를 넣는다. (어차피 queue에 pop 할만큼만 pop 하기 때문!

##### 예제 코드
~~~python 
def BFS():
    while queue:
        # 지금 큐에 들어가 있는 놈들 넓이대로 검사할꺼
        len_q = len(queue)
        for _ in range(len_q):
            # 왼쪽부터 터트린다 (큐 구조니깐 당연히 FIFO)
            cur = queue.popleft()
            # 터트릴때 조건에 맞으면 종료 (오버헤드 제거)
            if cur == target:
                print(cur)
                return
            for elem in child[cur]
                if elem not in visited:
                    # 자격 요건이 되고 (가지치기) 방문하지 않았다면
                    # 큐에 넣고 방문처리 해줌
                    queue.append(elem)
                    visited.append(elem)
        # 레벨 업 (깊이 추가)
        cnt += 1 
~~~

### DFS
- 통상적으로 자료구조 STACK 을 쓰기보다는 재귀를 이용하여 시스템 스택을 이용
- BFS를 그냥 써도 될떄가 많음

##### 예제 코드
~~~python 
# BFS는 큐 없어질때까지 그냥 있으면 되지만 얘는 root 의 자식이 없을때 까지 드루감 
def DFS(root):
    # 일단 오셨으니 방문 처리 하겠사옵니다.
    visited[root] = 1
    # 자식 없으면 그대로 함수 종료됨, iterate 할 애가 으므로
    for elem in child[root]:
        if not visited[elem]:
            DFS(elem)
    return visited
~~~