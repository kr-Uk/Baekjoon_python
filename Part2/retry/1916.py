import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]
for _ in range(m):
    s, d, cost = map(int, input().split())
    graph[s].append([d, cost])
    
start, dest = map(int, input().split())
distance[start] = 0
heap = []
heapq.heappush(heap, [0, start])

while heap:
    curr_cost, curr = heapq.heappop(heap)
    if distance[curr] < curr_cost:
        continue
    for next, next_cost in graph[curr]:
        sum_cost = curr_cost + next_cost
        if sum_cost >= distance[next]:
            continue
        distance[next] = sum_cost
        heapq.heappush(heap, [sum_cost, next])

print(distance[dest])