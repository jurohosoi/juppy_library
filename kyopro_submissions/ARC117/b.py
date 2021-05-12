# URL : https://atcoder.jp/contests/arc117/tasks/arc117_b

MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))
A.append(0)
N += 1

A.sort(reverse = True)


dp = [0]*N
dp[0] = 1

for i in range(1, N):
    sub = A[i-1] - A[i]
    dp[i] = dp[i-1] * (sub+1) % MOD

print(dp[-1])