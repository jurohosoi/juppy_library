# URL : https://atcoder.jp/contests/abc064/tasks/abc064_c

N = int(input())
A = list(map(int,input().split()))

ans = 0
plus = 0
color = set()

for elt in A:
    if elt >= 3200:
        plus += 1
    else:
        c = elt//400
        if not c in color:
            ans += 1
            color.add(c)

if ans == 0:
    print(1, plus)
else:
    print(ans, ans + plus)
