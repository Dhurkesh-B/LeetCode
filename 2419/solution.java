class Solution {
    public int longestSubarray(int[] nums) {
        int result = 0, cur_max = 0, size = 0;
        for(int i: nums){
            if(i>cur_max){
                cur_max = i;
                size = 1;
                result = 0;
            }
            else{
                if(i==cur_max)
                    size++;
                else
                    size = 0;
            }
            result = Math.max(result, size);
        }
        return result;
    }
}
