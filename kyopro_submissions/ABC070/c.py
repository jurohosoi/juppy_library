# URL : https://atcoder.jp/contests/abc070/tasks/abc070_c

import math

def lcm(x, y):
    return x*y/math.gcd(x, y)

N = int(input())
ans = 1

for i in range(N):
    T = int(input())
    ans = lcm(ans, T)

print(ans)