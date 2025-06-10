"""
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
union_set = [i for i in range(v+1)]
edges = []
result = 0

def union(x, y):
    a = y
    while union_set[a] != a:
        a = union_set[a]
    union_set[a] = union_set[x]

for _ in range(e):
    start, dest, cost = map(int, input().split())
    edges.append([start, dest, cost])

edges.sort(key=lambda x:x[2])

for i in range(e):
    start, dest, cost = edges[i]
    if union_set[start] != union_set[dest]:
        union(start, dest)
        result += cost

print(result)
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
union_set = [i for i in range(v+1)]
edges = []
result = 0

def union(x, y):
    a = find(x)
    b = find(y)
    
    if a < b:
        union_set[b] = a
    else:
        union_set[a] = b
    
def find(x):
    if union_set[x] == x:
        return x
    union_set[x] = find(union_set[x])
    return union_set[x]

def isSame(x, y):
    return find(x) == find(y)

for _ in range(e):
    start, dest, cost = map(int, input().split())
    edges.append([start, dest, cost])

edges.sort(key=lambda x:x[2])

for i in range(e):
    start, dest, cost = edges[i]
    if not isSame(start, dest):
        union(start, dest)
        result += cost

print(result)

