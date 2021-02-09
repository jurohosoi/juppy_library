class BinaryIndexedTree:

    __all__ = ['add', 'sumrange', 'lower_left']

    def __init__(self, maxsize=10**6):
        assert (maxsize > 0)

        self.n = maxsize+1
        self.bitdata = [0]*(maxsize+1)
    
    def add(self, i, x):
        """Add x to A[i] (A[i] += x) """
        assert(0 <= i < self.n)

        pos = i+1
        while pos < self.n:
            self.bitdata[pos] += x
            pos += pos&(-pos)
    
    def running_total(self, i):
        """ Return sum of (A[0] ... A[i]) """
        assert (-1<= i < self.n)

        if i == -1:
            return 0
        returnval = 0
        pos = i+1
        while pos:
            returnval += self.bitdata[pos]
            pos -= pos & (-pos)
        return returnval

    def sumrange(self, lo=0, hi=None):
        """ Return sum of (A[lo] ... A[hi]) """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = self.n

        return self.running_total(hi) - self.running_total(lo-1)

    def lower_left(self, total):
        """ Return min-index satisfying {sum(A0 ~ Ai) >= total} 
        only if Ai >= 0 (for all i)
        """
        if total < 0:
            return -1
        pos = 0
        k = 1<<(self.n.bit_length()-1)
        while k > 0:
            if pos+k < self.n and self.bitdata[pos+k] < total:
                total -= self.bitdata[pos+k]
                pos += k
            k //= 2
        return pos