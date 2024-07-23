import sys 


n = int(sys.stdin.readline()) 

for i in range(n):
    is_vps = True
    brackets = sys.stdin.readline().strip()
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
        
