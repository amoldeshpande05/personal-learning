# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.


# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        curr = prices[0]    
        for i in range(1,len(prices)):
            if prices[i] > curr:
                print(prices[i],"------",curr)
                profit += prices[i]-curr
            curr = prices[i]
        return profit
    
    
# Explaination:
# Dont worry about buying and selling, maintain a pointer which is having the privious day's value, and current pointer, check if current pointer is greater than the previous days, then assume you purchased previous days and sold it todays and add the profit. that's it