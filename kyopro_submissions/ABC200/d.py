# URL : https://atcoder.jp/contests/abc200/tasks/abc200_d

N = int(input())
A = list(map(int,input().split()))

d = dict()

x = -1
y = -1

for i in range(1, min(300, 1<<N)):
    s = 0
    for j in range(N):
        if (i >> j) & 1:
            s += A[j]
    s = s%200
    if s in d:
        x = d[s]
        y = i
        break
    else:
        d[s] = i


if x == -1:
    print("No")
else:
    print("Yes")
    ansx = []
    for j in range(N):
        if (x >> j) & 1:
            ansx.append(j+1)
    print(len(ansx), end = ' ')
    print(*ansx)

    ansy = []
    for j in range(N):
        if (y >> j) & 1:
            ansy.append(j+1)
    print(len(ansy), end = ' ')
    print(*ansy)