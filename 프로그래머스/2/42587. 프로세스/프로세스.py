from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, cur in enumerate(priorities):
        queue.append((cur, idx))

    while queue:
        process = queue.popleft()   # (2,0)

        if any(cur[0] > process[0] for cur in queue):
            queue.append(process)
        else:
            answer += 1
            if location == process[1]:
                return answer