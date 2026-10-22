class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        #buying point 
        left = 0
        #selling point 
        right = 1

        while right < len(prices):
            if (prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else: 
                # buying price is equal or greater than selling
                left = right
            right += 1
        
        return maxProfit

        