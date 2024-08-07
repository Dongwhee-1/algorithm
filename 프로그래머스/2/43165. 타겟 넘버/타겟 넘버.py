def solution(numbers, target):
    answer = 0
    def dfs(number, count, target):
        nonlocal answer
        if count == len(numbers)-1:
            if number == target:
                answer += 1
        else:
            count += 1
            number += numbers[count]
            dfs(number, count, target)
            number -= 2*numbers[count]
            dfs(number, count, target)
    dfs(0, -1, target)
    return answer