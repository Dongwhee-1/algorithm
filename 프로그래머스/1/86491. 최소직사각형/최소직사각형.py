def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    maxw = max([x[0] for x in sizes])
    maxh = max([x[1] for x in sizes])
    answer = maxw * maxh
    return answer