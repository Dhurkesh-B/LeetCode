class Solution {
    public int findGCD(int[] nums) {
        int smallValue = Integer.MAX_VALUE;
        int largeValue = Integer.MIN_VALUE;
        for(int i: nums){
            smallValue = Math.min(smallValue, i);
            largeValue = Math.max(largeValue, i);
        }
        while(smallValue>0){
            int temp = smallValue;
            smallValue = largeValue%smallValue;
            largeValue = temp;
        }
        return largeValue;
    }
}
