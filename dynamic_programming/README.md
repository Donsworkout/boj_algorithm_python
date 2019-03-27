[목록으로](https://github.com/Donsworkout/boj_algorithm_python/blob/master/README.md)

## Dynamic Programming
### 특징 / 풀이 순서
- 피보나치 같은 수열처럼 항 간 규칙이 분명히 존재한다.
ex) a[n] = a[n-2] + a[n-1] 
- 실제 경우의 수를 직접 계산하여 종이에 나열
- 점화식을 세워보고 맞는지 검증
- 코드는 아래와 같이 구성하여 응용한다
~~~python
#아래마냥 재귀로 호출해서 리턴하는 형태로 만든다
cache[n] = DP(n-2) + DP(n-1) 
return cache[n]
~~~
- 구한 값은 메모이제이션을 하여 오버헤드를 방지한다
- 점화식만 구하면 알고리즘 자체는 어렵지 않음
- 점화식 구하는게 어려워서 문제.. (DP로 풀릴지 판단하는 것이 더 어렵)

#### 오답노트
##### boj_2156.py
~~~ python 
# 3번 연속되지 않는 선에서 최대값 구하는 문제
# 3번 연속만 막으면 되므로 현재를 cur 이라고 했을때,
# d[cur-3] + arr[cur-1] + arr[cur] 
# d[cur-2] + arr[cur] 
# d[cur-1] => 얘는 현재 안고르는 경우
# 위의 세가지 케이스는 모든 상황을 대변한다
for i in range(3, n):
    p_max = max(d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i])
    d[i] = max(p_max, d[i-1])
~~~