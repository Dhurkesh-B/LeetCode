# 3170. Lexicographically Minimum String After Removing Stars

## Problem Statement

You are given a string `s` that may contain any number of `'*'` characters. Your task is to remove all `'*'` characters by following a specific rule:

> While there is a `'*'` in the string:
>
> * Delete the leftmost `'*'` and the **smallest non-`'*'` character to its left**. If there are several smallest characters, you can delete any of them.

Return the **lexicographically smallest** resulting string after all `'*'` characters are removed.

## Example

### Example 1:

**Input:**

```
s = "aaba*"
```

**Output:**

```
"aab"
```

**Explanation:**
We delete one of the 'a' characters with the '\*'. Removing `s[3]` makes the string lexicographically smallest.

### Example 2:

**Input:**

```
s = "abc"
```

**Output:**

```
"abc"
```

**Explanation:**
There is no `'*'` in the string, so no change is needed.

## Constraints

* `1 <= s.length <= 10^5`
* `s` consists only of lowercase English letters and `'*'`
* The input is guaranteed to be valid such that all `'*'` can be removed

---

## Approach

To solve this problem efficiently:

* Use a list of stacks (26 in total) to store character indices for each lowercase letter.
* Traverse the string and:

  * If you encounter a character, store its index in the corresponding stack.
  * If you encounter a `'*'`, remove the latest smallest character (lexicographically) to the left by checking the stacks in order.
* Finally, rebuild the result by skipping the marked characters.

This ensures both correctness and optimal performance.

---

## Python Implementation

```python
from collections import defaultdict
class Solution:
    def clearStars(self, s: str) -> str:
        counter = [[] for _ in range(26)]
        s = list(s)
        res = ''
        for i, c in enumerate(s):
            if c == '*':
                for j in range(26):
                    if counter[j]:
                        ind = counter[j].pop()
                        s[ind] = '*'
                        break
            else:
                counter[ord(c) - ord('a')].append(i)
        for c in s:
            if c != '*':
                res += c
        return res
```

### Time and Space Complexity

* **Time Complexity:** O(n \* 26) => O(n), where n is the length of the string
* **Space Complexity:** O(n) for storing indices in stacks

---

## Usage Example

```python
sol = Solution()
print(sol.clearStars("aaba*"))  # Output: "aab"
```

---

## Notes

* This approach ensures that the result is lexicographically smallest.
* Efficient handling of character tracking is key to keeping the algorithm fast.

---


