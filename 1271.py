import sys

money, n = map(int, input().split())

sys.stdout.write(f"{str(money // n)}\n")
sys.stdout.write(str(money % n))
