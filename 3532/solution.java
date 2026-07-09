class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] clusters = new int[n];
        int cluster = 1;
        boolean[] res = new boolean[queries.length];
        clusters[0] = cluster;
        for(int i=1;i<n;i++){
            if(nums[i]-nums[i-1]>maxDiff)
                cluster++;
            clusters[i] = cluster;
        }
        for(int i=0;i<queries.length;i++){
            int u = queries[i][0];
            int v = queries[i][1];
            if(clusters[u]==clusters[v] || u==v)
                res[i] = true;
            else
                res[i] = false;
        } 
        return res;
    }
}
