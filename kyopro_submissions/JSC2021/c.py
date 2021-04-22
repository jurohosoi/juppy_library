# URL : https://atcoder.jp/contests/jsc2021/tasks/jsc2021_c

A, B = map(int, input().split())

ans = 1
for g in range(1, B+1):
    Ag = ((A-1)//g + 1) * g
    Bg = (B//g) * g
    if Ag < Bg:
        ans = g

print(ans)