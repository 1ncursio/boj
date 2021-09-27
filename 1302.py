import sys

count = int(input())
dict = {}
for i in range(count):
    key = input()
    dict.setdefault(key, 0)
    dict[key] += 1

m = max(dict.values())
answers = [i for i in dict if dict[i] == m]

if len(answers) == 1:
    sys.stdout.write(str(answers[0]))
else:
    answers.sort()
    sys.stdout.write(str(answers[0]))
