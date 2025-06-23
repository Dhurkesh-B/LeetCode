class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num, k):
            result = []
            while num > 0:
                result.append(str(num % k))
                num //= k
            return ''.join(reversed(result))

        def generate_palindromes():
            length = 1
            while True:
                half = 10 ** ((length - 1) // 2)
                for i in range(half, 10 ** ((length + 1) // 2)):
                    s = str(i)
                    if length % 2 == 0:
                        pal = int(s + s[::-1])
                    else:
                        pal = int(s + s[-2::-1])
                    yield pal
                length += 1

        ans = 0
        count = 0
        for num in generate_palindromes():
            base_k_str = to_base_k(num, k)
            if is_palindrome(base_k_str):
                ans += num
                count += 1
                if count == n:
                    break
        return ans
