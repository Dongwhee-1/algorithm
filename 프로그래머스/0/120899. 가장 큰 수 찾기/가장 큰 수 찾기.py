from collections import deque

def solution(array):
    q = deque(array)
    max_num = -1
    count = 0
    while q:
        cur = q.popleft()
        if max_num < cur:
            max_num = cur
            answer = [max_num, count]
        count += 1
    return answer