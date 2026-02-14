class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        float[] previous = {poured};
        for(int row=1;row<=query_row;row++){
            float[] current = new float[row+1];
            for(int i=0;i<row;i++){
                float extra = previous[i]-1;
                if(extra>0){
                    current[i]+=extra/2;
                    current[i+1]+=extra/2;
                }
            }
            previous = current;
        }
        return Math.min(previous[query_glass],1);
    }
}
