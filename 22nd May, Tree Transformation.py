from typing import List
class Solution:
    def solve(self, N : int, p : List[int]) -> int:
        nodes = [0]*N        
        for i in range(1, N):
            nodes[p[i]] += 1
            nodes[i] += 1   
        leaf_cnt = sum(1 for n in nodes if n == 1)
        return max(N-leaf_cnt-1, 0)
