import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort(reverse=True)
first, second = data[0], data[1]

result = 0

"""
m >= k
m번 동안 list 중 최댓값을 k번만큼 더하고
그 다음은 그 인덱스를 제외한 값 중 최댓값을 k번만큼 더하기를 반복
"""
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
