class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if (len(prices) < 2):
            return 0

        left_buy = 0
        right_sell = 1

        max_profit = prices[right_sell] - prices[left_buy]

        while right_sell < len(prices): 
            current_profit = prices[right_sell] - prices[left_buy]
            if (current_profit > 0):
                max_profit = max(max_profit, current_profit)
            else: 
                left_buy = right_sell
            right_sell += 1
        
        if (max_profit < 0):
            return 0
        
        return max_profit

                

