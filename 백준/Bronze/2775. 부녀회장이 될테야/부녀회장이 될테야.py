import sys


def association(k, n):
    floor = []
    for i in range(1, n + 1):  # 1 2 3
        floor.append(i)  # [1,2,3]

    for _ in range(k):
        for i in range(1, n):  # 1 2
            floor[i] += floor[i - 1]

    return floor[-1]


answers = []
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    answers.append(association(k, n))

for ans in answers:
    print(ans)