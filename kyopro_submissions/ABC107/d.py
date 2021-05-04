# URL : https://atcoder.jp/contests/abc107/tasks/arc101_b

import bisect

class BinaryIndexedTree:

    __all__ = ['add', 'sumrange', 'lower_left']

    def __init__(self, maxsize=10**6):

        self._n = maxsize+1
        self._bitdata = [0]*(maxsize+1)
    
    def add(self, i, x):
        """Add x to A[i] (A[i] += x) """

        pos = i+1
        while pos < self._n:
            self._bitdata[pos] += x
            pos += pos&(-pos)
    
    def running_total(self, i):
        """ Return sum of (A[0] ... A[i]) """

        if i == -1:
            return 0
        returnval = 0
        pos = i+1
        while pos:
            returnval += self._bitdata[pos]
            pos -= pos & (-pos)
        return returnval

    def sumrange(self, lo=0, hi=None):
        """ Return sum of (A[lo] ... A[hi]) """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = self._n

        return self.running_total(hi) - self.running_total(lo-1)

    def lower_left(self, total):
        """ Return min-index satisfying {sum(A0 ~ Ai) >= total} 
        only if Ai >= 0 (for all i)
        """
        if total < 0:
            return -1
        pos = 0
        k = 1<<(self._n.bit_length()-1)
        while k > 0:
            if pos+k < self._n and self._bitdata[pos+k] < total:
                total -= self._bitdata[pos+k]
                pos += k
            k //= 2
        return pos

N = int(input())
A = list(map(int, input().split()))

# 中央値がm以下の個数が
ok = 10**9
ng = 0
while ok - ng > 1:
    m = (ok + ng) // 2

    # 1 or -1 累積和
    S = [0]*(N+1)
    for i in range(N):
        if A[i] <= m:
            S[i+1] = S[i] + 1
        else:
            S[i+1] = S[i] - 1
    
    # Sの転倒数
    S_sorted = sorted(S)
    S_compression = []
    for i in range(N+1):
        S_compression.append(bisect.bisect_left(S_sorted, S[i]) + 1)
    BIT = BinaryIndexedTree(maxsize = N+1)
    cnt = 0
    for i in range(N+1):
        val = S_compression[i]
        cnt += BIT.sumrange(hi = val - 1)
        BIT.add(val, 1)
    
    if cnt > N*(N+1)//4:
        ok = m
    else:
        ng = m

print(ok)