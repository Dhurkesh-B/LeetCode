class Solution {
    public int compareVersion(String version1, String version2) {
        ArrayList<Integer> v1 = new ArrayList<>();
        ArrayList<Integer> v2 = new ArrayList<>();
        for(String s:version1.split("\\."))
            v1.add(Integer.parseInt(s));
        for(String s:version2.split("\\."))
            v2.add(Integer.parseInt(s));
        int length = Math.max(v1.size(), v2.size());
        int x,y;
        for(int i=0;i<length;i++){
            if(i<v1.size())
                x = v1.get(i);
            else
                x = 0;
            if(i<v2.size())
                y = v2.get(i);
            else
                y = 0;
            if(x>y)
                return 1;
            if(x<y)
                return -1;
        }
        return 0;

    }
}
