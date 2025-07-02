class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)

        cnt = 1
        total = 1
        seg = []

        for i in range(1, n):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                total = (total * cnt) % MOD
                seg.append(cnt - 1)
                cnt = 1

        # Add the last segment
        total = (total * cnt) % MOD
        seg.append(cnt - 1)

        mnlen = len(seg)
        if k <= mnlen:
            return total

        k -= mnlen

        dp = [0] * k
        dp[0] = 1

        for x in seg:
            pref = [0] * k
            pref[0] = dp[0]
            for i in range(1, k):
                pref[i] = (pref[i - 1] + dp[i]) % MOD

            for i in range(k):
                if i - x - 1 >= 0:
                    dp[i] = (pref[i] - pref[i - x - 1] + MOD) % MOD
                else:
                    dp[i] = pref[i]

        invalid = sum(dp) % MOD
        return (total - invalid + MOD) % MOD
