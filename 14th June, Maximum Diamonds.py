#User function Template for python3
import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        pq = []
        for num in A:
            heapq.heappush(pq, -num)  # Using a min-heap with negated values            
        res = 0        
        while K > 0:
            m = -heapq.heappop(pq)
            res += m
            heapq.heappush(pq, -(m // 2))
            K -= 1        
        return res
