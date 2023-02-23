#백준 11657번 타임머신으로 빨리가기 - 벨만포드
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
edges=[]
distance=[sys.maxsize]*(n+1)

for i in range(m):
    start,end,time=map(int,input().split())
    edges.append((start,end,time))

distance[1]=0

for _ in range(n-1):
    for start,end,time in edges:
        if distance[start] != sys.maxsize and distance[end]>distance[start]+time:
            distance[end]=distance[start]+time

mcycle=False
for start,end,time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mcycle=True

if not mcycle:
    for i in range(2,n+1):
        if distance[i]!=sys.maxsize:
            print(distance[i])
        else:
            print(-1)

else:
    print(-1)