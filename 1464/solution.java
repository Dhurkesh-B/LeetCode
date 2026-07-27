class Solution {
    public int maxProduct(int[] nums) {
        int max1 = -1;
        int max2 = -1;

        for(int i: nums){
            if(i-1>max1){
                max2 = max1;
                max1 = i-1;
            }
            else if(i-1>max2)
                max2 = i-1;
        }
        
        return max1*max2;
    }
}
