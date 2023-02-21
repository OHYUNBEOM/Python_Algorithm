#백준 1929 소수 구하기
import math
m,n=map(int,input().split())
a=[0]*(n+1) #초기화

for i in range(2,n+1):
    a[i]=i # 인덱스를 채워넣기

for i in range(2,int(math.sqrt(n))+1): #제곱근까지만 수행
    if a[i]==0:
        continue
    for j in range(i+i,n+1,i): #배수로 지우기
        a[j]=0 #소수가 아닌건 지움

for i in range(m,n+1):
    if a[i]!=0:
        print(a[i])