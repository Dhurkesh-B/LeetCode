class Solution {
    public String answerString(String word, int numFriends) {
        String res = "";
        int l = word.length();

        if (numFriends == 1) {
            return word;
        }

        for (int i = 0; i < l; i++) {
            int ml = Math.min(l - numFriends + 1, l - i);
            String curr = word.substring(i, i + ml);
            if (curr.compareTo(res) > 0) {
                res = curr;
            }
        }

        return res;
    }
}
