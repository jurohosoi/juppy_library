# URL : https://atcoder.jp/contests/abc199/tasks/abc199_c

N = int(input())
S = list(input())
Q = int(input())
N_2 = N*2

rev = -1
for _ in range(Q):
    T, A, B = map(int,input().split())
    if T == 1:
        if rev > 0:
            A, B = (A+N-1)%N_2, (B+N-1)%N_2
        else:
            A, B = A-1, B-1
        S[A], S[B] = S[B], S[A]
    elif T == 2:
        rev *= -1
if rev > 0:
    for i in range(N):
        S[i], S[i+N] = S[i+N], S[i]

print(''.join(S))