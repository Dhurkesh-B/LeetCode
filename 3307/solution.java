class Solution {
    public char kthCharacter(long k, int[] operations) {
        int count = 0;
        k--;
        String bits = Long.toBinaryString(k);
        for(int i=0;i<bits.length();i++){
            if(i<operations.length && bits.charAt(i)=='1')
                count+=operations[i];
        }
        return (char)(97+count%26);
    }
}
