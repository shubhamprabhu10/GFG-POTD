class Solution:
    def findMoves(self,n,chairs,passengers):
        #code here
        chairs.sort()
        passengers.sort()
        # print(chairs)
        # print(passengers)
        c=0
        for i in range(n):
            c=c+abs(passengers[i]-chairs[i])
        return c
