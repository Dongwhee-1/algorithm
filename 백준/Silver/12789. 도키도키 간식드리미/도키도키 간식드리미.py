import sys

n = int(sys.stdin.readline()) 
line = list(map(int, sys.stdin.readline().split()))

count = 1
stack = []
answer = "Sad"

for i in line:
    stack.append(i)
    while stack and stack[-1] == count:
        stack.pop()
        count += 1

if stack:
    print("Sad")
else:
    print("Nice")