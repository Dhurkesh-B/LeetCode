# 3304. Find the K-th Character in String Game I

## Problem Statement

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a positive integer `k`.

Now Bob will ask Alice to perform the following operation forever:

> Generate a new string by changing each character in `word` to its next character in the English alphabet, and append it to the original word.

For example:

* Performing the operation on "c" generates "cd"
* Performing the operation on "zb" generates "zbac"

Return the value of the **k-th character** in `word`, after enough operations have been done for `word` to have at least `k` characters.

📌 Note: The character `'z'` wraps around to `'a'`.

---

## Examples

### Example 1:

**Input:**

```
k = 5
```

**Output:**

```
"b"
```

**Explanation:**
After 3 operations:

* "a" → "ab" → "abbc" → "abbcbccd"
  The 5th character is 'b'.

### Example 2:

**Input:**

```
k = 10
```

**Output:**

```
"c"
```

---

## Constraints

* `1 <= k <= 500`

---

## Approach

1. Start with the string "a".
2. Repeat the operation of generating and appending the next characters until the length of the string is at least `k`.
3. Use a character mapping to get the next letter.
4. Return the `k-th` character.

---

## Code Representation

---

## Summary

* This is a simulation problem with string transformations.
* Key optimization: Only simulate until reaching length `k`.
* Useful for understanding recursive character expansion and wrapping behavior.

---
