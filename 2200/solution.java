class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        ArrayList<Integer> kindex = new ArrayList<>();
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]==key)
                kindex.add(i);
        }
        ArrayList<Integer> res = new ArrayList<>();
        int start = 0;
        for(int ind:kindex){
            for(int i=Math.max(start,ind-k);i<Math.min(n,ind+k+1);i++){
                res.add(i);
            }
            start = ind+k+1;

        }
        return res;
        
    }
}
