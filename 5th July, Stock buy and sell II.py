class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        profit = 0
        for i in range(1, n):
        # checks if elements are adjacent and in increasing order
            if prices[i] > prices[i-1]:
            # difference added to 'profit'
                profit += prices[i] - prices[i-1]
        return profit
