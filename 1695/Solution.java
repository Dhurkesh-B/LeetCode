class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer, Boolean> map = new HashMap<>();
        int result = 0;
        int left = 0, right = 0;
        int curr = 0;
        int n = nums.length;
        while(right<n){
            while(left<= right && map.getOrDefault(nums[right], false)){
                curr-=nums[left];
                map.put(nums[left], false);
                left++;
            }
            curr+=nums[right];
            map.put(nums[right], true);
            result = Math.max(result, curr);
            right++;
        }
        return result;       
    }
}
