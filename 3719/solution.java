class Solution {
    public int longestBalanced(int[] nums) {
        Set<Integer> odd;
        Set<Integer> even;
        int n = nums.length, result = 0;
        for(int i=0;i<n;i++){
            odd = new HashSet<>();
            even = new HashSet<>();
            for(int j=i;j<n;j++){
                if(nums[j]%2==0)
                    even.add(nums[j]);
                else
                    odd.add(nums[j]);

                if(odd.size()==even.size())
                    result = Math.max(result, j-i+1);
            }
        }
        return result;        
    }
}
