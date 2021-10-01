"""
Flag가 False = 삭제안함, 카운트 o
Flag가 True = 삭제됨, 카운트 x

count가 K와 같을 때에 Flag를 True로 바꾼다

7 3
예제 출력 1
<3, 6, 2, 7, 5, 1, 4>
"""
N, K = map(int, input().split())

List = [i + 1 for i in range(N)]

Answers = []

i = 0

for _ in range(N):
    i += K - 1
    if i >= len(List):
        i %= len(List)

    Answers.append(List.pop(i))

print("<", ", ".join(list(map(str, Answers))), ">", sep="")
