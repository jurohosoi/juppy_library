# URL : https://atcoder.jp/contests/arc117/tasks/arc117_a

A, B = map(int, input().split())
ans = []

if A == B:
    for i in range(1, A+1):
        ans.append(i)
        ans.append(-i)
elif A > B:
    s = 0
    for i in range(1, A+1):
        ans.append(i)
        s += i
    for i in range(1, B):
        ans.append(-i)
        s -= i
    ans.append(-s)
else:
    s = 0
    for i in range(1, B+1):
        ans.append(-i)
        s -= i
    for i in range(1, A):
        ans.append(i)
        s += i
    ans.append(-s)

print(*ans)