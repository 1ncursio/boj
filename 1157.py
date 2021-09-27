import sys

word = input().upper()
dict = {}

for letter in word:
    dict.setdefault(letter, 0)
    dict[letter] += 1

m = max(dict.values())

answers = [i for i in dict if dict[i] == m]
sys.stdout.write(str(answers[0])) if len(answers) == 1 else sys.stdout.write("?")
