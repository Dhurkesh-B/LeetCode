class Solution {
    public int findLHS(int[] nums) {
        HashMap<Integer,Integer> map =  new HashMap<>();
        for(int i:nums){
            if(map.containsKey(i))
                map.put(i,map.get(i)+1);
            else
                map.put(i,1);
        }
        int res = 0;
        ArrayList<Integer> arr = new ArrayList<>(map.keySet());
        Collections.sort(arr);
        for(int i:arr){
            if(map.containsKey(i+1)){
                res = Math.max(res,map.get(i)+map.get(i+1));
            }
        }
        return res;
    }
}
