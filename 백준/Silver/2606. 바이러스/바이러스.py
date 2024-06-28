import sys


def computers(com):
    global answer

    visited[com] = True

    for i in graph[com]:
        if not visited[i]:
            answer += 1
            computers(i)

    return answer


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0
for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

print(computers(1))