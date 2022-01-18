class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mx = 0
        buy = prices[0]
        for i in range(len(prices)):
            if buy>prices[i]:
                buy = prices[i]
            else:
                mx = max(mx,(prices[i] - buy))
            
        return mx