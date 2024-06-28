import sys
sys.setrecursionlimit(10 ** 6)


def tree(node):
    for idx in graph[node]:
        if not visited[idx]:
            visited[idx] = True
            answer[idx] = node
            tree(idx)


n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)  # 리스트 크기를 n + 1로 초기화

for i in range(1, n):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visited[1] = True
tree(1)

for i in range(2, n + 1):
    print(answer[i])
