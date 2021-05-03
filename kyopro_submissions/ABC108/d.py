# URL : https://atcoder.jp/contests/abc108/tasks/arc102_b

L = int(input())
N = 20
edge = []


edge.append((1, 2, 0))
edge.append((1, 2, 1))
edge.append((1, 2, 2))
edge.append((1, 2, 3))

for i in range(2, 19):
    edge.append((i, i+1, 0))
    edge.append((i, i+1, 2**i))

add = 0
while L:
    k = 0
    while 2**(k+1) <= L:
        k += 1
    if L >= 4:
        edge.append((k, 20, add))
        add += 2**k
        L -= 2**k
    else:
        for plus in range(L):
            edge.append((1, 20, add + plus))
        L = 0

print(N, len(edge))
for u, v, w in edge:
    print(u, v, w)