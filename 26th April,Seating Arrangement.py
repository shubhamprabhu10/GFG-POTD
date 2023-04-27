

from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        if m==1:
            if seats[0]==1 and n==0:
                return True
            elif seats[0]==0 and n==1:
                return True
            elif seats[0]==0 and n>0:
                return False
        for i in range(m):
            if n==0:
                return True
            if i==0:
                if seats[i]==0 and seats[i+1]==0:
                    seats[i]=1
                    n-=1
            if i==m-1:
                if seats[i]==0 and seats[i-1]==0:
                    seats[i]=1
                    n-=1
            if seats[i]==0 and seats[i-1]==0 and seats[i+1]==0:
                seats[i]=1
                n-=1
        if n==0:
            return True
        else:
            return False
