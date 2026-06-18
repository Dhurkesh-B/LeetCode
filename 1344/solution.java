class Solution {
    public double angleClock(int hour, int minutes) {
        double res = Math.abs(30*hour - 5.5*minutes);
        return Math.min(res, 360-res);
    }
}
