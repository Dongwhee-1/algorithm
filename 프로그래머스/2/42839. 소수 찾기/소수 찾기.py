import math
from itertools import permutations

def solution(numbers):
    def is_prime_number(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    answer = []
    for i in range(len(numbers)):
        for j in permutations(numbers, i+1):
            x = int("".join(j))
            if is_prime_number(x) and x not in answer and x >= 2:
                answer.append(x)
    return len(answer)