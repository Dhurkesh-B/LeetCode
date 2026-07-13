class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        int minDigit = (int)Math.floor(Math.log10(low))+1;
        int maxDigit = (int)Math.floor(Math.log10(high))+1;
        String s = "123456789";
        List<Integer> res = new ArrayList<>();
        for(int l=minDigit;l<=maxDigit;l++){
            for(int i=0;i<10-l;i++){
                int value = Integer.parseInt(s.substring(i,i+l));
                if(value>high)
                    break;
                if(value>=low)
                    res.add(value);
            }
        }
        return res;
    }
}
