# URL : https://atcoder.jp/contests/abc034/tasks/abc034_c

MOD = 10**9 + 7
MAX_N = 10**6
W, H = map(int, input().split())

# Comb(W+H, H) mod 10**9 + 7

fact = [0]*MAX_N
fact_inv = [0]*MAX_N

fact[1] = 1
for i in range(2, MAX_N):
    fact[i] = fact[i-1] * i % MOD

fact_inv[MAX_N-1] = pow(fact[MAX_N-1], MOD-2, MOD)
for i in range(MAX_N-2, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % MOD
ans = fact[W+H-2] * fact_inv[W-1] * fact_inv[H-1] % MOD
print(ans)