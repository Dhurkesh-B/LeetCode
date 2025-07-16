class Solution {
    public int maximumLength(int[] nums) {
        int res = 0;
        int oddEven = 0;
        int evenOdd = 0;
        int even = 0;
        int odd = 0;
        for(int i:nums){
            if(i%2==evenOdd%2)
                evenOdd++;
            if(i%2!=oddEven%2)
                oddEven++;
            if(i%2==1)
                odd++;
            else
                even++;
        }
        res = Math.max(oddEven,Math.max(evenOdd,Math.max(odd,even)));
        return res;
    }
}
