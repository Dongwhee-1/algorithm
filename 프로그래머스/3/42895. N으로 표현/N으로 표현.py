from collections import deque

def solution(N, number):
    nums = [[int(str(N)*(i+1))] for i in range(8)]
    nums = [None] + nums

    if number == N:
        return 1
    for i in range(2,9):
        for j in range(1, i):
            for x in nums[j]:
                for y in nums[i - j]:
                    nums[i].append(x + y)
                    nums[i].append(x - y)
                    nums[i].append(x * y)
                    if y != 0:
                        nums[i].append(x // y)
        if number in nums[i]:
            return i
            break
    return -1