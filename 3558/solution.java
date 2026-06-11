class Solution {
    public int assignEdgeWeights(int[][] edges) {
        Map<Integer, List<Integer>> emap = new HashMap<>();
        Map<Integer, Integer> depth = new HashMap<>();
        int mod = 1_000_000_007;
        int maxDepth = 0;
        for(int[] edge: edges){
            int u = Math.min(edge[0], edge[1]);
            int v = Math.max(edge[0], edge[1]);
            emap.putIfAbsent(u, new ArrayList<>());
            emap.get(u).add(v);
        }
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        depth.put(1,0);
        while(!queue.isEmpty()){
            int node = queue.poll();
            if(!emap.containsKey(node))
                continue;
            for(int child: emap.get(node)){
                depth.put(child, depth.get(node)+1);
                maxDepth = Math.max(maxDepth, depth.get(child));
                queue.offer(child);
            }
        }
        long res = 1;
        for (int i = 0; i < maxDepth - 1; i++) {
            res = (res * 2) % mod;
        }
        return (int) res;
    }
}
