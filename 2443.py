N = int(input())

[print(" " * (i - 1), "*" * (2 * (N) - (2 * i - 1)), sep="") for i in range(1, N + 1)]
