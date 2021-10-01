N, K = map(int, input().split())

As = [int(input()) for _ in range(N)][::-1]

count = 0

while K != 0:
    for A in As:
        if A > K:
            continue
        count += K // A
        K %= A

print(count)
