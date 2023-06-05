class Solution:
    def minDiff(self,root, K):
        if root ==None :
            return float("inf")
        return min(abs(K-root.data),self.minDiff(root.left,K),self.minDiff(root.right,K))
