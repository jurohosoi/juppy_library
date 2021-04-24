# URL : https://atcoder.jp/contests/abc199/tasks/abc199_d

class UnionFindTree:

    __all__ = ['_find_root', 'merge', 'same', 'size']

    def __init__(self, maxsize=10**6):    

        self._n = maxsize # number of nodes
        # parent_or_size[V] ...
        #  if negative : V is the root of the group
        #                and the value*(-1) is the size of the tree
        #  else        : the value is the parent node of V
        self._parent_or_size = [-1]*maxsize
    
    def _find_root(self, a):
        """Find the root of a"""

        pos = a
        children = []
        # Follow the path to the root
        while self._parent_or_size[pos] >= 0:
            children.append(pos)
            pos = self._parent_or_size[pos]
        else:
            root_pos = pos
        # Set the parent of child_pos to root_pos
        for child_pos in children:
            self._parent_or_size[child_pos] = root_pos
        return root_pos



    def merge(self, a, b):
        """Merge the group of a and the group of b"""

        root_a = self._find_root(a)
        root_b = self._find_root(b)
        if root_a == root_b:
            return True
        else:
            # The size of the group of b should be larger 
            if -self._parent_or_size[root_a] > -self._parent_or_size[root_b]:
                root_a, root_b = root_b, root_a
            # Merge the group of a with the group of b
            self._parent_or_size[root_b] += self._parent_or_size[root_a]
            self._parent_or_size[root_a] = root_b
            return False
    
    def same(self, a, b):
        """See if the group of a and the group of b are the same"""

        root_a = self._find_root(a)
        root_b = self._find_root(b)
        return root_a == root_b
    
    def size(self, a):
        """Return the size of the group of a"""
        
        root_a = self._find_root(a)
        return -self._parent_or_size[root_a]

N, M = map(int,input().split())
edge = [[] for _ in range(N)]
UF = UnionFindTree(maxsize = 30)

for _ in range(M):
    A, B = map(int,input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)
    UF.merge(A-1, B-1)

ans = 1
visited = [False]*N
for start in range(N):
    if visited[start]:
        continue

    cnt = 0 # startと連結な部分の塗り方の総数
    nxtcnt = 0 # startと連結している頂点の個数

    # i番目のbitが立っている -> i番目の色は、色を決定する際に隣接しているる頂点の色+1 (立っていない場合-1)
    for bitflag in range(1<<N):
        color = [3]*N # 色は0,1,2 (3は色未定)
        color[start] = 0
        
        # DFS
        queue = [start]
        flag = True
        while queue and flag:
            now = queue.pop()
            visited[now] = True
            for nxt in edge[now]:
                if color[nxt] == 3:
                    # 未訪問の場合bitflagによって色を決定する
                    if (bitflag >> nxt)&1:
                        color[nxt] = (color[now] + 1) % 3
                    else:
                        color[nxt] = (color[now] - 1) % 3
                    queue.append(nxt)
                else:
                    # 既に訪問済みで色がお互い決定している場合は同じ色かを確認する
                    if color[nxt] == color[now]:
                        flag = False
                        break
        if flag:
            cnt += 3
    # startと連結していない部分のbit 0 or 1 は全て同じ状態をダブルカウントしているので外す
    cnt >>= N - UF.size(start) + 1
    
    ans *= cnt
    
print(ans)