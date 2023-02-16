# 깊이 우선 탐색
class Graph:
    def __init__(self,size):
        self.SIZE=size
        self.graph=[[0 for _ in range(size)] for i in range(size)]#2차원배열

G1=None
stack=[]
visitedAry=[] #방문한 정점

G1=Graph(4)
G1.graph[0][2]=1;G1.graph[0][3]=1
G1.graph[1][2]=1
G1.graph[2][0]=1;G1.graph[2][1]=1;G1.graph[2][3]=1
G1.graph[3][0]=1;G1.graph[3][2]=1

print('##G1 무방향 그래프##')
for item in G1.graph:
    print(item)

current=0 # 시작 정점
stack.append(current)
visitedAry.append(current) #스택, 방문기록

while(len(stack)!=0):
    next=None
    for vertex in range(4):
        if G1.graph[current][vertex]==1:
            if vertex in visitedAry : #방문한 적 있는 정점이면 탈락
                pass
            else: #방문한적이 없으면 다음 정점으로 지정
                next=vertex
                break
    if next!=None: # 다음 방문할 정점이 있으면
        current=next
        stack.append(current)
        visitedAry.append(current)
    else: #다음 방문할 정점이 없으면
        current=stack.pop()

print('방문 순서 -->',end=' ')
for i in visitedAry:
    print(chr(ord('A')+i),end=' ')
