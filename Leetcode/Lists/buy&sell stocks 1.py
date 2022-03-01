# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        maxProfit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] - buy) > maxProfit:
                maxProfit = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
        return maxProfit
# The solution is straight forward,
# The things to remember, while scanning through the numbers, if you get a lowest number, consider that itself as buying point and go on calculating the profit. Keep on tracking of the maximum profit.
                
                
            