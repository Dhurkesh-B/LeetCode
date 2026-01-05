class Solution {
    public long maxMatrixSum(int[][] matrix) {
        int neg = 0;
        int mi = Integer.MAX_VALUE;
        boolean zero = false;
        int result = 0;
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]==0)
                    zero = true;
                else{
                    if(matrix[i][j]<0)
                        neg++;
                }

                result+=Math.abs(matrix[i][j]);
                mi = Math.min(mi,Math.abs(matrix[i][j]));

            }
        }
        if(neg%2!=0 && zero!=true){
            result-=2*mi;
            
        }
        return result;
    }
}
