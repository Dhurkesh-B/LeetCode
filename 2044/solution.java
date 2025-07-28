class Solution {
    int result = 0;
    int max_or = 0;

    private void dfs(int[] nums, int curr,int i){
        if(i==nums.length){
            if(curr==max_or)
                result++;
            return;
        }
        dfs(nums,curr,i+1);
        dfs(nums,curr|nums[i],i+1);
    }
    public int countMaxOrSubsets(int[] nums) {
        for(int i:nums)
            max_or = max_or | i;
        dfs(nums,0,0);
        return result;
    }
}
