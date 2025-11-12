'''
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
premium lock icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # minPriceIdx = prices.index(min(prices))
        # restOfPrices = max(prices[minPriceIdx:])
        # maxPriceIdx = prices.index(restOfPrices)
        # if max(prices[minPriceIdx:]) > prices[minPriceIdx]:
        #     profit = prices[maxPriceIdx] - prices[minPriceIdx]
        # return profit

        buy = prices[0]
        sell = 0
        lowIdx = 0
        tempProfit = 0
        for i in range(len(prices)):
            if prices[i] < buy and i != len(prices)-1:
                buy = prices[i]
                lowIdx = i
                sell = 0
                #print("buy: ",buy)
            elif lowIdx < i and tempProfit < prices[i]-buy:
                sell = prices[i]
                #print("sell: ",sell)
            if sell-buy > tempProfit:
                tempProfit = sell - buy
            #print("tempProfit:", tempProfit)
        #print("sell: ",sell, "buy: ",buy)
        profit = tempProfit
        return profit

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices)) #5