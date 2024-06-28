import sys
from collections import deque

# 상하좌우 탐색을 위한 전역변수 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = 0
house_map = []  # 원본 배열
visited = []    # 방문 배열


def house(x, y):
    global house_map, visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1  # 현재 단지의 집 수

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    house_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    counts = []

    for i in range(N):
        for j in range(N):
            if house_map[i][j] == 1 and not visited[i][j]:
                counts.append(house(i, j))

    print(len(counts))
    counts.sort()
    for count in counts:
        print(count)
