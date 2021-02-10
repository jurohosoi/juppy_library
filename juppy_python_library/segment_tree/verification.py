import sys

class SegmentTree:

    __all__ = ['setval', 'pointupdate', 'segquery', 'segsearch_right', 'pointgetval']

    def __init__(self, n=10**6, idetify_elt=-10**9, func=max):
        assert (func(idetify_elt, idetify_elt) == idetify_elt)
        self.n = n
        self.seg_length_half = 2**(n-1).bit_length()
        self.idetify_elt = idetify_elt
        self.seg = [idetify_elt]*(2*self.seg_length_half)
        self.func = func

    def setval(self, x_list):
        '''Set value : A = x_list'''
        assert (len(x_list) == self.n)
        # Set value at the bottom
        for i in range(self.n):
            self.seg[i+self.seg_length_half-1] = x_list[i]    
        # Build value
        for i in range(self.seg_length_half-2, -1, -1):
            self.seg[i] = self.func(self.seg[2*i+1], self.seg[2*i+2])
    
    def pointupdate(self, k, x):
        '''Update : A[k] = x '''
        pos = k + self.seg_length_half - 1
        # Set value at k-th
        self.seg[pos] = x
        # Build bottom-up
        while pos:
            pos = (pos-1)//2
            self.seg[pos] = self.func(self.seg[pos*2+1], self.seg[pos*2+2])
    
    def pointgetval(self, k):
        ''' Return A[k] '''
        return self.seg[k + self.seg_length_half - 1]

    def segquery(self, left, right):
        ''' Return func(A[left], ... , A[right-1]) '''
        # if not left < right
        if right <= left:
            return self.idetify_elt
        
        func_value = self.idetify_elt
        leftpos = left + self.seg_length_half - 1 # leftmost segment
        rightpos = right + self.seg_length_half - 2 # rightmost segment

        while leftpos < rightpos-1:
            if leftpos&1 == 0:
                # if leftpos is right-child
                func_value = self.func(func_value, self.seg[leftpos])
            if rightpos&1 == 1:
                # if rightpos is leftchild
                func_value = self.func(func_value, self.seg[rightpos])
                rightpos -= 1
            # move up
            leftpos = leftpos//2
            rightpos = (rightpos-1)//2
        
        func_value = self.func(func_value, self.seg[leftpos])
        if leftpos != rightpos:
            func_value = self.func(func_value, self.seg[rightpos])
        return func_value

    def segsearch_right(self, condfunc, left=0):
        ''' Return min_i satisfying condfunc( func( A[left], ... , A[i])) 
        if impossible : return n
        '''
        # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
        if not condfunc(self.segquery(left, self.n)):
            return self.n
        
        # possible
        func_value = self.idetify_elt
        rightpos = left + self.seg_length_half - 1
        while True: 
            # while rightpos is the left-child, move bottom-up
            while rightpos&1 == 1:
                rightpos //= 2
            # try
            up_value_trial = self.func(func_value, self.seg[rightpos])
            if not condfunc(up_value_trial):
                # move up and right
                func_value = up_value_trial
                rightpos = (rightpos-1)//2 + 1
            else:
                # move top-down
                while rightpos < self.seg_length_half-1:
                    down_value_trial = self.func(func_value, self.seg[rightpos*2 + 1])
                    if condfunc(down_value_trial):
                        # move left-child
                        rightpos = rightpos*2 + 1
                    else:
                        # move right-child
                        func_value = down_value_trial
                        rightpos = rightpos*2 + 2
                return rightpos - self.seg_length_half + 1


def solve():
    # Input
    arg = list(map(int, sys.stdin.buffer.read().split()))
    N, Q = arg[0], arg[1]
    
    SegTree = SegmentTree(n=N, idetify_elt=0, func=max)
    SegTree.setval(arg[2:N+2])
    output = []
    
    # Query
    for i in range(0, Q):
        T, p, q = arg[N+2 + 3*i], arg[N+2 + 3*i+1], arg[N+2 + 3*i+2]
        if T == 1:
            SegTree.pointupdate(p-1, q)
        elif T == 2:
            output.append(SegTree.segquery(p-1, q))
        elif T == 3:
            output.append(SegTree.segsearch_right(left=p-1, condfunc = lambda x: x >= q) + 1)
    
    # Output
    print(*output)

if __name__ == '__main__':
    main()