
# 3330. Find the Original Typed String I

## Problem Statement

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this **at most once**.

You are given a string `word`, which represents the final output displayed on Alice's screen.

Return the **total number of possible original strings** that Alice might have intended to type.

---

## Examples

### Example 1:

**Input:**

```
word = "abbcccc"
```

**Output:**

```
5
```

**Explanation:**
The possible original strings are:

* "abbcccc"
* "abbccc"
* "abbcc"
* "abbc"
* "abcccc"

### Example 2:

**Input:**

```
word = "abcd"
```

**Output:**

```
1
```

**Explanation:**
No repeated characters to consider.

### Example 3:

**Input:**

```
word = "aaaa"
```

**Output:**

```
4
```

**Explanation:**
The possible original strings are:

* "aaaa"
* "aaa"
* "aa"
* "a"

---

## Constraints

* `1 <= word.length <= 100`
* `word` consists only of lowercase English letters.

---

## Approach

1. Traverse the string and count contiguous groups of the same character.
2. For each group where a character appears more than once, Alice could have intended any length from the full group down to removing just one repeated character (i.e., one long press).
3. For each such group, increment the result by the number of characters that could be reduced **once**.
4. Return the total count of possible interpretations.

---

## Code (Java)

```java
class Solution {
    public int possibleStringCount(String word) {
        int n = word.length(), res = 1, i = 0,j;
        while(i<n){
            j = i;
            while(j+1<n && word.charAt(i)==word.charAt(j+1))
                j++;
            if(j>i){
                res+=(j-i);
                i = j;
            }
            i++;
        }
        return res;        
    }
}
```

---

## Summary

* This problem combines string traversal with counting repeated character sequences.
* It's important to recognize that only one such sequence can have a reduction in length.
* Time Complexity: `O(n)` where `n` is the length of the string.
* Space Complexity: `O(1)`.

