# URL : https://atcoder.jp/contests/abc019/tasks/abc019_4
N = int(input())

# 頂点1から最も遠い点pを求める
p = 1
ma_dist = 0
for i in range(2, N+1):
    print("? {0} {1}".format(1, i), flush=True)
    dist = int(input())

    if dist > ma_dist:
        p = i
        ma_dist = dist


# 頂点pから最も遠い点qを求める
q = p
ma_dist = 0
for i in range(1, N+1):
    if i == p:
        continue
    print("? {0} {1}".format(p, i), flush=True)
    dist = int(input())

    if dist > ma_dist:
        q = i
        ma_dist = dist

print("! {}".format(ma_dist))