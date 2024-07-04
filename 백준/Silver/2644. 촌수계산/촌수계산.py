import sys


def dfs(num1):
    global count, result
    visited[num1] = 1

    if num1 == people2:
        result = count
        return

    for child in graph[num1]:
        if visited[child] == 0:
            count += 1
            visited[child] = 1
            dfs(child)
            count -= 1


n = int(sys.stdin.readline().strip())  # 전체 사람의 수
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

people1, people2 = map(int, sys.stdin.readline().strip().split())  # 촌수 계산할 사라들
m = int(sys.stdin.readline().strip())  # 관계의 개수
count = 0
result = 0
for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(people1)    # result 계산 완료
if result:
    print(result)
else:
    print(-1)


