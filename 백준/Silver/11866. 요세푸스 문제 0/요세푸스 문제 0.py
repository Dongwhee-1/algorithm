import sys
from collections import deque
n, k = tuple(map(int, sys.stdin.readline().split()))

Josephus = [i+1 for i in range(n)]
answer = []
q = deque(Josephus)
count = 1
while q: 
    a = q.popleft() 
    if count == k:
        answer.append(str(a)) 
        count = 1
    else:
        q.append(a)
        count += 1

print("<" + ", ".join(answer) + ">")
    
# O(n*k), 1<=n,k<=1,000이므로 최대 연산은 1,000,000 시간 제한 달성
