import sys
from collections import defaultdict

name = sys.stdin.readline().rstrip()
length = len(name)
name = sorted(name)
n_dict = defaultdict(int)

for i in name:
    n_dict[i] += 1

odd = 0
for j in n_dict.values():
    if j % 2 == 1:
        odd+= 1

if odd >= 2:
    print("I'm Sorry Hansoo")
else:
    half = []
    middle = []
    for key in n_dict.keys():
        if n_dict[key] % 2 == 1:
            half.append(key * (n_dict[key] // 2))
            middle.append(key)
        else:
            half.append(key * (n_dict[key] // 2))
    print("".join(half + middle + half[::-1]))