class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def cal_steps(n, curr, next):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return steps

        curr = 1
        k -= 1  # we already consider '1' as first

        while k > 0:
            steps = cal_steps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
