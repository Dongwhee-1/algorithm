import sys
from collections import deque

n = int(sys.stdin.readline())
balloons = [x+1 for x in range(1,n)] #O(n)
q = deque(balloons)
paper = list(map(int, sys.stdin.readline().split()))
answer = ['1']
i = 1

while q:
    if paper[i-1] > 0:
        for i in range(1, paper[i-1]):
            q.append(q.popleft())
        i = q.popleft()
        answer.append(str(i))
    else:
        for i in range(1, -1*paper[i-1]):
            q.appendleft(q.pop())
        i = q.pop()
        answer.append(str(i))

print(" ".join(answer))
           
    
    
    
        