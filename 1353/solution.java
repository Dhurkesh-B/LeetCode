
class Solution {
    public int maxEvents(int[][] events) {
        int n = events.length;
        int lastDay = 0;
        for(int[] event:events)
            lastDay = Math.max(lastDay,event[1]);
        Arrays.sort(events,(a,b)->Integer.compare(a[0],b[0]));
        PriorityQueue<Integer> minHeap = new PriorityQueue();
        int i = 0;
        int count = 0;
        for(int day=1;day<=lastDay;day++){
            while(i<n && events[i][0]==day)
                minHeap.add(events[i++][1]);
            while(!minHeap.isEmpty() && day>minHeap.peek())
                minHeap.poll();
            if(!minHeap.isEmpty()){
                minHeap.poll();
                count++;
            }
            if(minHeap.isEmpty() && i>=n)
                break;
        }
        return count; 
        
    }
}
