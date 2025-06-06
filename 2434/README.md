# 2434. Using a Robot to Print the Lexicographically Smallest String

## Problem Statement

You are given a string `s` and a robot that currently holds an empty string `t`. Apply one of the following operations until both `s` and `t` are empty:

1. Remove the first character of `s` and give it to the robot. The robot will append this character to the end of string `t`.
2. Remove the last character of `t` and give it to the robot. The robot will write this character on paper.

Your task is to return the **lexicographically smallest** string that can be written on the paper by performing these operations.

---

## Example

### Example 1:

**Input:**

```
s = "zza"
```

**Output:**

```
azz
```

**Explanation:**

* Initially: p="", s="zza", t="".
* Operation 1 (3 times): t="zza".
* Operation 2 (3 times): p="azz".

### Example 2:

**Input:**

```
s = "bac"
```

**Output:**

```
abc
```

**Explanation:**

* Operation 1 (2 times): t="ba", s="c"
* Operation 2 (2 times): p="ab", t="", s="c"
* Operation 1: t="c"
* Operation 2: p="abc"

### Example 3:

**Input:**

```
s = "bdda"
```

**Output:**

```
addb
```

---

## Constraints

* `1 <= s.length <= 10^5`
* `s` consists only of English lowercase letters.

---

## Solution Approach

The core idea is to simulate the robot behavior using a stack. Maintain a frequency count of all characters in `s` and track the lexicographically smallest available character.

### Steps:

1. Traverse the string `s`, pushing characters into a stack `t` and decrementing their frequency.
2. Keep track of the minimum character still available in the remaining part of `s`.
3. While the top of stack `t` is less than or equal to the smallest remaining character, pop from `t` and add to result.
4. Repeat until both `s` and `t` are empty.

### Time and Space Complexity

* **Time Complexity:** O(n), where `n` is the length of `s`.
* **Space Complexity:** O(n) for the stack and result string.

---

## Code Implementation (Python)

```python
from collections import defaultdict
class Solution:
    def robotWithString(self, s: str) -> str:
        di = defaultdict(int)
        res = ''
        temp = []
        for i in s:
            di[i] += 1
        for c in s:
            temp.append(c)
            di[c] -= 1
            mi = 'a'
            while mi != 'z' and di[mi] == 0:
                mi = chr(ord(mi) + 1)
            while temp and temp[-1] <= mi:
                res += temp.pop()
        return res
```

---

## Tags

`Greedy`, `Stack`, `Simulation`, `Lexicographical Order`

---

⭐ *Feel free to fork and optimize the code. Contributions are welcome!* 🚀
