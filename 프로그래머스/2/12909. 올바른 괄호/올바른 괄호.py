def solution(s):
    p = []
    for i in range(len(s)):
        if len(p) != 0 and p[-1] == "(" and s[i] == ")":
            p.pop()
        else:
            p.append(s[i])   
    if len(p) == 0:
        return True
    return False