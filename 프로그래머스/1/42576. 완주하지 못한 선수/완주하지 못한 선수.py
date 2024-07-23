from collections import defaultdict


def solution(participant, completion):
    p_dict = defaultdict(int)
    for i in range(len(participant)):
        p_dict[participant[i]] += 1
    while len(completion) != 0:
        c = completion.pop()
        p_dict[c] -= 1
        if p_dict[c] == 0:
            p_dict.pop(c)
    answer = list(p_dict.keys())[0]
    return answer