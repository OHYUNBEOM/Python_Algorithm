#백준 2751 수 정렬하기 2
import sys
input=sys.stdin.readline #백준 2750과 차이점임 sys.stdin없으면 시간초과뜸
arr=[]
n=int(input())
for i in range(n):
    m=int(input())
    arr.append(m)
arr.sort()
for i in range(len(arr)):
    print(arr[i])