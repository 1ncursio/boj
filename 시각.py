n = int(input())

h = 0
m = 0
s = 0

count = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                count += 1

# while h <= n:
#     if "3" in str(h) + str(m) + str(s):
#         count += 1
#     s += 1
#     if s == 60:
#         s = 0
#         m += 1
#     if m == 60:
#         m = 0
#         h += 1

print(count)
