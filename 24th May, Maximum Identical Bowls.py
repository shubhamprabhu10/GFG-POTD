from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        sum = 0
        for i in arr:
            sum+=i
        for i in range(N,0,-1):
            if sum%i==0:
                return i
