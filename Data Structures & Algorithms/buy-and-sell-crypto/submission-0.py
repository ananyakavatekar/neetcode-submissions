class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_sell = 0


        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                if (sell - buy > max_sell):
                    max_sell = sell - buy
        return max_sell