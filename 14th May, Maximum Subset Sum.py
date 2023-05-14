from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        # code here
        take=n_take=0
        for i in A:
            take,n_take=max(i+take,n_take),i+take
        return max(take,n_take)
