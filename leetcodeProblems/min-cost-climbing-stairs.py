
class Solution:
        
    def minCostClimbingStairs(self, cost) -> int:

        # solution with recurcion, but its time limit

        def solve(ind):
            if ind >= len(cost):
                return 0
            result = cost[ind] + min(solve(ind+1),solve(ind+2))
            return result
        return min(solve(1),solve(0))

    
    #  solution with loop (correct solution)
    def minCostClimbingStairs(self, cost):
        if len(cost)==2:
            return min(cost[0],cost[1])
        dp = [0 for _ in range(len(cost))]
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
        
        