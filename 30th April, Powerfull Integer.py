from typing import List
class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        dic = dict()
        occurence = 0
        ans = -1
        for i in intervals:
            if i[0] not in dic:
                dic[i[0]] = 0  
            dic[i[0]] += 1
            if i[1]+1 not in dic:
                dic[i[1]+1] = 0
            dic[i[1]+1] -= 1 
        
        sorted_key = sorted(dic.keys())
        for key in sorted_key:
            if occurence >= k and dic[key] < 0:
                ans = key-1
            occurence += dic[key]
            if occurence >= k:
                ans = key
        return ans                           
