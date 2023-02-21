# 백준 1920 원하는 정수 찾기
# 시간초과뜸.. 이분탐색으로 해야하나봄
n = int(input())
arr1=list(map(int,input().split()))

m=int(input())
arr2=list(map(int,input().split()))

for num2 in range(len(arr2)):
    for num1 in range(len(arr1)):
        if arr2[num2]==arr1[num1]:
            print('1')
            break
        if num1==len(arr1)-1:
            print('0')