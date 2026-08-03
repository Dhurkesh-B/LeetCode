class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            total = 0
            dp[i] = float('-inf') 
            for k in range(i,min(i+3,n)):
                total+=stoneValue[k]
                dp[i] = max(dp[i], total-dp[k+1])
        
        return "Alice" if dp[0]>0 else "Bob" if dp[0]<0 else "Tie"
