import re

"""
복서 선수들의 몸무게 리스트 weights
복서 선수들의 전적 리스트 head2head
"""


def solution(weights, head2head):
    N = len(weights)
    answer = [i + 1 for i in range(N)]

    for i in reversed(range(N)):
        for j in reversed(range(N - 1)):
            w1, h1 = weights[j], head2head[j]
            w2, h2 = weights[j + 1], head2head[j + 1]
            win_rate1 = h1.replace("N", "")

    return answer
