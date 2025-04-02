

## Problem Statement
You are given a **0-indexed integer array** `nums`.

Return the **maximum value** over all triplets of indices `(i, j, k)` such that `i < j < k`. If all such triplets have a negative value, return `0`.

The value of a triplet of indices `(i, j, k)` is calculated as:
```
(nums[i] - nums[j]) * nums[k]
```

### **Example 1**
**Input:**
```python
nums = [12,6,1,2,7]
```
**Output:**
```python
77
```
**Explanation:**
The value of the triplet `(0, 2, 4)` is `(nums[0] - nums[2]) * nums[4] = (12 - 1) * 7 = 77`.
It can be shown that there are no ordered triplets of indices with a value greater than `77`.

### **Example 2**
**Input:**
```python
nums = [1,10,3,4,19]
```
**Output:**
```python
133
```
**Explanation:**
The value of the triplet `(1, 2, 4)` is `(nums[1] - nums[2]) * nums[4] = (10 - 3) * 19 = 133`.

### **Example 3**
**Input:**
```python
nums = [1,2,3]
```
**Output:**
```python
0
```
**Explanation:**
The only ordered triplet `(0, 1, 2)` has a negative value `(1 - 2) * 3 = -3`, so the answer is `0`.

---
## **Solution Approach**
### **Brute Force Approach (O(n³))**
We iterate through all possible triplets `(i, j, k)` where `i < j < k` and compute their values. We keep track of the maximum value found.

### **Code Implementation**
```python
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        
        return res
```

### **Explanation of Code**
1. **Initialize `res = 0`** to store the maximum triplet value found.
2. **Use three nested loops** to generate all valid `(i, j, k)` triplets where `i < j < k`.
3. **Compute the triplet value** using `(nums[i] - nums[j]) * nums[k]` and update `res` if the value is greater.
4. **Return `res`**, ensuring that if all triplets result in negative values, the function returns `0`.

### **Time Complexity Analysis**
- The brute-force approach involves three nested loops, iterating over `n` elements.
- The worst-case time complexity is **O(n³)**, where `n ≤ 100`, making it feasible for small constraints.

---
## **Optimized Approach (O(n)) - Not Implemented Here**
A more efficient approach could involve precomputing values to reduce redundant calculations, but the brute force method is sufficient given the constraints.

---
## **Conclusion**
- The **brute-force solution works well** for `n ≤ 100`.
- Future improvements can reduce the time complexity to **O(n²) or O(n)** using **prefix/suffix arrays**.

This approach successfully finds the maximum ordered triplet value efficiently within the given constraints. 🚀

