from typing import List
class Solution:
    def kthPermutation(self, n: int, k: int) -> str:
        k -= 1
        pool = []
        factorial = 1
        for i in range(1, n + 1):
            pool.append(str(i))
            factorial *= i
        permutation = ""
        for i in reversed(range(1, n + 1)):
            factorial //= i
            permutation += pool.pop(k // factorial)
            k %= factorial
        return permutation                
