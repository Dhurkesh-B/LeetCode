class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        
        List<Integer> arr = new ArrayList<>();
        for(int[] val: grid){
            for(int i: val)
                arr.add(i);
        }
        int n = arr.size();
        k = k%n;
        int col = grid[0].length;
        List<Integer> rotated = new ArrayList<>();
        rotated.addAll(arr.subList(n-k,n));
        rotated.addAll(arr.subList(0,n-k));

        for(int i=0;i<n;i++)
            grid[i/col][i%col] = rotated.get(i);
        
        List<List<Integer>> res = new ArrayList<>();
        for(int[] val: grid){
            List<Integer> list = new ArrayList<>();
            for(int i: val)
                list.add(i);
            res.add(list);
        }

        return res;

    }

}
