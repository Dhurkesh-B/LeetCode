# 1353. Maximum Number of Events That Can Be Attended

## Problem Statement

You are given an array of events where `events[i] = [startDayi, endDayi]`. Each event can be attended on any day between its `startDay` and `endDay`, inclusive.

You may attend **at most one event** per day. Return the **maximum** number of events you can attend.

---

## Examples

### Example 1:

**Input:**

```
events = [[1,2],[2,3],[3,4]]
```

**Output:**

```
3
```

**Explanation:**

* Attend the first event on day 1.
* Attend the second event on day 2.
* Attend the third event on day 3.
  All events are attended.

### Example 2:

**Input:**

```
events = [[1,2],[2,3],[3,4],[1,2]]
```

**Output:**

```
4
```

---

## Constraints

* `1 <= events.length <= 10^5`
* `events[i].length == 2`
* `1 <= startDayi <= endDayi <= 10^5`

---

## Approach

1. **Sort events** based on their start day.
2. Use a **min-heap** to keep track of the end days of the events that can be attended on a given day.
3. Iterate through each day from 1 to the latest possible end day.
4. For each day:

   * Add events starting today to the heap.

     Remove events from the heap that have already expired.
   * Attend the event with the earliest end date.
5. Continue until all days are processed or no more events can be attended.

This greedy algorithm ensures that we always prioritize events that end earlier, allowing room to attend more events later.

---

## Code Representation

---

## Summary

* Efficient solution using **greedy + priority queue**.
* Achieves optimal event attendance by choosing earliest finishing events first.
* Time complexity is approximately O(N log N) due to sorting and heap operations.

---
