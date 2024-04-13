import sys
from heapq import heapify, heappop, heappush
from collections import Counter, defaultdict
from queue import SimpleQueue, PriorityQueue

input = sys.stdin.readline
# sys.stdin = open('test.txt', 'r')
# sys.stdout = open('result.txt', 'w')

def dijkstra(target):
    if target == 0:
        return 0
    
    dist = [-1] * 100
    heap = [(-60, 0, -1)] # w, to, elevator-number
    
    while heap:
        w, t, elv = heappop(heap)

        if target == t:
            return w

        if dist[t] != -1:
            continue

        dist[t] = w
        for c, cw, celv in graph[t]:
            if dist[c] == -1 and elv != celv:
                heappush(heap, (cw + w + 60, c, celv))
    return dist[target]

try:
    while True:
        n, k = map(int, input().split())
        times = [*map(int, input().split())]
        graph = {i: [] for i in range(100)} 
        for i in range(n):
            floors = [*map(int, input().split())]
            for j in range(len(floors)):
                for l in range(j + 1, len(floors)):
                    weight = abs(floors[j] - floors[l]) * times[i]
                    graph[floors[j]].append((floors[l], weight, i)) 
                    graph[floors[l]].append((floors[j], weight, i))

        time = dijkstra(k)
        if time == -1:
            print('IMPOSSIBLE')
        else:
            print(time)
except:
    pass
    
