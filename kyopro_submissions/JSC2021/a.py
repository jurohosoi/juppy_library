# URL : https://atcoder.jp/contests/jsc2021/tasks/jsc2021_a

X, Y, Z = map(int, input().split())
YZ = Y*Z

hi = 10**6
lo = 0
while hi - lo > 1:
    mid = (hi+lo)//2
    if mid*X < YZ:
        lo = mid
    else:
        hi = mid
print(lo)