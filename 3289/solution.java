class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int n = nums.length;
        int[] cnt = new int[n];
        int ind = 0;
        int[] res = new int[2];
        for(int i:nums){
            if(cnt[i]==1)
                res[ind++] = i;
            else
                cnt[i] = 1;
        }
        return res;
    }
}
