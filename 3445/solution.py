class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(cnt_a, cnt_b):
            return ((cnt_a % 2) << 1) | (cnt_b % 2)

        n = len(s)
        ans = float('-inf')

        for a in range(5):  # characters '0' to '4'
            for b in range(5):
                if a == b:
                    continue

                best = [float('inf')] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    cnt_a += (int(s[right]) == a)
                    cnt_b += (int(s[right]) == b)

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        prev_a += (int(s[left]) == a)
                        prev_b += (int(s[left]) == b)

                    right_status = get_status(cnt_a, cnt_b)
                    target_status = right_status ^ 0b10

                    if best[target_status] != float('inf'):
                        ans = max(ans, (cnt_a - cnt_b) - best[target_status])

        return -1 if ans == float('-inf') else ans
