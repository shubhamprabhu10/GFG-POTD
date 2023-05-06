from functools import lru_cache
class Solution:
    def makeChanges(self, N : int, k : int, target : int, coins : List[int]) -> bool:
        # code here
        @lru_cache(None)
        def recur(amt,k):
            if not k:
                return amt==0
            res=False
            for c in coins:
                if c<=amt:
                    res=res or recur(amt-c,k-1)
            return res
        return recur(target,k)
