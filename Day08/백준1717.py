# 백준 1717번 - 집합의 표현(유니온 파인드)
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
parent=[0]*(n+1) # = [0 for _ in range(n+1)]

def find(a): # find 연산
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a]) # 재귀호출 -> 경로압축

def union(a,b): #대표노드끼리 합치기
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

def checksame(a,b): #둘이 같은 집합인지 확인
    a=find(a)
    b=find(b)
    if a==b: return True
    else: return False

for i in range(0,n+1):
    parent[i]=i #1,1,2,2,3,3,4,4,5,5,6,6,7,7

for i in range(m):
    question,a,b=map(int,input().split()) #0 1 3 or 1 1 7
    if question ==0 :
        union(a,b)
    else:
        if checksame(a,b):
            print('Yes')
        else:
            print('No')