from sys import stdin, stdout
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(graph, y, x, visited):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = True
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if ny < 0 or ny >= len(graph) or nx < 0 or nx >= len(graph[0]):
                continue
            if not visited[ny][nx] and graph[ny][nx] == 1:
                queue.append([ny, nx])
                visited[ny][nx] = True


T = int(input())

Ms, Ns, Ks, graphs, visiteds = [], [], [], [], []


for _ in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, stdin.readline().rstrip().split())
        graph[Y][X] = 1
    Ms.append(M)
    Ns.append(N)
    Ks.append(K)
    graphs.append(graph)
    visiteds.append(visited)

for M, N, K, graph, visited in zip(Ms, Ns, Ks, graphs, visiteds):
    count = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(graph, i, j, visited)
                count += 1

    stdout.write(str(count) + "\n")
