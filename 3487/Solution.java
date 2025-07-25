class Solution {
    public int maxSum(int[] nums) {
        Set<Integer> vis = new HashSet<>();
        int result = 0;
        int maxi = Integer.MIN_VALUE;
        for(int i: nums){
            if(i>0 && !vis.contains(i)){
                result+=i;
                vis.add(i);
            }
            maxi = Math.max(maxi, i);
        }
        if(vis.size()==0)
            result+=maxi;
        return result;
    }
}
