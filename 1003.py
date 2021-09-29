count = [0] * 2

d = [0] * 40
d[0] = 1
d[1] = 1


def fibonacci(n):
    if n == 0:
        count[0] += 1
        return 0
    elif n == 1:
        count[1] += 1
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]


T = int(input())

Ns = []
for _ in range(T):
    N = int(input())
    Ns.append(N)

for N in Ns:
    count = [0] * 2
    fibonacci(N)
    print(" ".join(map(str, count)))
