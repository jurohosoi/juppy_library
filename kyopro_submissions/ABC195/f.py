# URL : https://atcoder.jp/contests/abc195/tasks/abc195_f

def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

ps = primes(75)
A, B = map(int, input().split())
N = B-A+1
M = len(ps)

# anti-MLE DP
dp = [[0]*(1<<M) for _ in range(2)]
dp[0][0] = 1

for i in range(1, N+1):
    num = A + i - 1
    numbit = 0
    for j in range(M):
        if num%ps[j] == 0:
            numbit |= 1<<j
    for j in range(1<<M):
        if (j^numbit) == (j|numbit):
            dp[i%2][j^numbit] = dp[(i+1)%2][j^numbit] + dp[(i+1)%2][j]     
        else:
            dp[i%2][j^numbit] = dp[(i+1)%2][j^numbit]

    #print(numbit, dp[i][:10])
print(sum(dp[N%2]))