"""
전위순회: 루트 왼쪽 오른쪽
중위순회: 왼쪽 루트 오른쪽
후위순회: 왼쪽 오른쪽 루트

클래스를 이용하자 !
이진트리라 배열도 이용할 수 있으 !

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.data, end="")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end="")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="")

n = int(input())
tree = {}

for _ in range(n):
    data, left, right = input().split()
    if data not in tree:
        tree[data] = Node(data)
    node = tree[data]

    if left != '.':
        if left not in tree:
            tree[left] = Node(left)
        node.left = tree[left]
    
    if right != '.':
        if right not in tree:
            tree[right] = Node(right)
        node.right = tree[right]

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

배열로 만들면
[A, B, C, D, ., E, F, ., ., ., ., ., G]
parent = k
left = 2k+1
right = 2k+2
parent 찾을 때는 (k-1)//2

26개가 한쪽일 경우
[A, ., B, ., ., ., C, .] ...

메모리 때문에 안돼 ㅠㅠ 이거는 힙이긴 해,,

그냥 딕셔너리가 더 간편함
tree = {}
tree[root] = left, right  # {'A': ('B', 'C')}
순회 시
tree[v][0], tree[v][1]
"""

import sys
input = sys.stdin.readline

n = int(input())
tree = [0] * 10000000
root = 0

for i in range(n):
    data, left, right = input().split()
    if data in tree:
        temp = tree.index(data)
    else:
        temp = i
    tree[temp] = data
    if left != '.':
        tree[2*temp + 1] = left
    if right != '.':
        tree[2*temp + 2] = right
    
def preorder(index):
    if tree[index] == 0:
        return
    print(tree[index], end="")
    preorder(index*2+1)
    preorder(index*2+2)

def inorder(index):
    if tree[index] == 0:
        return
    inorder(index*2+1)
    print(tree[index], end="")
    inorder(index*2+2)

def postorder(index):
    if tree[index] == 0:
        return
    postorder(index*2+1)
    postorder(index*2+2)
    print(tree[index], end="")

preorder(root)
print()
inorder(root)
print()
postorder(root)
    

