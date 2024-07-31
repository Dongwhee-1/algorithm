import sys
from collections import deque
n, m = tuple(map(int, sys.stdin.readline().split()))

maze = []
for _ in range(n):
    maze.append([int(x) for x in sys.stdin.readline().rstrip()])
q = deque()
visited = [[0] * m for _ in range(n)]
y_move = [1, 0, -1, 0]
x_move = [0, 1, 0, -1]

def bfs(x, y):
    visited[y-1][x-1] = 1
    q.append([y, x, 1])
    while q:
        now = q.popleft()
        y, x, count = now[0], now[1], now[2]
        if y == n and x == m:
            break
        else:
            for i in range(4):
                y_next = y + y_move[i]
                x_next = x + x_move[i]
                if y_next >= 1 and y_next <= n and x_next >= 1 and x_next <= m:
                    if maze[y_next-1][x_next-1] == 1 and visited[y_next-1][x_next-1] == 0:
                        visited[y_next-1][x_next-1] = 1
                        q.append([y_next, x_next, count+1])
    return count

print(bfs(1,1))