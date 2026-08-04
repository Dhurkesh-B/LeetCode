class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Set<Integer> vis = new HashSet<>();
        int minValue = Integer.MAX_VALUE;
        int maxValue = Integer.MIN_VALUE;
        for(int i: nums){
            minValue = Math.min(minValue, i);
            maxValue = Math.max(maxValue, i);
            vis.add(i);
        }
        List<Integer> res = new ArrayList<>();
        for(int i=minValue;i<maxValue;i++){
            if(!vis.contains(i))
                res.add(i);
        }
        return res;
    }
}
