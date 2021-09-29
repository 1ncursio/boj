from collections import deque

T = int(input())

Ns = []
Ms = []
Deqs = []
Is = []

for _ in range(T):
    """
    문서의 개수 N
    몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째 M

    N개의 문서의 중요도 Deq
    0 <= M < N
    """
    N, M = map(int, input().split())
    Deq = deque((map(int, input().split())))
    I = deque([i for i in range(N)])

    Ns.append(N)
    Ms.append(M)
    Deqs.append(Deq)
    Is.append(I)

for N, M, Deq, I in zip(Ns, Ms, Deqs, Is):
    count = 0

    while Deq:
        if Deq[0] == max(Deq):
            deq_first = Deq.popleft()
            I_first = I.popleft()
            count += 1
            if I_first == M:
                print(count)
                break
        else:
            Deq.rotate(-1)
            I.rotate(-1)
