from typing import List

from bisect import bisect_left

class Solution:

    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:

        # code here

        ranges.sort()

        ans=[ranges[0]]

        for i in range(1,n):

            if ans[-1][1]>=ranges[i][0]:

                ans[-1][1]=max(ans[-1][1],ranges[i][1])

            else:

                ans.append(ranges[i])

        m=len(ans)

        s=[0]*m

        s[0]=ans[0][1]-ans[0][0]+1

        for i in range(1,m):

            s[i]+=(s[i-1]+ans[i][1]-ans[i][0]+1)

        fans=[]

        for qq in queries:

            i=bisect_left(s,qq)

            if i==m:

                fans+=[-1]

            else:

                ss=0

                if i>0:

                    ss=s[i-1]

                d=s[i]-qq

                fans+=[ans[i][1]-d]

        return fans

        # code here

        

