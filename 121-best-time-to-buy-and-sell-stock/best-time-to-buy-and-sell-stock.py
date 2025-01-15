class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # low_sales = min(prices)
        # day_of_sales = prices.index(low_sales)
        # day_after_low_sales = prices[day_of_sales:] 
        # if day_after_low_sales:
        #     return max(day_after_low_sales) - low_sales
        # return 0
        max_profit = 0
        if len(prices) <= 1 :
            return max_profit
        p1, p2 = 0, 1

        while p2 < len(prices):
            if prices[p1] < prices[p2]:
                max_profit = max((prices[p2] - prices[p1]),max_profit)
                p2 += 1  
            else:
                p1 = p2
                p2 += 1
        return max_profit