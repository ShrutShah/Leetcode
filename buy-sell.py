class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0

        for curr in prices[1:]:

            if curr < buy:
                buy = curr
            
            else:
                profit = max(profit, curr - buy)

        return profit
