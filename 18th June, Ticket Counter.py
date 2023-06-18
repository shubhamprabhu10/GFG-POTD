class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        i,j=1,N
        while(i<=N and j>=0):
            i+=K
            if (i>=j):
                return j
            j-=K
            if (i>=j):
                return i
