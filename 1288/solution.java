class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> {
            if(a[0]!=b[0])
                return Integer.compare(a[0],b[0]);
            return Integer.compare(b[1],a[1]);
        });
        int res = intervals.length;
        int maxEnding = intervals[0][1];
        for(int i=1;i<intervals.length;i++){
            if(intervals[i][1]<=maxEnding)
                res--;
            else
                maxEnding = intervals[i][1];
        }
        return res;
    }
}
