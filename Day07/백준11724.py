#이 받아쓰기 하는 수업이 무슨 의미가 있을까.
#백준 11724 - 연결요소 개수 확인
#파이썬 재귀호출 1000번까지 가능
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split()) # 6 5 일 때
A=[[] for _ in range(n+1)] # x, 7열 2차원 리스트
visited=[False]*(n+1) #[0,1,2,3,4,5,6,]

#DFS(재귀함수)
def DFS(v):
    visited[v]=True
    for i in A[v]:
        if not visited[i]:#방문을 안했다면
            DFS(i)

for _ in range(m): #엣지(edgt) 개수 만큼
    s,e=map(int,input().split())
    A[s].append(e) #무방향이기에 양쪽 edge 추가
    A[e].append(s)

count=0

for i in range(1,n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)