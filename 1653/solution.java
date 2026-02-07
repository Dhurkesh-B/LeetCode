class Solution {
  public int minimumDeletions(String s) {
    int result = 0;
    Stack<Character> stack = new Stack<>();
    stack.push('c');
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) == 'a' && stack.peek() == 'b') {
        result++;
        stack.pop();
      } else
        stack.push(s.charAt(i));
    }
    return result;
  }
}
