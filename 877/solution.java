class Solution {

    private Integer[][] dp;

    public int dfs(int[] piles, int left, int right){
        if(left==right)
            return piles[left];

        if(dp[left][right]!=null)
            return dp[left][right];

        int leftSide = piles[left] - dfs(piles,left+1,right);
        int rightSide = piles[right] - dfs(piles,left, right-1);
        dp[left][right] = Math.max(leftSide,rightSide);
        return dp[left][right];
    }

    public boolean stoneGame(int[] piles) {
        int n = piles.length;
        dp = new Integer[n][n];
        boolean res = dfs(piles,0,n-1)>=1;
        return res;
    }
}
