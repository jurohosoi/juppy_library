
NANO = 10**9
FULL = 12*60*60*NANO
T = int(input())

def check_axis(h, m, s, n):
    total_time = ((h*60 + m)*60 + s) * NANO + n
    x = total_time
    y = total_time%(FULL//12)*12
    z = total_time%(FULL//720)*720
    #print(total_time, x, y, z)
    return (x, y, z)

def find_time(x, y, z):
    sn = z//720
    s, n = divmod(sn, NANO)
    m = y // (720*NANO)
    h = x // (3600*NANO)
    #print(h, m, s, n)
    if check_axis(h, m, s, n) == (x, y, z):
        return h, m, s, n
    return -1, -1, -1, -1

for testcasenum in range(1, T+1):
    A, B, C = map(int, input().split())
    h, m, s, n = find_time(A, B, C)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue
    h, m, s, n = find_time(A, C, B)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue
    h, m, s, n = find_time(B, A, C)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue
    h, m, s, n = find_time(B, C, A)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue
    h, m, s, n = find_time(C, A, B)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue
    h, m, s, n = find_time(C, B, A)
    if h != -1:
        print("Case #{}: {} {} {} {}".format(testcasenum, h, m, s, n))
        continue

