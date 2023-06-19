class Solution:
    #Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    #with O(1) extra space.
    def arrange(self,arr, n): 
        #Your code here
        tempar=[0]*n
        for i in range(n):
            tempar[i]=arr[arr[i]]            
        arr[:]=tempar[:]
