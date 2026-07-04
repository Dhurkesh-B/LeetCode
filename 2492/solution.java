class Solution {
    Set<Integer> vis = new HashSet<>();
    int res = Integer.MAX_VALUE;
    Map<Integer,List<int[]>> edges = new HashMap<>();
    
    public void dfs(int i){
        if(vis.contains(i))
            return;
        vis.add(i);
        for(int[] edge: edges.get(i)){
            res = Math.min(res, edge[1]);
            dfs(edge[0]);
        }
    }


    public int minScore(int n, int[][] roads) {
        for(int[] road: roads){
            edges.computeIfAbsent(road[0], k -> new ArrayList<>()).add(new int[]{road[1], road[2]});
            edges.computeIfAbsent(road[1], k -> new ArrayList<>()).add(new int[]{road[0], road[2]});

        }
        dfs(1);
        return res;
    }
}
