# URL : https://atcoder.jp/contests/arc116/tasks/arc116_b

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
mi = 0

for e in A:
    mi = (mi*2 + e)%MOD
    ans = (ans + mi*e)%MOD

print(ans)