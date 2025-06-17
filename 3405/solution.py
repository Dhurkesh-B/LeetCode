MOD = 10**9 + 7
MAX = 10**5 + 5

# Precompute factorials and inverses
fact = [1] * MAX
inv_fact = [1] * MAX
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MAX-1] = pow(fact[MAX-1], MOD - 2, MOD)
for i in range(MAX-2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, k):
    if k < 0 or k > n: return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        ways = comb(n - 1, k)
        ways = ways * m % MOD
        ways = ways * pow(m - 1, n - k - 1, MOD) % MOD
        return ways
