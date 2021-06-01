# URL : https://atcoder.jp/contests/abc203/tasks/abc203_b

N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    for j in range(1, K+1):
        ans += i*100 + j

print(ans)