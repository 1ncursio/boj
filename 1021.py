import sys
from collections import deque


"""
큐의 길이 N
뽑아내는 개수 M
뽑으려는 수의 인덱스들의 deque picks
큐의 위치 deque indexes

picks가 있는 동안:
    뽑으려는 원소가 첫번째에 있다면:
        뽑기
        picks에서 제거
        컨티뉴
    
    뽑으려는 원소가 큐의 왼쪽 반에 있다면:
        큐를 왼쪽으로 회전
        카운트 증가
    아니라면:
        큐를 오른쪽으로 회전
        카운트 증가
"""


n, m = map(int, sys.stdin.readline().rstrip().split())
picks = deque(list(map(int, sys.stdin.readline().rstrip().split())))

indexes = deque([i + 1 for i in range(n)])

count = 0

while picks:
    if indexes[0] == picks[0]:
        picks.popleft()
        indexes.popleft()
        continue

    mid_idx = len(indexes) // 2

    while indexes[0] != picks[0]:
        if indexes.index(picks[0]) > mid_idx:
            indexes.rotate(1)
        else:
            indexes.rotate(-1)
        count += 1

sys.stdout.write(str(count))
