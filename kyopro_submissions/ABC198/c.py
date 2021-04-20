# URL : https://atcoder.jp/contests/abc198/tasks/abc198_c

R, X, Y = map(int, input().split())

K2 = (X**2 + Y**2) // (R**2)
K1 = int(K2**0.5)

if K1 == 0:
    K1 = 1

if (X**2 + Y**2) % (R**2) == 0:
    if K1**2 == K2:
        print(K1)
    else:
        print(K1 + 1)
else:
    print(K1 + 1)