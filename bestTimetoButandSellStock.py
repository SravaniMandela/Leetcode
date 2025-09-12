class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        max_profit=0
        max_p=[]
        for i in range(1,len(prices)):
            if(prices[i]<min):
                min=prices[i]
            else:
                max_profit=prices[i]-min
                max_p.append(max_profit)
        return max(max_p)
                
prices=[7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))



# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.