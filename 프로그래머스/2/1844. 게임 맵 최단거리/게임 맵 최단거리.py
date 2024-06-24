from collections import deque

def solution(maps):
    n = len(maps)   # 세로의 길이
    m = len(maps[0])    # 가로의 길이
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * m for _ in range(len(maps))]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]