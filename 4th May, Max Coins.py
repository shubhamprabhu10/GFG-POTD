class Solution:
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        # code here
        ranges.sort(key=lambda e: (e[1], e[0]))
        
        maxv, ends = [], []
        sofar, ans = 0, 0
        for start, end, v0 in ranges:
            lo, hi = 0, len(ends)
            while lo < hi:
                mi = lo+(hi-lo)//2
                if ends[mi] <= start:
                    lo = mi+1
                else:
                    hi = mi
            v = v0
            if 0 <= lo-1 < len(ends):
                v += maxv[lo-1]
            ans = max(ans, v)
            ends.append(end)
            sofar = max(sofar, v0)
            maxv.append(sofar)
        return ans
