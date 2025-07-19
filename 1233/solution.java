class Solution {
    public static boolean notStartWith(String s1, String s2){
        String[] arr1 = s1.split("/");
        String[] arr2 = s2.split("/");
        for(int i=0;i<Math.min(arr1.length, arr2.length);i++){
            if(!arr1[i].equals(arr2[i]))
                return true;
        }
        return false;
    }
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        List<String> result = new ArrayList<>();
        result.add(folder[0]);
        for(String s: folder){
            if(notStartWith(result.get(result.size()-1),s))
                result.add(s);
        }
        return result;
    }
}
