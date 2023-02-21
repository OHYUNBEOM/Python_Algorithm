#백준 1541번 잃어버린 괄호
answer=0
A=list(map(str,input().split('+')))
def mysum(i):
    sum=0
    temp=str(i).split('+')
    for i in temp:
        sum+=int(i)
    return sum

for i in range(len(A)):
    temp=mysum(A[i])
    if i==0:
        answer+=temp
    else:
        answer-=temp

print(answer)
