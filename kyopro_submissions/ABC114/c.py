# URL : https://atcoder.jp/contests/abc114/tasks/abc114_c

N = int(input())
res = 0
old = {0}
dg = 1
while True:
    flag = True
    new = set()
    for elt in old:
        for nxt in (3, 5, 7):
            if nxt*dg + elt <= N:
                new.add(nxt*dg + elt)
                flag = False
                if len(set(list(str(nxt*dg + elt)))) == 3:
                    res += 1
    dg *= 10
    old = new
    if flag:
        break
print(res)    