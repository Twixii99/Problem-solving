import sys
from heapq import heapify, heappop, heappush
from collections import Counter, defaultdict
from queue import SimpleQueue, PriorityQueue

# input = sys.stdin.readline
# sys.stdin = open('test.txt', 'r')
# sys.stdout = open('result.txt', 'w')

def isValid(a, b):
    return 0 <= b < w and 0 <= a < h and graph[a][b] != -1

def dijkstra():
    visited = {}
    heap = [(0, start)]

    while heap:
        w, to = heappop(heap)

        if to == end:
            return w
        
        if to in visited:
            continue

        visited[to] = w
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            idx = to[0] + dx, to[1] + dy
            if isValid(*idx) and idx not in visited:
                heappush(heap, (graph[idx[0]][idx[1]] + w, idx))

    return -1

while True:
    w, h = map(int, input().split())
    if w == 0: break

    graph = []
    start, end = None, None
    for i in range(h):
        data = []
        for j, c in enumerate(input()):
            if '1' <= c <= '9':
                data.append(int(c))
            elif c == 'X':
                data.append(-1)
            elif c == 'S':
                start = (i, j)
                data.append(0)
            else:
                end = (i, j)
                data.append(0)
        graph.append(data)

    print(dijkstra())
    
    input()