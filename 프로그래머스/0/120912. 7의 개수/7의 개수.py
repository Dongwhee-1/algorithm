def solution(array):
    array_str = "".join(map(str, array))
    answer = 0
    for i in array_str:
        if i == "7":
            answer += 1
    return answer