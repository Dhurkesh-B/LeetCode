class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int[] bits = new int[32];
        Arrays.fill(bits,-1);
        int max_or = 0, curr, position, max_index;
        for(int i=n-1;i>=0;i--){
            max_or = max_or | nums[i];
            curr = nums[i];
            position = 0;
            while(curr>0){
                if(curr%2==1)
                    bits[position] = i;
                curr/=2;
                position++;
            }
            max_index = Arrays.stream(bits).max().getAsInt();
            if(max_index==-1)
                result[i] = 1;
            else
                result[i] = max_index-i+1;
        }
        return result;
    }
}
