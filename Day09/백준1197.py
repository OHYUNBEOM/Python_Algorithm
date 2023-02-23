#백준 1197-최소신장트리 구하기
import sys
from queue import PriorityQueue

input=sys.stdin.readline
n,m=map(int,input().split())
pq=PriorityQueue()
parent=[0]*(n+1)

#유니온파인드를 위한 대표노드 리스트 초기화
for i in range(n+1):
    parent[i]=i

for i in range(m):
    s,e,w=map(int,input().split())
    pq.put((w,s,e))

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

useedge=0
result=0

while useedge<n-1:#mst는 항상 n-1의 엣지를 사용함
    w,s,e=pq.get()
    if find(s)!=find(e):#같은 부모가 아닌 경우만 연결
        union(s,e)
        result+=w
        useedge+=1

print(result)