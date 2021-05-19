# # URL : https://atcoder.jp/contests/arc119/tasks/arc119_c

N = int(input())
A = list(map(int, input().split()))
B = [0]*N

dB = dict()
dB[0] = 1
ans = 0

for i in range(N):
    if i%2:
        B[i] = B[i-1] + A[i]
    else:
        B[i] = B[i-1] - A[i]
    if B[i] in dB:
        ans += dB[B[i]]
        dB[B[i]] += 1
    else:
        dB[B[i]] = 1

print(ans)
