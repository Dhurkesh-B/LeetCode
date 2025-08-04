class Solution {
    public int totalFruit(int[] fruits) {
        int n = fruits.length;
        int left = 0, result = 0, total = 0;
        int fruit;
        Map<Integer, Integer> map = new HashMap<>();
        for(int right: fruits){
            map.put(right, map.getOrDefault(right,0)+1);
            total++;
            while(map.size()>2){
                fruit = fruits[left];
                map.put(fruit, map.get(fruit)-1);
                total--;
                if(map.get(fruit)==0)
                    map.remove(fruit);

                left++;
            }
            result = Math.max(result, total);
        }
        return result;
    }
}
