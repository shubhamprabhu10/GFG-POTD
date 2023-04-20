'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def ladoos(self, root, home, k):
        # Your code goes here
#        Nested function concept with recursion 
        def _precompute(nd, par):
            nonlocal start
            nd.parent = par
            if nd.left: _precompute(nd.left, nd)
            if nd.right: _precompute(nd.right, nd)
            if nd.data == home: start = nd
        def _solve(nd, dis, prev):
            if dis<0: return 0
            ans = nd.data
            for nex in (nd.parent, nd.left, nd.right):
                if nex is prev or nex is None: continue
                ans += _solve(nex, dis-1, nd)
            return ans
        
        start = None
        _precompute(root, None)
        ans = _solve(start, k, None)
        return ans
