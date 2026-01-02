class Solution {
    public int repeatedNTimes(int[] nums) {
        Set<Integer> vis = new HashSet<>();
        for(int i:nums){
            if(vis.contains(i))
                return i;
            vis.add(i);
        }
        return 0;
    }
}
