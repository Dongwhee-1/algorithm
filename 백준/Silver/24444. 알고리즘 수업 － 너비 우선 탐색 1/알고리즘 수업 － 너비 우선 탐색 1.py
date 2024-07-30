import sys
from collections import deque

n, m, r = tuple(map(int, sys.stdin.readline().split()))

edges = [ list() for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
order = 1
q = deque()

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    edges[x].append(y)
    edges[y].append(x)

for i in range(len(edges)):
    edges[i].sort()

def bfs(start):
    global order
    visited[start] = order
    order += 1
    q.append(start)
    while q:
        u = q.popleft()
        for ele in edges[u]:
            if visited[ele] == 0:
                visited[ele] = order
                order += 1
                q.append(ele)

bfs(r)
for i in range(1, n+1):
    print(visited[i])