A, B, K = map(int, input().split())

fact = [1]
for i in range(63):
    fact.append(fact[-1]*(i+1))
def nCk(n, k):
    return fact[n] // (fact[n-k] * fact[k])

N = A+B
ans = []

for i in range(N):
    if A == 0:
        ans.append('b')
        B -= 1
    else:
        tmp = nCk(A+B-1, B)
        if K <= tmp:
            ans.append('a')
            A -= 1
        else:
            K -= tmp
            ans.append('b')
            B -= 1

print(''.join(ans))