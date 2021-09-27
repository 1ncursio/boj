import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        for k in range(K):
            C[n][k] += A[n][m] * B[m][k]

for n in range(N):
    for k in range(K):
        sys.stdout.write(str(C[n][k]) + " ")
    sys.stdout.write("\n")
