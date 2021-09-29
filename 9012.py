T = int(input())

Parens = [input() for _ in range(T)]

for P in Parens:
    stack = []
    flag = True
    for p in P:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if len(stack) > 0 and stack[-1] == "(":
                del stack[-1]
            else:
                flag = False
                break
    print("YES") if len(stack) == 0 and flag else print("NO")
