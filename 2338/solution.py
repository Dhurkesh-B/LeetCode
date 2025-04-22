class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from math import comb
        MOD = 10**9 + 7
        max_len = 14  

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb_mod(n, k):
            if k > n or k < 0:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        dp = [[0] * (max_len + 1) for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1

        for length in range(2, max_len + 1):
            for i in range(1, maxValue + 1):
                for j in range(2 * i, maxValue + 1, i):
                    dp[j][length] = (dp[j][length] + dp[i][length - 1]) % MOD

        res = 0
        for val in range(1, maxValue + 1):
            for length in range(1, max_len + 1):
                count = dp[val][length]
                ways = comb_mod(n - 1, length - 1)
                res = (res + count * ways) % MOD

        return res
