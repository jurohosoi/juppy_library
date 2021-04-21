# URL : https://atcoder.jp/contests/arc114/tasks/arc114_b

MOD = 998244353
N = int(input())
f = [0] + list(map(int, input().split()))

# 有効な輪の個数
circle_cnt = 0
# 入力辺の個数
nonused = [True]*(N+1)

for i in range(1, N+1):
    if nonused[i]:
        start = i
        now = start
        visited = set()
        while True:
            visited.add(now)
            nxt = f[now]

            # 訪れた先が既に有効輪
            if not nonused[nxt]:
                nonused[start] = False
                break
            
            # 有効に1周した
            if nxt in visited:
                if nxt == start:
                    circle_cnt += 1
                    for point in visited:
                        nonused[point] = False    
                nonused[start] = False
                break
            now = nxt

print((pow(2, circle_cnt, MOD) - 1) %MOD)