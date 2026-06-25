class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int counter = 0;
        int res = 0;
        for(int i=0;i<nums.length;i++){
            counter =0;
            for(int j=i;j<nums.length;j++){
                if(nums[j]==target)
                    counter++;
                if(2*counter>j-i+1)
                    res++;
            }
        }
        return res;
    }
}
