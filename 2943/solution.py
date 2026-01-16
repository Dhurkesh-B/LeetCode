class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def longest_consecutive(arr):
            if not arr:
                return 1
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    best = max(best, cur)
                    cur = 1
            best = max(best, cur)
            return best + 1  # +1 because k consecutive removed bars => k+1 hole size

        maxRow = longest_consecutive(hBars)
        maxCol = longest_consecutive(vBars)

        side = min(maxRow, maxCol)
        return side * side
