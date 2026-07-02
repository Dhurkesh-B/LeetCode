class Solution {
    int[][] best;
    int row, col;
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        row = grid.size();
        col = grid.get(0).size();
        best = new int[row][col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++)
                best[i][j] = -1;
        }
        return dfs(0,0,health-grid.get(0).get(0),grid);
    }

    private boolean dfs(int r, int c, int health, List<List<Integer>> grid){
        if(r==row-1 && c==col-1)
            return health>0;
        
        if(health<=0)
            return false;
        
        if(best[r][c]>=health)
            return false;
        
        best[r][c] = health;

        int[][] direct = {{0,-1}, {0,1},{-1,0}, {1,0}};

        for(int[] dir: direct){
            int nr = r+dir[0];
            int nc = c+dir[1];
            if(nr>=0 && nr<row && nc>=0 && nc<col)
                if(dfs(nr,nc,health-grid.get(nr).get(nc),grid))
                    return true;
        }
        return false;
    }
}
