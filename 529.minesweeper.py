#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i = click[0]
        j = click[1]
        m = len(board)
        n = len(board[0])

        d = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        if (board[i][j] == "M"):
            board[i][j] = "X"
        else:
            queue = [(i, j)]
            while len(queue) > 0:
                x, y = queue.pop(0)
                if board[x][y] != "E":
                    continue

                mines = 0

                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if (board[nx][ny] == "M"):
                        mines += 1

                if mines == 0:
                    board[x][y] = "B"
                    for dx, dy in d:
                        nx = x + dx
                        ny = y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        queue.append((nx, ny))

                else:
                    board[x][y] = str(mines)
        return board

        # O(m * n)
# @lc code=end
