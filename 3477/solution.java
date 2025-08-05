    class Solution {
        public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
            int n = fruits.length, ind;
            ArrayList<Integer> basket = new ArrayList<>();
            for(int b: baskets)
                basket.add(b);
            for(int i=0;i<n;i++){
                ind = -1;
                for(int j=0;j<basket.size();j++){
                    if(basket.get(j)>=fruits[i]){
                        ind = j;
                        break;
                    }
                }
                if(ind!=-1)
                    basket.remove(ind);

            }
            return basket.size();            
        }
    }
