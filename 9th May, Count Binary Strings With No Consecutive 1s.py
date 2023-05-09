class Solution: 
    def countStrings(self, N): 
        M = 10**9+7
        
        def matrix_multiply(a, b):
            nonlocal M
            c = [[0, 0], [0, 0]]    # matrix zero
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        c[i][j] = (c[i][j]+a[i][k]*b[k][j])%M
            return c
        
        def matrix_power(a, n):
            nonlocal M
            ans = [[1, 0], [0, 1]]  # matrix one
            while n > 0:
                if n%2 == 1:
                    ans = matrix_multiply(ans, a)
                a = matrix_multiply(a, a)
                n //= 2
            return ans
                
            
        return matrix_power([[1, 1], [1, 0]], N+1)[0][0]

