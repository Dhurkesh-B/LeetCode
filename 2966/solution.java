
class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        int[][] arr = new int[n/3][3];
        boolean ck = false;
        int[] temp = new int[3];
        int max,min;
        for(int i=0;i<n;i+=3){
            max = nums[i];
            min = nums[i];
            for(int j=i;j<i+3;j++){
                max = Math.max(nums[j],max);
                min = Math.min(nums[j],min);
                temp[j-i] = nums[j];
            }
            
            if(max-min<=k)
                for(int j=0;j<3;j++)
                    arr[i/3][j] = temp[j];
            else{
                ck = true;
                break;
            }
        }
        if(ck)
            return new int[0][0];
        return arr;
    }
}
