import sys
n, r1, c1, r2, c2 = tuple(map(int, sys.stdin.readline().split()))

def get_char(n, y, x):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    table_size = n * 2 - 1
    
    y %= table_size
    x %= table_size
    
    dist = abs(n - 1 - y) + abs(n - 1 - x)
    
    if dist < n:
        return alphabets[(dist) % 26]
    else:
        return "."

for i in range(r1, r2 + 1):
    row = []
    for j in range(c1, c2 + 1):
        row.append(get_char(n, i, j))
    print("".join(row))
