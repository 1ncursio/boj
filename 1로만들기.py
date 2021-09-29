X = int(input())

count = 0

while X != 1:
    count += 1
    if X % 5 == 0:
        X //= 5
        continue
    elif X % 3 == 0:
        X //= 3
        continue
    elif X % 2 == 0:
        X //= 2
        continue
    else:
        X -= 1

print(count)
