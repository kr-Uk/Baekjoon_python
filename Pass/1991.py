import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(r):
    if r == '.':
        return
    print(r, end = "")
    preorder(tree[r][0])
    preorder(tree[r][1])

def inorder(r):
    if r == '.':
        return
    inorder(tree[r][0])
    print(r, end="")
    inorder(tree[r][1])

def postorder(r):
    if r == '.':
        return
    postorder(tree[r][0])
    postorder(tree[r][1])
    print(r, end="")
    
preorder('A')
print()
inorder('A')
print()
postorder('A')