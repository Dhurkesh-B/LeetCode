class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int result = numBottles;
        int empty = numBottles;
        int fullBottles = 0;
        while(empty>=numExchange){
            empty-=(numExchange-1);
            numExchange++;
            result++;
        }
        return result;
        
    }
}
