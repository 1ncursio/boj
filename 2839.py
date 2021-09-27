import sys

n = int(sys.stdin.readline())

count = 0

for bag in [5, 3]:
    count += n // bag
    n %= bag

sys.stdout.write(str(count))
