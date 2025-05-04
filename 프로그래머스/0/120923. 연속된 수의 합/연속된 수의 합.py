def solution(num, total):
    answer = [x for x in range(0, num)]
    cur = sum(answer)
    if cur == total:
        return answer
    else:
        diff = (cur - total)//num
        answer = [x for x in range(0-diff, num-diff)]
    return answer