from collections import deque

def solution(prices):
    queue = deque()
    answer = []
    count = 0
    for i in prices:
        queue.append(i)

    while queue:
        cur = queue.popleft()       # 3
        for time in queue:
            if time >= cur:
                count += 1
                continue
            else:
                count += 1
                break
        answer.append(count)
        count = 0

    return answer