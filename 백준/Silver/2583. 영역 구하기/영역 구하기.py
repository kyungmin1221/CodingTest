import sys
from collections import deque

def solution(y, x):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    area = 1
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny <n and visited[ny][nx] == 0 and arr[ny][nx] == 0:
                visited[ny][nx] = 1
                arr[ny][nx] = 1
                area += 1
                queue.append((ny, nx))

    return area


n, m, k = map(int, sys.stdin.readline().strip().split())    # n:세로 m:가로 k:그릴 삼각형
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
count = 0
result = []
for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for x in range(x1, x2):      # 0 - 4
        for y in range(y1, y2):     #  2 - 4
            arr[y][x] = 1


for y in range(n):      # 5
    for x in range(m):  # 7
        if arr[y][x] == 0 and visited[y][x] == 0:
            count += 1
            ans = solution(y, x)
            result.append(ans)

result.sort()
print(count)
print(*result)