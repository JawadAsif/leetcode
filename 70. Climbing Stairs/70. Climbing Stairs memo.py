class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i: int) -> int:
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)
            return memo[i]
        memo = {}
        return dp(n)
