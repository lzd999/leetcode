"""
思路：

"""

from typing import List


class Solution79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if not 0 <= r < m or not 0 <= c < n or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            board[r][c] = ""
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = word[i]
            return res

        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
