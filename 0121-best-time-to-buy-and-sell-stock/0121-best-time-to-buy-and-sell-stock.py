class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0;
        pointer1 = 0
        pointer2 = 1
        
        #use pointer two it always iterate ahead
        while pointer2 < len(prices):
            if prices[pointer1] < prices[pointer2] : #3, 5
                #find difference 
                prof = prices[pointer2] - prices[pointer1]
                max_profit = max(max_profit, prof) # get max

            else:
                #assigned pointer2 index to pointer1 since are interrested to only buy item at lower price
                pointer1 = pointer2
            pointer2 += 1
        return max_profit