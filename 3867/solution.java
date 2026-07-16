class Solution {
    public int gcd(int a, int b){
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }

    public long gcdSum(int[] nums) {
        int mx = nums[0];
        int n = nums.length;
        int[] prefixGcd = new int[n];
        long result = 0l;
        for(int i=0;i<n;i++){
            mx = Math.max(mx, nums[i]);
            prefixGcd[i] = gcd(nums[i], mx);
        }
        Arrays.sort(prefixGcd);
        for(int i=0;i<(n/2);i++)
            result+=gcd(prefixGcd[i], prefixGcd[n-1-i]);
        return result;
    }
}
