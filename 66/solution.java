class Solution {
    public int[] plusOne(int[] digits) {
        int ind = digits.length-1;
        while(ind>=0){
            if(digits[ind]<9){
               digits[ind]++;
               break; 
            }
            digits[ind] = 0;
            ind--;
        }
        if(ind==-1){
            int[] result = new int[digits.length+1];
            result[0] = 1;
            for(int i=1;i<result.length;i++)
                result[i] = 0;
            return result;
        }

        return digits;

    }
}
