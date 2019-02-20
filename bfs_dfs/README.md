## BFS / DFS
###BFS
- BFS는 층을 기반으로 센다 (거리)
- 따라서 최소 거리 찾기가 쉬움
- Queue를 사용한다.
- Python은 collections 의 Deque 를 사용해야 시간에러 안남
- 층을 셀때는 층마다 대기중인 queue의 length 를 세어주고 거기에 count 를 넣는다. (어차피 queue에 pop 할만큼만 pop 하기 때문!
