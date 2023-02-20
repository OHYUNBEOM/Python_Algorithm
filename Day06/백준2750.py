# 백준 2750 수 정렬하기
n=int(input())
m=[]
for i in range(n):
    m.append(int(input()))
m.sort()
for i in range(n):
    print(m[i])