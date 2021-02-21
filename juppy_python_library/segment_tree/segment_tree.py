class SegmentTree:

    __all__ = ['setval', 'pointupdate', 'segquery', 'segsearch_right', 'pointgetval']

    def __init__(self, n=10**6, idetify_elt=-10**9, func=max):

        self._n = n
        self._seg_length_half = 2**(n-1).bit_length()
        self._idetify_elt = idetify_elt
        self._seg = [idetify_elt]*(2*self._seg_length_half)
        self._func = func

    def setval(self, x_list):
        """Set value : A = x_list"""

        # Set value at the bottom
        for i in range(self._n):
            self._seg[i+self._seg_length_half-1] = x_list[i]    
        # Build value
        for i in range(self._seg_length_half-2, -1, -1):
            self._seg[i] = self._func(self._seg[2*i+1], self._seg[2*i+2])
    
    def pointupdate(self, k, x):
        """Update : A[k] = x """
        pos = k + self._seg_length_half - 1
        # Set value at k-th
        self._seg[pos] = x
        # Build bottom-up
        while pos:
            pos = (pos-1)//2
            self._seg[pos] = self._func(self._seg[pos*2+1], self._seg[pos*2+2])
    
    def pointgetval(self, k):
        """ Return A[k] """
        return self._seg[k + self._seg_length_half - 1]

    def segquery(self, left, right):
        """ Return func(A[left], ... , A[right-1]) """
        # if not left < right
        if right <= left:
            return self._idetify_elt
        
        func_value = self._idetify_elt
        leftpos = left + self._seg_length_half - 1 # leftmost segment
        rightpos = right + self._seg_length_half - 2 # rightmost segment

        while leftpos < rightpos-1:
            if leftpos&1 == 0:
                # if leftpos is right-child
                func_value = self._func(func_value, self._seg[leftpos])
            if rightpos&1 == 1:
                # if rightpos is leftchild
                func_value = self._func(func_value, self._seg[rightpos])
                rightpos -= 1
            # move up
            leftpos = leftpos//2
            rightpos = (rightpos-1)//2
        
        func_value = self._func(func_value, self._seg[leftpos])
        if leftpos != rightpos:
            func_value = self._func(func_value, self._seg[rightpos])
        return func_value

    def segsearch_right(self, condfunc, left=0):
        """ Return min_i satisfying condfunc( func( A[left], ... , A[i])) 
        if impossible : return n
        """
        # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
        if not condfunc(self._segquery(left, self._n)):
            return self._n
        
        # possible
        func_value = self._idetify_elt
        rightpos = left + self._seg_length_half - 1
        while True: 
            # while rightpos is the left-child, move bottom-up
            while rightpos&1 == 1:
                rightpos //= 2
            # try
            up_value_trial = self._func(func_value, self._seg[rightpos])
            if not condfunc(up_value_trial):
                # move up and right
                func_value = up_value_trial
                rightpos = (rightpos-1)//2 + 1
            else:
                # move top-down
                while rightpos < self._seg_length_half-1:
                    down_value_trial = self._func(func_value, self._seg[rightpos*2 + 1])
                    if condfunc(down_value_trial):
                        # move left-child
                        rightpos = rightpos*2 + 1
                    else:
                        # move right-child
                        func_value = down_value_trial
                        rightpos = rightpos*2 + 2
                return rightpos - self._seg_length_half + 1
