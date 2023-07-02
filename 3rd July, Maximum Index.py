class Solution:
	def maxIndexDiff(self,arr, n):
        leftMin = [0]*n
        leftMin[0] = arr[0]
        for i in range(1,n):
            leftMin[i] = min(leftMin[i-1], arr[i])
        maxDist = - 2**32
        i = n-1
        j = n-1
        while(i>=0  and  j>=0):
            if(arr[j] >= leftMin[i]):
                maxDist = max(maxDist, j-i)
                i-=1
            else:
                j-=1
        return maxDist
