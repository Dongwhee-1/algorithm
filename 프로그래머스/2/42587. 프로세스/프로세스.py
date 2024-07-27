from collections import deque

def solution(priorities, location):
    answer = 0
    index = 100
    priorities = [[priorities[i], i] for i in range(len(priorities))]
    q = deque(priorities)  
    while index != location:
        a = q.popleft()
        is_max = True
        for i in q:
            if a[0] < i[0]:
                is_max = False
        if is_max:
            index = a[1]
            answer +=1
        else:
            q.append(a)                              
    return answer


# from collections import deque

# def solution(priorities, location):
#     ans = 0
#     index = [i for i in range(len(priorities))]
#     dq = deque(zip(index, priorities))
#     goal = dq[location]
#     answer = 0
#     while dq:
#         a = dq.popleft()
#         is_max = True
#         for i in dq:
#             if a[1] < i[1]:
#                 is_max = False  
#         if not is_max:
#             dq.append(a)
#         else:
#             answer +=1
#             if a == goal:
#                 break
#     return answer