class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)
        profits = []
        for i in range(0,len(prices)):
            day = []
            for j in range(i+1,len(prices)):
                actual_profit = prices[j] - prices[i]
                day.append(actual_profit)
            if day:
                profits.append(max(day))
            else:
                profits.append(0)
        
        return max(profits)
