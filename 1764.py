import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dict = {}
for i in range(n + m):
    key = sys.stdin.readline().rstrip()
    dict.setdefault(key, 0)
    dict[key] += 1

answers = [i for i in dict if dict[i] != 1]

if len(answers) > 1:
    answers.sort()

sys.stdout.write(str(len(answers)))
sys.stdout.write("\n")
for answer in answers:
    sys.stdout.write(f"{answer}\n")
