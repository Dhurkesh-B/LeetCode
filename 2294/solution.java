class Solution {
    public int partitionArray(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        int i = 0, res = 0;
        int j;
        while(i<n){
            j = i;
            while(j+1<n && nums[j+1]-nums[i]<=k)
                j++;
            res++;
            i = j+1;
        }
        return res;
                
    }
}
