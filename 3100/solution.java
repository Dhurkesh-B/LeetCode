class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int result = numBottles;
        int empty = numBottles;
        while(empty>=numExchange){
            empty-=(numExchange-1);
            numExchange++;
            result++;
        }
        return result;
        
    }
}
