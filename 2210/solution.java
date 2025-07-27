class Solution {
    public int countHillValley(int[] nums) {
        int result = 0;
        int i = 1;
        int n = nums.length;
        int prev;
        while(i<n-1){
            prev = nums[i-1];
            while(i+1<n-1 && nums[i]==nums[i+1])
                i++;
            if((prev<nums[i] && nums[i]>nums[i+1]) || (prev>nums[i] && nums[i]<nums[i+1]))
                result++;
            i++;
        }
        return result;
    }
}
