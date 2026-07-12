class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int rank = 1;
        int[] nums = arr.clone();
        Map<Integer, Integer> map = new HashMap<>();
        Arrays.sort(nums);
        for(int i: nums){
            if(!map.containsKey(i))
                map.put(i, rank++);
        }
        for(int i=0;i<arr.length;i++){
            arr[i] = map.get(arr[i]);
        }
        return arr;         
    }
}
