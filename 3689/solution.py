class Solution {
    public long maxTotalValue(int[] nums, int k) {
        long minValue = Long.MAX_VALUE;
        long maxValue = Long.MIN_VALUE;
        for(int i:nums){
            minValue = Math.min(minValue, i);
            maxValue = Math.max(maxValue, i);
        }
        long res = (maxValue-minValue)*k;
        return res;
    }
}
