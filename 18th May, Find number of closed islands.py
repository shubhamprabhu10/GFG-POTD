class Solution:
    def closedIslands(self, grid, n, m):
        res = 0
        visited = set()
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i == n or j == m:
                return False            
            if grid[i][j] == 0 or (i, j) in visited: 
                return True            
            visited.add((i, j)) 
            top = dfs(i-1, j)
            bottom = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return top and bottom and right and left
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited and dfs(i, j):
                    res += 1
        return res  
