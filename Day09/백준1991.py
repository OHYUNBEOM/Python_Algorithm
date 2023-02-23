#백준 1991 - 트리순회
import sys
input=sys.stdin.readline
n=int(input())
tree={}

for _ in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]

def preorder(now):
    if now=='.':
        return
    print(now,end='')
    preorder(tree[now][0])
    preorder(tree[now][1])

def inorder(now):
    if now=='.':
        return
    inorder(tree[now][0])
    print(now,end='')
    inorder(tree[now][1])

def postorder(now):
    if now=='.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')