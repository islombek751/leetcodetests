#https://leetcode.com/problems/valid-sudoku/
class Solution:

    @staticmethod
    def reverse(board):
        r = []
        for i in range(9):
            subr = []
            for j in range(9):
                subr.append(board[j][i])
            r.append(subr)
        return r
    @staticmethod
    def check_row(board):
        for i in range(9):
            row = []
            for subrow in board[i]:
                if subrow in row and subrow != ".":
                    return False
                else:
                    row.append(subrow)
        return True
    @classmethod
    def isValidSudoku(cls, board):
        result1 = cls.check_row(board)
        reversed_board = cls.reverse(board)
        result2 = cls.check_row(reversed_board)
        return result1 and result2

print(
    Solution.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )
)