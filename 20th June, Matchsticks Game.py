class Solution:
    def matchGame(self, N):
        if(N%5==0):
            return -1
        return N%5
