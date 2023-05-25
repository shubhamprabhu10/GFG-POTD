class Solution:
    def addOperators(self, S, target):
        def dfs(l, r, expr, cur, last, res):
            if l == r:
                if cur == target:
                    res.append(expr)
                return
            for i in range(l + 1, r + 1):
                if i == l + 1 or (i > l + 1 and S[l] != "0"):
                    s, x = S[l:i], int(S[l:i])
                    if last is None:
                        dfs(i, r, s, x, x, res)
                    else:
                        dfs(i, r, expr+"+"+s, cur + x, x, res)
                        dfs(i, r, expr+"-"+s, cur - x, -x, res)
                        dfs(i, r, expr+"*"+s, cur-last+last*x, last*x, res)
        res = []
        dfs(0, len(S), '', 0, None, res)
        return res
