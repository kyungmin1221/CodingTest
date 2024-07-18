import sys

def solution(visitor, x):
    result = []
    count = 1
    current_value = sum(visitor[:x])   # current = 5
    max_value = current_value           #  max = 5
    for i in range(x, len(visitor)):    # 2 - 5
        current_value -= visitor[i - x]
        current_value += visitor[i]

        if max_value < current_value:
            max_value = current_value
            count = 1
        elif max_value == current_value:
            count += 1

    if max_value == 0:
        result.append("SAD")
    else:
        result.append(max_value)
        result.append(count)

    return result


n, x = map(int, sys.stdin.readline().strip().split())
visitor = list(map(int, sys.stdin.readline().strip().split()))
answer = solution(visitor, x)
for ans in answer:
    print(ans)