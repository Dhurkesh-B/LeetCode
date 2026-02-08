/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean result = true;
    public boolean isBalanced(TreeNode root) {
        dfs(root, 0);
        return result;
    }

    public int dfs(TreeNode root, int height){
        if(root!=null){
            int left = dfs(root.left, height) + height+1;
            int right = dfs(root.right, height) + height+1;
            if(Math.abs(left-right)>=2)
                result = false;
            return Math.max(left, right);
        }
        return 0;
    }
}
