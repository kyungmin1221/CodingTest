import sys


def solution(items):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, k + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][k]


n, k = map(int, sys.stdin.readline().strip().split())       # 4 7
items = [tuple(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
ans = solution(items)
print(ans)