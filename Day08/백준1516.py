# 백준 1516-게임개발
from collections import deque

n=int(input())
a=[[] for _ in range(n+1)] #0번 인덱스는 안씀
indegree = [0]*[n+1] #진입차수
selfbuild = [0]*[n+1] #자기건물 건축시간

for i in range(1,n+1):
    inputlist=list(map(int,input().split())) # 4 1 
    selfbuild[i]=inputlist[0]
    index=1
    while True: #인접리스트
        pretemp=inputlist[index]
        index+=1
        if pretemp == -1 : break #while문 탈출

        a[pretemp].append(i)
        indegree[i]+=1 # 진입차수 증가

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i) #1부터 시작 

result=[0]*(n+1)

while q: #위상정렬 수행
    now=q.popleft()
    for next in a[now]: #1--> 2, 3, 4
        indegree[next]-=1 #방문했으니까 -1감소
        #시간업데이트
        result[next]=max(result[next],result[now]+selfbuild[now])
        if indegree[next]==0:
            q.append(next)

for i in range(1,n+1):
    print(result[i]+selfbuild[i])