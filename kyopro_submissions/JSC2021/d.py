# URL : https://atcoder.jp/contests/jsc2021/tasks/jsc2021_d

MOD = 10**9 + 7
N, P = map(int, input().split())

ans = pow(P-2, N-1, MOD) * (P-1) % MOD
print(ans)