class Solution():
    def maxSweetness(self, sweetness, n, k):
        #your code goes here
        def torelable(val):
            sweet=0
            count=0
            for i in sweetness:
                sweet +=i
                if sweet >=val:
                    count+=1
                    sweet=0
            if count>=k+1:
                return True
            else:
                return False
        
        low= min(sweetness)
        high=sum(sweetness)+1
        while low<high:
            mid=(low+high)//2
            if torelable(mid)==False:
                high=mid
            else:
                low=mid+1
        return low-1
