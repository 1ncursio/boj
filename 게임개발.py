n, m = map(int, input().split())

x, y, player_dir = map(int, input().split())

dirs = [
    (-1, 0),  # λΆ
    (0, 1),  # λ
    (1, 0),  # λ¨
    (0, -1),  # μ
]

matrix = [list(map(int, input().split())) for _ in range(n)]
visits = [[False for _ in range(m)] for _ in range(n)]

visits[y][x] = True
print(visits)
# while True:
#     if dirs[player_dir]:
