import sys
from collections import deque

n = int(sys.stdin.readline()) 
q = deque()

for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a == '3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a == '4':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a == '5':
        print(len(q))
    elif a == '6':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == '7':
        if q:
            print(q[0])
        else:
            print(-1)      
    elif a == '8':
        if q:
            print(q[-1])
        else:
            print(-1)       
    else:
        a = a.split()
        if a[0] == '1':
            q.appendleft(a[1])
        else:
            q.append(a[1])