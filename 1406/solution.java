class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] dp = new int[n+1];
        for(int i=n-1;i>=0;i--){
            int sum = 0;
            dp[i] = Integer.MIN_VALUE;
            for(int k=i;k<Math.min(i+3,n);k++){
                sum+=stoneValue[k];
                dp[i] = Math.max(dp[i], sum-dp[k+1]);
            }
        }
        return dp[0]>0 ? "Alice" : dp[0]<0 ? "Bob" : "Tie";
    }
}
