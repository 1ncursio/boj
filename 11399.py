"""
1 2 3 3 4

1 = 1
1 2 = 3
1 2 3 = 6
1 2 3 3 = 9
1 2 3 3 4 = 13
"""


N = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0
len_p = len(P)
for p in P:
    result += len_p * p
    len_p -= 1

print(result)
