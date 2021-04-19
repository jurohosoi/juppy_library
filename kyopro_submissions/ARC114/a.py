# URL : https://atcoder.jp/contests/arc114/tasks/arc114_a

import math

MAX_X = 50

N = int(input())
X = list(map(int, input().split()))

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

prime_list = primes(MAX_X)
PN = len(prime_list)
ans = -1

for bitflag in range(1<<PN):
    flag = True # 互いに素でない条件を満たすか

    tmp_ans = 1 # 解候補 : bitflagの立っているindexの素数の積
    for bitidx in range(PN):
        if (bitflag>>bitidx)&1 == 1:
            tmp_ans *= prime_list[bitidx]
    
    for X_elt in X:
        if math.gcd(X_elt, tmp_ans) == 1:
            flag = False
            break
    
    if flag:
        if ans == -1:
            ans = tmp_ans
        else:
            ans = min(ans, tmp_ans)

print(ans)