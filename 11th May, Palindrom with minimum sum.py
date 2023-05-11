import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        arr = [i for i in s]
        start, end = 0, len(arr)-1
        prev = curr = arr[0]
        
        ans = 0
        while start < end:
            if arr[start] == arr[end]:
                if arr[start] == '?':
                    pass
                
            elif arr[start] == '?' or arr[end] == '?':
                
                if arr[start] == '?':
                    arr[start] = arr[end]
                else:
                    arr[end] = arr[start]
                    
            else:
                return -1
                
            start += 1
            end += -1
            
        for i in range(len(arr)//2 + 1):
            if arr[i] != '?':
                prev = curr
                curr = arr[i]
                
                if prev != '?':
                    ans += abs(ord(prev)-ord(curr))
        
        return ans * 2
