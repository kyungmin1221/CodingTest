import sys

sys.setrecursionlimit(10 ** 6)

memo = {}


def fibo(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


n = int(sys.stdin.readline().strip())
print(fibo(n))
