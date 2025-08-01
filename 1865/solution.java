
class FindSumPairs {
    int[] nums1;
    int[] nums2;
    Map<Integer,Integer> map;
    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        map = new HashMap<>();
        for(int i:nums2)
            map.put(i,map.getOrDefault(i,0)+1);
    }
    
    public void add(int index, int val) {
        map.put(nums2[index],map.get(nums2[index])-1);
        nums2[index]+=val;
        map.put(nums2[index],map.getOrDefault(nums2[index],0)+1);
    }
    
    public int count(int tot) {
        int count = 0;
        int rem;
        for(int i:nums1){
            rem = tot - i;
            count = count + map.getOrDefault(rem,0);
        }
        return count;     
    }
}
