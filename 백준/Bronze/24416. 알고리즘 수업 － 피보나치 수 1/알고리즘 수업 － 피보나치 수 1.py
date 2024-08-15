import sys

n = int(sys.stdin.readline())

def recursion(n):
    fibo = [0 for _ in range(n)]
    for i in range(n):
        if i ==  0 or i == 1:
            fibo[i] = 1
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n-1]

a = recursion(n)
b = n-2

print(" ".join([str(a), str(b)]))