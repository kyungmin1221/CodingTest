from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])

    if target not in words:
        return answer

    while queue:
        now_begin, count = queue.popleft()
        if now_begin == target:
            answer = count
            break

        for word in words:
            step = 0
            for i in range(len(begin)):
                if now_begin[i] != word[i]:
                    step += 1

            if step == 1:
                queue.append([word, count + 1])

    return answer