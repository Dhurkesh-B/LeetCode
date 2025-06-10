# 3442. Maximum Difference Between Even and Odd Frequency I

## Problem Statement

You are given a string `s` consisting of lowercase English letters.

Your task is to find the maximum difference `diff = a1 - a2` between the frequency of characters `a1` and `a2` in the string such that:

* `a1` has an **odd** frequency in the string.
* `a2` has an **even** frequency in the string.

Return this **maximum difference**.

---

## Examples

### Example 1:

**Input:**

```
s = "aaaaabbc"
```

**Output:**

```
3
```

**Explanation:**

* Character 'a' appears 5 times (odd), 'b' appears 2 times (even).
* The difference is `5 - 2 = 3`.

### Example 2:

**Input:**

```
s = "abcabcab"
```

**Output:**

```
1
```

**Explanation:**

* 'a': 3 (odd), 'c': 2 (even) → `3 - 2 = 1`

---

## Constraints

* `3 <= s.length <= 100`
* `s` consists only of lowercase English letters.
* `s` contains **at least one character with an odd frequency** and **one with an even frequency**.

---

## Solution Approach

The algorithm:

1. Count frequency of each character.
2. Track the maximum frequency among **odd counts**.
3. Track the minimum frequency among **even counts**.
4. Return the difference between them.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`, where `n` is the length of the string.
* **Space Complexity:** `O(1)`, as at most 26 characters are stored.

---

## Key Insights

* Handles multiple characters with odd/even counts.
* Guarantees output as per constraints.

---

⭐ *If this helped, consider sharing or contributing improvements!*
