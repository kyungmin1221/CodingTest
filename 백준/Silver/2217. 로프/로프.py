import sys

def solution(ropes):
    ropes.sort(reverse=True)
    max_weight = 0
    for i in range(len(ropes)):
        result = ropes[i] * (i + 1)
        max_weight = max(max_weight, result)

    return max_weight


n = int(sys.stdin.readline().strip())
ropes = []
for i in range(n):
    rope = int(sys.stdin.readline().strip())
    ropes.append(rope)

print(solution(ropes))