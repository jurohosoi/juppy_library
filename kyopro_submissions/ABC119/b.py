# URL : https://atcoder.jp/contests/abc119/tasks/abc119_b

N = int(input())

ans = 0
for _ in range(N):
    x, u = map(str, input().split())
    x_float = float(x)
    if u == 'JPY':
        ans += x_float
    else:
        ans += x_float * 380000.0

print(ans)