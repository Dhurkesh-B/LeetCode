class Solution {
    public int longestSubarray(int[] nums) {
        int maxValue = -1;
        int result = 0;
        int curr = 0;
        int n = nums.length;
        for(int i: nums)
            maxValue = Math.max(maxValue,i);
        int i = 0;
        while(i<n){
            curr = 0;
            while(i<n && nums[i]==maxValue){
                curr++;
                i++;
            }
            result = Math.max(result,curr);
            i++;
        }
        return result;        
    }
}
