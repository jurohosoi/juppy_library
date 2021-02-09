class SegmentTree:

    def __init__(self, maxsize=10**6, idetify_elt=-10**9, func=max):
        assert (func(idetify_elt, idetify_elt) == idetify_elt)
        self.n = maxsize
        self.seg_length_half = 2**(maxsize-1).bit_length()
        self.idetify_elt = idetify_elt
        self.seg = [idetify_elt]*(2*self.seg_length_half)
        self.func = func

    def setval(self, set_list):
        assert (len(set_list) == self.n)
        # Set value at the bottom
        for i in range(self.n):
            self.seg[i+self.seg_length_half-1] = set_list[i]    
        # Build value
        for i in range(self.seg_length_half-2, -1, -1):
            self.seg[i] = self.func(self.seg[2*i+1], self.seg[2*i+2])
    
    def update(self, k, x):
        """ A[k] = x """
        pos = k + self.seg_length_half - 1
        # Set value at k-th
        self.seg[pos] = x
        # Build value
        while pos:
            pos = (pos-1)//2
            self.seg[pos] = self.func(self.seg[pos*2+1], self.seg[pos*2+2])
    
    def query(self, left, right):
        """func(A[left], ... , A[right]) """
        
        if right <= left:
            return self.idetify_elt
        
        func_value = self.idetify_elt
        leftpos = left + self.seg_length_half - 1
        rightpos = right + self.seg_length_half - 2


        while leftpos < rightpos:
            if leftpos&1 == 0:
                func_value = self.func(func_value, self.seg[leftpos])
            if rightpos&1 == 1:
                func_value = self.func(func_value, self.seg[rightpos])
            leftpos = leftpos//2
            rightpos = (rightpos-1)//2

        return func_value

        

        
