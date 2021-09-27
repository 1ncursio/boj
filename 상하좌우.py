n = int(input())
moves = input().split()

matrix = [1, 1]
dic = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}


def clamp(num, min_val, max_val):
    return max(min(num, max_val), min_val)


for move in moves:
    matrix = [m + d for m, d in zip(matrix, dic[move])]
    matrix = list(map(lambda x: clamp(x, 1, n), matrix))


print(matrix)
