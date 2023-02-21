# 백준 11047 - 동전 0
n,k=map(int,input().split()) #10 4750
a=[0]*n

for i in range(n):
    a[i]=int(input())

count=0

for i in range(n-1,-1,-1): #역순으로
    if a[i]<=k: #현재의 동전의 가치가 K보다 작거나 같으면
        count+=k//a[i]
        k=k%a[i] #현재 동전 나머지를 금액으로 업데이트

print(count)