class Solution {
    public int minRemoval(int[] nums, int k) {
        int left= 0, result = 0, n = nums.length;
        Arrays.sort(nums);
        for(int right = 0;right<n;right++){
            while((long)nums[left]*k<nums[right])
                left++;
            result = Math.max(result, right-left+1);
        }
        return n-result;
    }
}
