"""
思路：
N 皇后最直观的做法是遍历每一行，先放置一个皇后，然后判断是否与其它行的皇后存在冲突，若存在冲突则重新选择上一行皇后的放置位置。
可以看出，N 皇后问题属于排列型回溯
定义 cols 数组记录被放置皇后的列，on_path 数组记录皇后间是否存在列冲突，diag_main 和 diag_sub 数组记录是否皇后间是否存在主对角线和副对角线冲突。
遍历每一行，对当前行的每一列判断当前皇后与已放置皇后是否存在列冲突、主对角线冲突和副对角线冲突，如果都不存在才能放置；
当所有行遍历完后，说明当前放置路径可行，加入答案
"""

from typing import List


class Solution51:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(r):
            if r == n:
                path = []
                for c in cols:
                    row = ["."] * n
                    row[c] = "Q"
                    path.append("".join(row))
                ans.append(path)
                return
            for c in range(n):
                dm, ds = r + c, r - c
                if not on_path[c] and not diag_main[dm] and not diag_sub[ds]:
                    cols[r] = c
                    on_path[c] = diag_main[dm] = diag_sub[ds] = True
                    dfs(r + 1)
                    on_path[c] = diag_main[dm] = diag_sub[ds] = False

        ans = []
        cols = [0] * n
        on_path = [False] * n
        m = 2 * n - 1
        diag_main, diag_sub = [False] * m, [False] * m
        dfs(0)
        return ans
