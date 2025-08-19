class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long count = 0;
        long result = 0;
        for(int i:nums){
            if(i==0)
                count++;
            else{
                result+=((count+1)*count)/2;
                count = 0;
            }
        }
        if(count!=0)
            result+=((count+1)*count)/2;
        return result;   
    }
}
