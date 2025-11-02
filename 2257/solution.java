class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        char[][] grid = new char[m][n];
        int result = 0;
        for(int[] guard:guards)
            grid[guard[0]][guard[1]] = 'g';
        
        for(int[] wall:walls)
            grid[wall[0]][wall[1]] = 'w';

        int r,c,cr,cc;
        for(int[] guard:guards){
            r = guard[0];
            c = guard[1];
            //left
            cc = c-1;
            while(cc>=0 && grid[r][cc]!='g' && grid[r][cc]!='w')
                grid[r][cc--] = 'o';
            //right
            cc = c+1;
            while(cc<n && grid[r][cc]!='g' && grid[r][cc]!='w')
                grid[r][cc++] = 'o';
            //top
            cr = r-1;
            while(cr>=0 && grid[cr][c]!='g' && grid[cr][c]!='w')
                grid[cr--][c] = 'o';
            //bottom
            cr = r+1;
            while(cr<m && grid[cr][c]!='g' && grid[cr][c]!='w')
                grid[cr++][c] = 'o';
            
        }

        for(char[] chr:grid){
            for(char ch:chr){
                if(ch=='\u0000')
                    result++;
            }
        }
        return result;

    }
}
