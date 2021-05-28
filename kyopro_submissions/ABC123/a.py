# URL : https://atcoder.jp/contests/abc123/tasks/abc123_a

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

h = [a, b, c, d, e]
h.sort()

sub = h[-1] - h[0]

if sub <= k:
    print("Yay!")
else:
    print(":(")