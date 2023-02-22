# Python_CodingTest_2023
Python_CodingTest_Repisitory

# 1일차
1. 코딩테스트 Tutorial
2. 알고리즘 
    - 자료구조
    - 백준 알고리즘 문제 풀이
        - 구간합

# 2일차
! 파이썬 파일명에는 '_'만 사용할 것
1. 알고리즘
    - 구간합 2
    - 자료구조
        - 연결리스트
        - 스택
    - 백준 알고리즘 풀이
        - 개인적으로 진행

# 3일차
1. 코딩테스트 학습
    - 자료구조
        - 스택
        - 큐
        - 스택,큐 pythonds 확인
        - 그래프

# 4일차
1. 코딩테스트 학습
    - 자료구조
        - 그래프
        - 깊이 우선 탐색(DFS)
        - 재귀호출
        
# 6일차
1. 코딩테스트 학습
    - 자료구조
        - deque(덱)
    - 백준 알고리즘 문제 풀이
        - 1253,2750,2751,12891
```python
import sys
input=sys.stdin.readline
N=int(input())
count=0
A=list(map(int,input().split())) 
A.sort()
for k in range(N):
    find=A[k]
    i=0;j=N-1 #i는 리스트 첫번째, j는 리스트 마지막에 위치
    while i<j: #두 인덱스가 만나면 while 종료
        if A[i]+A[j]==find: # 두 수의 합이 찾는 수와 일치
            if i!=k and j!=k: #i,j는 k와 같은 위치가 되면 안됨
                count+=1
                break
            elif i==k : i+=1
            elif j==k: j-=1
        elif A[i]+ A[j] < find: #i를 증가시켜야 합의 수가 커짐
            i+=1
        elif A[i] + A[j] > find: #두 수의 합이 찾는수보다 크면 j 감소시켜야 합의 수 작아짐
            j-=1
print(count)
```

# 7일차
1. 코딩테스트 학습
    - 자료구조
        - 그래프
        - Priority Queue(우선순위 큐)
        - HeapQueue
    - 알고리즘(탐색)
        - DFS/BFS

# 8일차
1. 코딩테스트 학습
    - 자료구조
    - 알고리즘
        - 정수론
        - 그래프 활용
        