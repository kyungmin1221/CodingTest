import sys


def solution(equation):
    parts_1 = equation.split('-')
    sum_1 = sum(map(int, parts_1[0].split('+')))

    sum_2 = 0
    for p1 in parts_1[1:]:
        sum_2 += sum(map(int, p1.split('+')))

    result = sum_1 - sum_2
    return result


equation = sys.stdin.readline().strip()
print(solution(equation))

