import sys
from itertools import permutations
from collections import deque

n = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split()))

i = n - 1
while i > 0 and arr[i-1] <= arr[i]:
    i -= 1

# 이미 가장 작은 순열인 경우
if i == 0:
    print(-1)
else:
    j = n - 1
    # i-1 위치의 수보다 작은 수 중에서 가장 큰 수 찾기
    while arr[i-1] <= arr[j]:
        j -= 1
    # 교환
    arr[i-1], arr[j] = arr[j], arr[i-1]
    # i 이후의 부분을 내림차순으로 정렬
    arr = arr[:i] + sorted(arr[i:], reverse=True)
    print(" ".join(map(str, arr)))