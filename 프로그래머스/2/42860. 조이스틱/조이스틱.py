def solution(name):
    answer = 0
    atoz = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(name)):
        if name[i] == "A":
            pass
        else:
            idx = atoz.find(name[i])
            answer += min(idx + 1, 25 - idx)
    move = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        distance = i + i + (len(name) - next)
        move = min(move, distance)

        distance = (len(name) - next) * 2 + i
        move = min(move, distance)
        
    return answer + move

