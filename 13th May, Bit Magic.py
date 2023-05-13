from typing import List
class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        i=0
        j=n-1
        c=0
        while(i<=j):
            if(arr[i]!=arr[j]):
                c=c+1
            i=i+1
            j=j-1
        if(c%2==0):
            return(c//2)
        return (c//2 + 1)
