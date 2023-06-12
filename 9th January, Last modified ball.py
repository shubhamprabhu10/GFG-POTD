class Solution():
    def solve(self, N, A):        
        while N>0:
            if (A[N-1]<=8):
                return N
            N=N-1                
