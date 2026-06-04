'''
123. Best Time to Buy and Sell Stock III
Solved
Hard
Topics
premium lock icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        # find min1 max1, min2, max2
        # choose between (max1-min1 + max2-min2) or max2 - min1
        
        # minIndex = 0
        # maxIndex = -1
        # profit = 0
        
        if len(prices) == 0:
            return 0

        first =  Solution.profit(self, prices)
        profit = first[0]
        if first[2] == -1:
            return 0

        left = Solution.profit(self, prices[:first[1]])
        right = Solution.profit(self, prices[first[2]+1:])
        mid = Solution.loss(self, prices[first[1]+1:first[2]]) * -1


        return profit + max(left[0], right[0], mid)
    
    def profit(self, prices):
        if len(prices) == 0:
            return [0,0,0]
        minIndex = 0
        currentMin = 0
        maxIndex = -1
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= prices[minIndex]:
                minIndex = i
            if profit < prices[i] - prices[minIndex]:
                profit = prices[i] - prices[minIndex]
                maxIndex = i
                currentMin = minIndex
        return [profit, currentMin ,maxIndex]

    def loss(self, prices):
        if len(prices) == 0:
            return 0
        loss = 0
        maxValue = prices[0]
        for i in range(len(prices)):
            maxValue = max(prices[i], maxValue)
            loss = min(prices[i] - maxValue, loss)
        return loss
    
prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices)) # 6