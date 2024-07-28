import sys
from collections import deque

n = int(sys.stdin.readline())
qs = list(map(int, sys.stdin.readline().split()))
elements = list(map(int, sys.stdin.readline().split()))
q = deque()


for i in range(n):
    if qs[i] == 0:
        q.append(elements[i])

k = int(sys.stdin.readline())
new_elements = list(map(int, sys.stdin.readline().split()))

answer= []
for i in range(k):
    q.appendleft(new_elements[i])
    answer.append(str(q.pop()))

print(" ".join(answer))