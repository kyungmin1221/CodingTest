import sys

MOD = 1000000
P = MOD // 10 * 15
fibo = [0] * P
fibo[0], fibo[1] = 0, 1

def compute_fibo_mod(n):
    for i in range(2, P):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % MOD
    return fibo[n % P]

n = int(sys.stdin.readline().strip())
print(compute_fibo_mod(n))
