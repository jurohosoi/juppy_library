# URL : https://atcoder.jp/contests/abc200/tasks/abc200_e

N, K = map(int, input().split())

M = [0]*(2*N+1)
Ma = [0]*(2*N+1)
for i in range(2, N+1):
    M[i] = i-1
    Ma[i] = Ma[i-1] + i-1
for i in range(N+1, 2*N+1):
    M[i] = N - (i - (N+1))
    Ma[i] = Ma[i-1] + N - (i - (N+1))

for total in range(3, 3*N+1):
    c = Ma[min(2*N, total-1)] - Ma[max(0, total-N-1)]

    if K > c:
        K -= c
    else:
        S = total
        break

for Ap in range(1, N+1):
    if S - Ap < 2 or S - Ap > 2*N:
        continue
    c = M[S - Ap]
    if K > c:
        K -= c
    else:
        A = Ap
        S -= A
        break

for Bp in range(1, N+1):
    if S - Bp < 1 or S - Bp > N:
        continue
    if K == 1:
        B = Bp
        C = S - B
        break
    else:
        K -= 1

print(A, B, C)
