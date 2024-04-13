import sys
from heapq import heapify, heappop, heappush
from collections import Counter, defaultdict
from queue import SimpleQueue, PriorityQueue

input = sys.stdin.readline

g = None
def dijkstra(s, t):
    dist = [-1] * len(g)
    heap = [(0, s)]
    while heap:
        weight, to = heappop(heap)
        if to == t:
            return weight
        
        if dist[to] != -1:
            continue
        
        dist[to] = weight
        for c, w in g[to]:
            if dist[c] == -1:
                heappush(heap, (w + weight, c))

    return dist[t]

for i in range(int(input())):
    n, m, s, t = map(lambda a: int(a), input().split(' '))
    g = {i: [] for i in range(n)}
    
    for j in range(m):
        a, b, w = map(int,  input().split(' '))
        g[a].append((b, w))
        g[b].append((a, w))

    dist = -1
    if len(g[t]) != 0:
        dist = dijkstra(s, t)
    print(f'Case #{i + 1}:', 'unreachable' if dist == -1 else dist)