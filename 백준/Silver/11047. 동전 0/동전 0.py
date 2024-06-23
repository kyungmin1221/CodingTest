import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = []

for i in range(0, n):
    coin = int(sys.stdin.readline().strip())
    coin_list.append(coin)

coin_list.sort()
# [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
count = 0
cost = k
for i in range(n-1, -1, -1):
    if (cost // coin_list[i]) > 0:
        count += (cost // coin_list[i])
        cost = (cost % coin_list[i])   # 200

print(count)