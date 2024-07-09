import sys


t = int(sys.stdin.readline().strip())
for i in range(t):
    result = {}
    count = 1
    n = int(sys.stdin.readline().strip())
    for c in range(n):
        cloth, kind = sys.stdin.readline().strip().split()
        if kind in result:
            result[kind] += 1
        else:
            result[kind] = 1

    for ans in result:
        count *= (result[ans] + 1)

    print(count-1)