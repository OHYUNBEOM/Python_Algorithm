#백준 1260 DFS와 BFS
from collections import deque
n,m,start=map(int,input().split())
a=[[] for _ in range(n+1)]

for _ in range(m):
    s,e=map(int,input().split())
    a[s].append(e) #양방형 edge이므로 양쪽에 edge 더하기
    a[e].append(s)

for i in range(n+1):
    a[i].sort()

def DFS(v):
    print(v,end=' ')
    visited[v]=True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

visited=[False] * (n+1)
DFS(start)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now_node=queue.popleft()
        print(now_node,end=' ')
        for i in a[now_node]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
print()
visited=[False]*(n+1)
BFS(start)