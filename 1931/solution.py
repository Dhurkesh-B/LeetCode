class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        from itertools import product

        # Step 1: Generate all valid column colorings
        def is_valid(col):
            for i in range(1, len(col)):
                if col[i] == col[i-1]:
                    return False
            return True

        colors = [0, 1, 2]  # 0 = Red, 1 = Green, 2 = Blue
        valid_cols = []
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        # Step 2: Build compatibility map between column colorings
        def are_compatible(c1, c2):
            for x, y in zip(c1, c2):
                if x == y:
                    return False
            return True

        transitions = {}
        for i, c1 in enumerate(valid_cols):
            transitions[i] = []
            for j, c2 in enumerate(valid_cols):
                if are_compatible(c1, c2):
                    transitions[i].append(j)

        # Step 3: DP
        dp = [1] * len(valid_cols)
        for _ in range(1, n):
            new_dp = [0] * len(valid_cols)
            for i in range(len(valid_cols)):
                for j in transitions[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD

