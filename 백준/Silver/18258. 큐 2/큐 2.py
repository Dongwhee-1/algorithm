import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for i in range(n):
    a = input().rstrip()
    if a == 'pop':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        a = a.split()
        q.append(a[-1])
        
