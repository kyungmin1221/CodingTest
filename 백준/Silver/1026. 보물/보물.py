import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
a.sort(reverse=True)
b.sort()

for i in range(n):
    answer += a[i]*b[i]

print(answer)

