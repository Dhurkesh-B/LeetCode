class Solution {
    public int maxBuilding(int n, int[][] restrictions) {
        List<int[]> restrict = new ArrayList<>();
        for(int[] arr: restrictions)
            restrict.add(arr);
        restrict.add(new int[]{1,0});
        Collections.sort(restrict, (a,b)-> a[0]-b[0]);

        if(restrict.get(restrict.size()-1)[0]!=n)
            restrict.add(new int[]{n,n-1});
        
        int r = restrict.size();
        int res = 0, h1, h2, dist;
        for(int i=1;i<r;i++){
            dist = restrict.get(i)[0] - restrict.get(i-1)[0];
            restrict.get(i)[1] = Math.min(restrict.get(i)[1], restrict.get(i-1)[1]+dist);
        }

        for(int i=r-2;i>=0;i--){
            dist = restrict.get(i+1)[0] - restrict.get(i)[0];
            restrict.get(i)[1] = Math.min(restrict.get(i)[1], restrict.get(i+1)[1]+dist);
        }

        for(int i=1;i<r;i++){
            dist = restrict.get(i)[0] - restrict.get(i-1)[0];
            h1 = restrict.get(i-1)[1];
            h2 = restrict.get(i)[1];
            res = Math.max(res, (h1+h2+dist)/2);
        }

        return res;
    }
}
