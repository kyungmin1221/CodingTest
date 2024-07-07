import sys
import heapq


def solution(dasom, candidate):
    count = 0

    if len(candidate) == 0:
        count = 0
        return count

    max_num = -heapq.heappop(candidate)  # (1) 7

    while dasom <= max_num:
        dasom += 1  # (1) 5->6
        max_num -= 1  # (1) 7->6
        heapq.heappush(candidate, -max_num)  # (1) [-7,-6]
        count += 1
        max_num = -heapq.heappop(candidate)

    return count


n = int(sys.stdin.readline().strip())
dasom = int(sys.stdin.readline().strip())

candidate = []  # 다른 후보자들
for i in range(n - 1):
    other = int(sys.stdin.readline().strip())
    heapq.heappush(candidate, -other)

# dasom = [5]
# candidate = [-7, -7]
print(solution(dasom, candidate))