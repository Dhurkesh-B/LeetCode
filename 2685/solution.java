class Solution {

    Map<Integer, List<Integer>> paths = new HashMap<>();
    Set<Integer> vis = new HashSet<>();

    public int[] dfs(int node){
        vis.add(node);
        int nodes = 1;
        int edges = paths.getOrDefault(node, new ArrayList<>()).size();
        for(int nei: paths.getOrDefault(node, new ArrayList<>())){
            if(!vis.contains(nei)){
                int[] nodesAndEdges = dfs(nei);
                nodes+=nodesAndEdges[0];
                edges+=nodesAndEdges[1]; 
            }
        }
        return new int[] {nodes, edges};
    }

    public int countCompleteComponents(int n, int[][] edges) {
        int res = 0;
        for(int[] edge: edges){
            int src = edge[0];
            int dest = edge[1];
            paths.computeIfAbsent(src, k -> new ArrayList<>()).add(dest);
            paths.computeIfAbsent(dest, k -> new ArrayList<>()).add(src);
        }

        for(int i=0;i<n;i++){
            if(vis.contains(i))
                continue;
            int[] ne = dfs(i);
            ne[1]/=2;
            if(ne[1]==ne[0]*(ne[0]-1)/2)
                res++;
        }
        return res;
    }
}
