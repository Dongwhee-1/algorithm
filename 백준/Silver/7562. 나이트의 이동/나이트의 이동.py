import sys
from collections import deque

def bfs(i, starty, startx, endy, endx):
    board = [[0] * i for _ in range(i)]
    move_x = [-1, -2, -2, -1, 1, 2, 2, 1]
    move_y = [2, 1, -1, -2, 2, 1, -1, -2]
    q = deque()
    q.append([starty, startx, 0])
    while q:
        u = q.popleft()
        starty, startx, count = u[0], u[1], u[2]
        if starty == endy and startx == endx:
            print(count)
            break
        for k in range(len(move_x)):
            nexty = starty + move_y[k]
            nextx = startx + move_x[k]
            if 0 <= nexty <= i-1 and 0 <= nextx <= i-1:
                if board[nexty][nextx] == 0 or board[nexty][nextx] > count + 1:
                    board[nexty][nextx] = count + 1
                    q.append([nexty, nextx, count + 1])


n = int(sys.stdin.readline())
for _ in range(n):
    i = int(sys.stdin.readline())
    starty, startx = tuple(map(int, sys.stdin.readline().split()))
    endy, endx = tuple(map(int, sys.stdin.readline().split()))
    bfs(i, starty, startx, endy, endx)