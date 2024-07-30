import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m, v = tuple(map(int, sys.stdin.readline().split()))
edges = [list() for _ in range(n+1)]
b_visited = [0 for _ in range(n+1)]
d_visited = [0 for _ in range(n+1)]
q = deque()
dfs_list = []
bfs_list = []

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    edges[x].append(y)
    edges[y].append(x)

for i in range(len(edges)):
    edges[i].sort()

def dfs(v, edges):
    dfs_list.append(str(v))
    d_visited[v] = 1
    for i in edges[v]:
        if d_visited[i] == 0:
            dfs(i, edges)

def bfs(v):
    bfs_list.append(str(v))
    b_visited[v] = 1
    q.append(v)
    while q:
        u = q.popleft()
        for e in edges[u]:
            if b_visited[e] == 0:
                b_visited[e] = 1
                bfs_list.append(str(e))
                q.append(e)

dfs(v, edges)
bfs(v)
print(" ".join(dfs_list))
print(" ".join(bfs_list))