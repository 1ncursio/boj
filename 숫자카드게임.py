n, m = map(int, input().split())

list = [list(map(int, input().split())) for _ in range(n)]
"""
각 행에서 최솟값을 뽑아야하므로 각 행의 최솟값이 가장 큰 행에서 뽑아야 함

행 반복:
    열최솟값 리스트에 각 열에서의 최솟값 추가
열 최솟값 리스트 중에서 최댓값 출력

"""

col_mins = []

for row in list:
    col_mins.append(min(row))

print(max(col_mins))
