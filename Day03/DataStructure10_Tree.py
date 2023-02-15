# 이진 탐색트리 구현
# 전역변수 선언
memory=[]
root=None
nameAry=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

class TreeNode:
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None

if __name__=='__main__':
    node=TreeNode() #TreeNode 다 가지는 node 생성함
    node.data=nameAry[0] #node.data에 블랙핑크 들어감
    root=node #root는 블랙핑크 들어간 noode 가지고있음
    memory.append(node) #memory에다가 추가함

for name in nameAry[1:]: #0에는 블랙핑크 들어가있고 그 뒤로 쭉 돌아가면서
    node=TreeNode()
    node.data=name#node.data에 레드벨벳~트와이스 추가로 들어감
    current=root
    while True:
        if name<current.data: #부모노드 왼쪽 / 걸그룹이름 ㄱㄴㄷㄹ 비교해서 작으면 왼쪽으로
            if current.left==None:
                current.left=node
                break
            current=current.left
        else: #부모노드 오른쪽 / 이름 ㄱㄴㄷㄹ 비교해서 크면 오른쪽으로
            if current.right==None:
                current.right=node
                break
            current=current.right
    memory.append(node)
print('이진 탐색 트리 구성 완료')

search=input('찾을 걸그룹 입력 > ')
current=root
while True:
    if search==current.data:
        print(search,'찾음')
        break
    elif search < current.data:
        if current.left==None:
            print(search,'못찾음')
            break
        else:
            current=current.left
    else:
        if current.right==None:
            print(search,'못찾음')
            break
        else:
            current=current.right

# findName='마마무'
# current=root
# while True:
#     if findName==current.data:
#         print(findName,'을(를) 찾음.')
#         break
#     elif findName<current.data:
#         if current.left==None:
#             print(findName,'이(가) 트리에 없음')
#             break
#         current=current.left
#     else:
#         if current.right==None:
#             print(findName,'이(가) 트리에 없음')
#             break
#         current=current.right