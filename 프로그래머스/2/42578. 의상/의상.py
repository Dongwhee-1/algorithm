from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for i in clothes:
        clothes_dict[i[-1]] += 1
    if len(clothes_dict) == 1:
        answer = list(clothes_dict.values())[0]
    else:
        for i in list(clothes_dict.values()):
            answer *= i+1
        answer -= 1
    return answer
    