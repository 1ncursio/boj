K = int(input())

Ns = [int(input()) for _ in range(K)]

Answers = []

for N in Ns:
    if N != 0:
        Answers.append(N)
    else:
        Answers.pop()

print(sum(Answers))
