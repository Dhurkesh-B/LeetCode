class Solution {
    public boolean isPowerOfThree(int n) {        
        double value =  Math.log(n)/Math.log(3);
        return n>0 && Math.abs(value-Math.round(value))< 1e-10;
    }
}
