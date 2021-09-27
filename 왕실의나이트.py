x, y = list(input())
x = ord(x) - 96
y = int(y)

moves = (
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
)

count = 0

for move in moves:
    moved = [a + b for a, b in zip([x, y], move)]
    if min(moved) >= 1 and max(moved) <= 8:
        count += 1

print(count)
