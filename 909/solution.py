from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board#Convert 2D board into a 1D list while following Boustrophedon order
        def get_board_index(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (cell number, steps)

        while queue:
            cell, steps = queue.popleft()
            if cell == n * n:
                return steps

            for i in range(1, 7):
                next_cell = cell + i
                if next_cell > n * n:
                    continue
                r, c = get_board_index(next_cell)
                if board[r][c] != -1:
                    next_cell = board[r][c]
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, steps + 1))

        return -1
