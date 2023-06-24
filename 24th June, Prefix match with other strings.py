import re
class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        ch=s[:k]
        count=0
        for i in range (n):
            if ch in arr[i] and re.search("^"+ch,arr[i]) and k<=len(arr[i]) and k<=len(s):
                count+=1
        return count
