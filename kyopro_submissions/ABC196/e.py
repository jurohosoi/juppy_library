# URL : https://atcoder.jp/contests/abc196/tasks/abc196_e

def f(x, miX, miY, maY):
    if x <= miX:
        return miY
    if x >= miX + (maY - miY):
        return maY
    return miY + (x - miX) 

N = int(input())
miX, miY, maY = -10**16, -10**16, 10**16

for _ in range(N):
    A, T = map(int, input().split())
    if T == 1:
        miY += A
        maY += A
    elif T == 2:
        if A >= maY:
            miY = A
            maY = A
        elif miY < A < maY:
            miX += A - miY
            miY = A
        elif A <= miY:
            continue       
    elif T == 3:
        if A >= maY:
            continue
        elif miY < A < maY:
            maY = A
        elif A <= miY:
            miY = A
            maY = A

Q = int(input())
X = list(map(int, input().split()))
for xelt in X:
    print(f(xelt, miX, miY, maY))