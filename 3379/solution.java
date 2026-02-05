class Solution {
    public int[] constructTransformedArray(int[] nums) {
     int n = nums.length, index;
     int[] result = new int[n];
     index = nums[0]%n;
     if(index<0)
        index = n+index;
     result[0] = nums[index];
     for(int i=1;i<n;i++){
        index = (i + nums[i])%n;      
        if(index<0)
            index = n+index;
        result[i] = nums[index%n];
     }   
     return result;
    }
}
