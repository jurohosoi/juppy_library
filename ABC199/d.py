# URL : https://atcoder.jp/contests/abc199/tasks/abc199_d

N, M = map(int,input().split())
edge = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int,input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)

ans = 1
visited = [False]*N
for start in range(N):
    if visited[start]:
        continue

    cnt = 0 # startと連結な部分の塗り方の総数
    points = [] # startからDFSしたときに訪れる点

    # DFS
    queue = [start]
    while queue:
        now = queue.pop()
        points.append(now)
        visited[now] = True
        for nxt in edge[now]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append(nxt) 
    
    pN = len(points)
    points_idx = {elt : i for i, elt in enumerate(points)}

    # i番目のbitが立っている -> i番目の色は、色を決定する際に隣接しているる頂点の色+1 (立っていない場合-1)
    for bitflag in range(0, 1<<pN, 2):
        # startのbit 0 or 1 はダブルカウントになるので片方外す
        color = [3]*N # 色は0,1,2 (3は色未定)
        color[start] = 0
        
        # DFS
        queue = [start]
        flag = True
        while queue and flag:
            now = queue.pop()
            for nxt in edge[now]:
                if color[nxt] == 3:
                    # 未訪問の場合bitflagによって色を決定する
                    if (bitflag >> points_idx[nxt])&1:
                        color[nxt] = (color[now] + 1) % 3
                    else:
                        color[nxt] = (color[now] - 1) % 3
                    queue.append(nxt)
                else:
                    # 既に訪問済みで色がお互い決定している場合は同じ色かを確認する
                    if color[nxt] == color[now]:
                        flag = False
                        queue = []
                        break
        if flag:
            cnt += 3
    
    ans *= cnt
    
print(ans)