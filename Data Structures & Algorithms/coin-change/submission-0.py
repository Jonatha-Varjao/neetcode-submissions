class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def minCoins(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            
            if remaining in cache:
                return cache[remaining]
            
            best = float('inf')
            for coin in coins:
                result = minCoins(remaining-coin)
                if result != -1:
                    best = min(best, result + 1 )

            final_result = best if best != float('inf') else -1
            cache[remaining] = final_result
            
            return final_result

        return minCoins(amount)