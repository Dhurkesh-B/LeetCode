
# 🏠 Leetcode 2044: Count Number of Maximum Bitwise-OR Subsets

## 📘 Problem Statement

Given an integer array `nums`, find the **maximum possible bitwise OR** of any non-empty subset of `nums` and **return the number of different non-empty subsets** with that maximum bitwise OR.

Two subsets are considered different if the indices of the elements chosen are different.

---

## 🧪 Examples

### ✅ Example 1:

**Input:** `nums = [3,1]`
**Output:** `2`

**Explanation:**

* Maximum OR = `3`
* Subsets: `[3]`, `[3,1]`

---

### ✅ Example 2:

**Input:** `nums = [2,2,2]`
**Output:** `7`

**Explanation:**

* Maximum OR = `2`
* All 7 non-empty subsets have OR = 2

---

### ✅ Example 3:

**Input:** `nums = [3,2,1,5]`
**Output:** `6`

**Explanation:**

* Maximum OR = `7`
* Subsets with OR = 7:
  `[3,5]`, `[3,1,5]`, `[3,2,5]`, `[3,2,1,5]`, `[2,5]`, `[2,1,5]`

---

## 🧠 Approach

1. **Compute the target OR** by taking bitwise OR of all elements.
2. Use **DFS/backtracking** to explore all subsets.
3. Maintain a counter of subsets whose OR equals the target.

Since `nums.length ≤ 16`, it's efficient enough to try all possible subsets (at most `2^16 = 65536`).

---

## 💻 Code

![Code Image](image.png)

---

## ⏱️ Time & Space Complexity

| Type     | Complexity               |
| -------- | ------------------------ |
| 🕒 Time  | `O(2^n)`                 |
| 🧠 Space | `O(n)` (recursion stack) |

Where `n = nums.length`

---

## 📚 Constraints

* `1 <= nums.length <= 16`
* `1 <= nums[i] <= 10^5`

---

## 🔗 Related Topics

* Bit Manipulation
* Recursion
* Backtracking
* Subsets / Combinatorics

---
