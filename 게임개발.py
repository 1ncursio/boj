n, m = map(int, input().split())

x, y, player_dir = map(int, input().split())

dirs = [
    (-1, 0),  # 북
    (0, 1),  # 동
    (1, 0),  # 남
    (0, -1),  # 서
]

matrix = [list(map(int, input().split())) for _ in range(n)]
visits = [[False for _ in range(m)] for _ in range(n)]

visits[y][x] = True
print(visits)
# while True:
#     if dirs[player_dir]:
