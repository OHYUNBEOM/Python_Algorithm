# 백준 12891 DNA 비밀번호
# 의미없는 받아쓰기 같아서 오류수정 안했고 돌려보면 오류날거임
checkList=[0]*4
mylist=[0]*4
checkSecret=0

def myadd(c):
    global checkList,mylist,checkSecret
    if c=='A':
        mylist[0]+=1
        if mylist[0] == checkList[0]:
            checkSecret+=1
        elif c=='C':
            mylist[1]+=1
            if mylist[1]==checkList[1]:
                checkSecret+=1
        elif c=='G':
            mylist[2]+=1
            if mylist[2]==checkList[2]:
                checkSecret+=1
        elif c=='T':
            mylist[3]+=1
            if mylist[3]==checkList[3]:
                checkSecret+=1

def myremove(c):
    global checkList,mylist,checkSecret
    if c=='A':
        if mylist[0]==checkList[0]:
            checkSecret-=1
        mylist[0]-=1
    elif c=='C':
        if mylist[1]==checkList[1]:
            checkSecret-=1
        mylist[1]-=1
    elif c=='G':
        if mylist[2]==checkList[2]:
            checkSecret-=1
        mylist[2]-=1
    elif c=='T':
        if mylist[3]==checkList[3]:
            checkSecret-=1
        mylist[3]-=1

S,P=map(int,input().split())
Result=0
A=list(input())
checkList=list(map(int,input().split()))

for i in range(4):
    if checkList[i]==0:
        checkSecret+=1

for i in range(P):
    myadd(A[i])

if checkSecret==4:
    Result+=1

for i in range(P,5):
    j=i-P
    myadd(A[i])
    myremove(A[j])
    if checkSecret==4:
        Result+=1

print(Result)