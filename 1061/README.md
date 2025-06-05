# 1061. Lexicographically Smallest Equivalent String

## Problem Statement

You are given two strings of the same length `s1` and `s2` that define equivalence between characters. You're also given a string `baseStr`.

We define characters `s1[i]` and `s2[i]` as equivalent, and equivalence is transitive, symmetric, and reflexive.

Your task is to return the lexicographically smallest equivalent string of `baseStr` by using the equivalence information from `s1` and `s2`.

---

## Examples

### Example 1

**Input:**

```
s1 = "parker"
s2 = "morris"
baseStr = "parser"
```

**Output:**

```
makkek
```

**Explanation:**
Groups of equivalency: \[m,p], \[a,o], \[k,r,s], \[e,i]. The smallest in each group is used for the transformation.

### Example 2

**Input:**

```
s1 = "hello"
s2 = "world"
baseStr = "hold"
```

**Output:**

```
hdld
```

**Explanation:**
Groups: \[h,w], \[d,e,o], \[l,r]. The result is "hdld" using smallest lexicographical values in each group.

### Example 3

**Input:**

```
s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
```

**Output:**

```
aauaaaaada
```

---

## Constraints

* 1 <= s1.length, s2.length, baseStr.length <= 1000
* s1.length == s2.length
* All characters are lowercase English letters.

---

## Approach

* Build groups of equivalent characters using Union-Find (Disjoint Set Union) or dictionary-based merging.
* For each group, identify the lexicographically smallest character.
* Replace each character in `baseStr` with the smallest character from its equivalence group.

---

## Code (Python)

```python
from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        di = defaultdict(set)
        charmap = defaultdict(str)
        res = ''
        smallestMap = defaultdict(str)
        for i in range(len(s1)):
            u,v = s1[i],s2[i]
            if u==v:
                continue
            if v in charmap and u in charmap:
                grp_u ,grp_v = charmap[u], charmap[v]
                if grp_u==grp_v:
                    continue
                newMap = di[charmap[u]] | di[charmap[v]] | {u,v}
                new_leader = min(grp_u,grp_v)
                del di[grp_u]
                del di[grp_v]
                for c in newMap:
                    charmap[c] = new_leader
                di[new_leader] = newMap
            elif u in charmap:
                di[charmap[u]].add(v)
                charmap[v] = charmap[u]
            elif v in charmap:
                di[charmap[v]].add(u)
                charmap[u] = charmap[v]
            else:
                u,v = sorted([u,v])
                di[u] = {u,v}
                charmap[v] = u
                charmap[u] = u
        for i in charmap:
            di[charmap[i]].add(i)
        for i in di.keys():
            mi = min(di[i])
            for c in di[i]:
                smallestMap[c] = mi
        for i in baseStr:
            if i in smallestMap:
                res+=smallestMap[i]
            else:
                res+=i
        return res
```

---

## Complexity

* **Time Complexity:** O(N \* log N), where N is the length of `s1`/`s2` due to union operations and sorting during merges.
* **Space Complexity:** O(1) since we're dealing with only 26 lowercase characters.

---

## Tags

`String`, `Union Find`, `Graph`, `Greedy`

---


