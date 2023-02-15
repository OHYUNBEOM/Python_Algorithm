# Queue 구현
# 전역 변수
SIZE=0
queue=[]
front,rear=-1,-1
# Queue 꽉 찼는지 확인
def isQueueFull():
    if (rear==SIZE-1):
        return True
    else:
        return False
# Queue 비어있는지 확인
def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front==rear):
        return True
    else:
        return False
#Queue 데이터 삽입
def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print('Queue is Full')
    else:
        rear+=1
        queue[rear]=data
#Queue 데이터 추출
def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('Queue is Empty')
        return None
    else:
        front+=1
        data=queue[front]
        queue[front]=None
        #뽑을때마다 앞으로 당기면서 queue의 data값 위치 맞춰줘야함
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front -=1
        rear -=1
        ##
        return data
#Queue front+1 위치 데이터 확인
def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('Queue is Empty')
        return None
    return queue[front+1]

if __name__=='__main__':
    SIZE=int(input('Queue 크기 입력-->'))
    queue=[None for _ in range(SIZE)]
    front,rear=-1,-1
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) >> ')
        if select.lower() == 'x':       # 종료
            break

        elif select.lower()=='i':
            data=input('입력할 데이터>>')
            enQueue(data)
            print('큐 상태 : ',queue)
            print()

        elif select.lower()=='e':
            data=deQueue()
            print('추출된 데이터 >>',data)
            print('큐 상태 : ',queue)
            print()

        elif select.lower()=='v':
            data=peek()
            print('확인된 데이터 >>',data)
            print('큐 상태 : ',queue)
            print()

        else:
            continue            
    print('스택 프로그램 종료')