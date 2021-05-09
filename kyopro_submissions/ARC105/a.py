A = list(map(int,input().split()))

for i in range(1<<4):
    s = 0
    t = 0
    for j in range(4):
        if (i>>j) & 1:
            s += A[j]
        else:
            t += A[j]
    if s == t:
        print("Yes")
        exit()

print("No")