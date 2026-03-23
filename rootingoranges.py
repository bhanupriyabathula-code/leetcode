from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        q = []
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh += 1

        while q:
            row, col, x = q.pop(0)
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c, x + 1))
                    res = max(res, x + 1)

        if fresh == 0:
            return res
        else:
            return -1
                


          


        
