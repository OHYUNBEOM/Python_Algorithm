# 백준 1753번 - 최단 경로 구하기
import sys
input=sys.stdin.readline
from queue import PriorityQueue

v,e=map(int,input().split())
k=int(input())
distance=[sys.maxsize]*(v+1)
visited=[False]*(v+1)
mylist=[[] for _ in range(v+1)]
q=PriorityQueue()

for _ in range(e):
    u,v,w = map(int,input().split()) #u --> v 가중치 w 엣지
    mylist[u].append((v,w))

q.put((0,k)) #시작점 K
distance[k]=0

while q.qsize()>0:
    current=q.get()
    c_v=current[1]
    if visited[c_v]:
        continue
    visited[c_v]=True
    for tmp in mylist[c_v]:
        next=tmp[0]
        value=tmp[1]
        if distance[next]>distance[c_v] + value: # 최소 거리로 업데이트
            distance[next]=distance[c_v]+value 
            #가중치가 정렬 기준이므로 순서를 가중치,목표 노드 순으로 우선순위 큐 설정
            q.put((distance[next],next)) # 가중치로 오름차순

for i in range(1,v+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')