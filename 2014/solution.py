
from collections import deque, Counter

class Solution:
    def ifexists(self, s: str, p: str, k: int) -> bool:
        target = p * k
        j = 0
        for ch in s:
            if ch == target[j]:
                j += 1
                if j == len(target):
                    return True
        return j == len(target)

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for i in range(26):
            if freq[i] < k:
                freq[i] = 0
            else:
                freq[i] //= k

        q = deque([""])
        ans = ""

        while q:
            cur = q.popleft()
            n_freq = freq.copy()

            for ch in cur:
                n_freq[ord(ch) - ord('a')] -= 1

            for i in range(25, -1, -1):  # reverse for lexicographically larger
                if n_freq[i] == 0:
                    continue
                c = chr(i + ord('a'))
                temp = cur + c
                if self.ifexists(s, temp, k):
                    q.append(temp)
                    if len(temp) > len(ans) or (len(temp) == len(ans) and temp > ans):
                        ans = temp

        return ans
