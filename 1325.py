from sys import stdin, stdout
from collections import deque

"""
list: 각 컴퓨터번호 별 해킹할 수 있는 컴퓨터 수
"""

N, M = map(int, stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
list = []

for _ in range(M):
    v1, v2 = map(int, stdin.readline().rstrip().split())
    graph[v2].append(v1)

print(graph)


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for i in range(1, N + 1):
    bfs(graph, i, visited)
    list.append(visited.count(True))
    visited = [False] * (N + 1)

max_val = max(list)
[stdout.write(str(index + 1) + " ") for index, i in enumerate(list) if i == max_val]
