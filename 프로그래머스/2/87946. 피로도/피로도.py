import itertools

def solution(k, dungeons):
    answer = -1
    arr = itertools.permutations(dungeons, len(dungeons))
    for ways in arr:
        start = k
        count = 0
        for i in ways:
            if i[0] <= start:
                count += 1
                start -= i[1]
        if answer < count:
            answer = count
    return answer