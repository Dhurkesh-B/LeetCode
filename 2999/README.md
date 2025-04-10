# 2999. Count the Number of Powerful Integers

## Problem Statement

You are given three integers `start`, `finish`, and `limit`, along with a 0-indexed string `s` representing a positive integer.

A **positive integer `x`** is called **powerful** if:

1. It ends with `s` (i.e., `s` is a suffix of `x`).
2. Each digit in `x` is less than or equal to `limit`.

Return the total number of powerful integers within the range `[start..finish]` (inclusive).

### Definitions
- A string `x` is a suffix of a string `y` if it starts at some index in `y` and continues to the end.

---

## Examples

### Example 1:
**Input:**
```
start = 1, finish = 6000, limit = 4, s = "124"
```
**Output:**
```
5
```
**Explanation:**
Valid powerful integers: `124, 1124, 2124, 3124, 4124`

### Example 2:
**Input:**
```
start = 15, finish = 215, limit = 6, s = "10"
```
**Output:**
```
2
```
**Explanation:**
Valid powerful integers: `110, 210`

### Example 3:
**Input:**
```
start = 1000, finish = 2000, limit = 4, s = "3000"
```
**Output:**
```
0
```
**Explanation:**
All numbers in range are smaller than `3000`, hence no match.

---

## Constraints

- `1 <= start <= finish <= 10^15`
- `1 <= limit <= 9`
- `1 <= s.length <= floor(log10(finish)) + 1`
- `s` consists of numeric digits only, each digit <= `limit`
- `s` has no leading zeros

---

## Approach

We solve this using **Digit Dynamic Programming (Digit DP)** to efficiently count numbers:

1. **Key Observations:**
   - All digits must be `<= limit`
   - Number must end with suffix `s`

2. **Steps:**
   - Define a recursive function that tries all possible digits up to the length of `finish`.
   - Ensure valid digits `<= limit`
   - Check that suffix matches only at appropriate positions.
   - Use memoization (`cache`) to avoid recomputation.

---

## Code

📎 See `image.png` for the full implementation.

---

## Complexity Analysis

- **Time Complexity:** Efficient for numbers up to `10^15` due to memoized recursion on digits
- **Space Complexity:** Depends on number of unique digit-position states cached

---

🧠 **Insight:** This is a classic Digit DP problem that blends constraints on value limits and string suffix matching for massive number ranges.

