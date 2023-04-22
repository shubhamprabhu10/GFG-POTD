class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
       sum+=arr[i]     
        d={}
        x=arr.copy()
        x.sort()
        s=0
        ans=[]
        for i in range(n):
            if x[i] not in d:
                d[x[i]]=s
            s+=x[i]
        for i in arr:
            ans.append(d[i])
        return ans 
