# URL : https://atcoder.jp/contests/arc120/tasks/arc120_b

MOD = 998244353
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = 1

for i in range(H):
    x, y = i, 0
    mark = '.'
    dotflag = True
    while x >= 0 and y < W:
        if S[x][y] != '.':
            dotflag = False
            if mark == '.':
                mark = S[x][y]
            elif S[x][y] != mark:
                ans = 0
                break
        x -= 1
        y += 1
    if ans == 0:
        break
    if dotflag:
        ans = ans*2%MOD

for j in range(1, W):
    x, y = H-1, j
    mark = '.'
    dotflag = True
    while x >= 0 and y < W:
        if S[x][y] != '.':
            dotflag = False
            if mark == '.':
                mark = S[x][y]
            elif S[x][y] != mark:
                ans = 0
                break
        x -= 1
        y += 1
    if ans == 0:
        break
    if dotflag:
        ans = ans*2%MOD
print(ans)
    