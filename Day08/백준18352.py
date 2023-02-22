# 백준 18352번 - 특정 거리 도시 찾기
import sys
from collections import deque
input=sys.stdin.readline

n,m,k,x=map(int,input().split()) # 노드수,엣지수,목표거리,시작노드
a=[[] for _ in range(n+1)] #초기화
answer=[] #값을 담을 리스트
visited=[-1]*(n+1) #방문리스트 초기화

def bfs(v):
    q=deque()
    q.append(v)
    visited[v] +=1
    while q:
        now=q.popleft() 
        for i in a[now]:
            if visited[i]==-1: #미방문이면
                visited[i]=visited[now]+1
                q.append(i)

#두번째 줄부터 엣지 입력
for _ in range(m):
    s,e=map(int,input().split())
    a[s].append(e)

bfs(x) #시작점부터 bfs 시작

for i in range(n+1):
    if visited[i]==k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)