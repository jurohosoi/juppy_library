# URL : https://atcoder.jp/contests/arc110/tasks/arc110_b
M = 3 * (10**10)
N = int(input())
T = list(input())

ans = 0

S = ['1', '1', '0'] * (N//3 +3)

for i in range(3):
    if T == S[i:i+N]:
        m = (i+N-1)%3
        startidx = i+N-1
        endidx = -1
        for j in range(3):
            if (M - 1 - j) % 3 == m:
                endidx = M - 1 - j
        ans += (endidx - startidx)//3 + 1

print(ans)