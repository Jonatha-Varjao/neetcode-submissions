class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy_so_far = 0

        best_buy_so_far = prices[0] 
        max_profit = 0

        for i in range(1,len(prices)):
            profit_day = prices[i] - best_buy_so_far
            if profit_day > max_profit:
                max_profit = profit_day
                
            elif best_buy_so_far - prices[i] > 0:
                best_buy_so_far = prices[i]
        
        return max_profit
