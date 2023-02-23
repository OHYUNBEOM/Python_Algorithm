#백준11404 - 가장 빠른 노선 구하기 - 플로이드 워셜
import sys
input=sys.stdin.readline
n=int(input()) #도시 5
m=int(input()) #노선개수 14
distance=[[sys.maxsize for j in range(n+1)] for i in range(n+1)]#6x6 인접행렬

for i in range(1,n+1): #인접 행렬 초기화
    distance[i][i]=0 #인접 행렬 초기화

for i in range(m):
    s,e,v = map(int,input().split())
    if distance[s][e]>v: #중복된 노선중 더 저렴한 버스가 있으면
        distance[s][e]=v

#플로이드 워셜 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==sys.maxsize:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()