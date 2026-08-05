class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        
        List<Integer>[] graph = new ArrayList[n];
    
        for(int i=0;i<n;i++)
            graph[i] = new ArrayList<>();

        for(int[] edge: invocations)
            graph[edge[0]].add(edge[1]); 
        
        boolean isSafe = false;
        boolean[] suspicious = new boolean[n];
        suspicious[k] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(k);

        while(!queue.isEmpty()){
            int node = queue.poll();
            for(int nei: graph[node]){
                if(!suspicious[nei]){
                    suspicious[nei] = true;
                    queue.offer(nei);
                }
            }
        }

        for(int[] edge: invocations){
            int u = edge[0];
            int v = edge[1];
            if(suspicious[u]==false && suspicious[v]==true){
                isSafe = true;
                break;
            }
        }

        List<Integer> res = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(isSafe==true || suspicious[i]==false)
                res.add(i);
        }
        return res;
    }
}
