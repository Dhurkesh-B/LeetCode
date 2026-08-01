class Solution {

    public int dfs(int[] arr, int left, int right){
        if(left==right)
            return arr[left];
        int leftSide = arr[left] - dfs(arr, left+1, right);
        int rightSide = arr[right] - dfs(arr, left, right-1);
        return Math.max(leftSide, rightSide);
    }
    public boolean predictTheWinner(int[] nums) {
        return dfs(nums, 0, nums.length-1)>=0;
    }
}
