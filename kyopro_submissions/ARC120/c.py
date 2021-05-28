
from collections import deque
import heapq

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
B = list(map(int, input().split()))

zero_val = dict()
for i in range(N):
    if A[i]+i in zero_val:
        zero_val[A[i] + i].append(i)
    else:
        zero_val[A[i]+ i] = deque([i])

BIT = BinaryIndexedTree()

ans = 0
for i in range(N):
    bval = B[i] + i
    if not bval in zero_val:
        ans = -1
        break

    if len(zero_val[bval]) == 0:
        ans = -1
        break
    popidx = zero_val[bval].popleft()
    fr_idx = popidx + BIT.sumrange(lo=popidx, hi=N-1)

    ans += fr_idx - i
    BIT.add(popidx, 1)

print(ans)
