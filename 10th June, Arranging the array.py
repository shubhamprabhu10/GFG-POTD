class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        po=[]
        ne=[]
        for i in arr:
            if(i>=0):
                po.append(i)
            else:
                ne.append(i)
        ln=len(ne)
        i=0
        while(i<ln):
            arr[i]=ne[i]
            i=i+1
        j=0
        while(i<n):
            arr[i]=po[j]
            i=i+1
            j=j+1
