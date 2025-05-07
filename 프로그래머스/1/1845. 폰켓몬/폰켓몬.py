def solution(nums):
    max_num = len(nums)/2
    nums_unique = set(nums)
    if len(nums_unique) >= max_num:
        return max_num
    else:
        return len(nums_unique)