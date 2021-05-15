# URL : https://atcoder.jp/contests/abc201/tasks/abc201_a

A = list(map(int,input().split()))
A.sort()

if A[1] - A[0] == A[2] - A[1]:
    print("Yes")
else:
    print("No")