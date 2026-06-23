class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        rows = {}
        cols = {}

        for i in range(len(board)):
            for j in range(len(board[i])):

                if i not in rows:
                    rows[i] = set()

                if j not in cols:
                    cols[j] = set()

                if (i//3, j//3) not in boxes:
                    boxes[(i//3, j//3)] = set()

                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in boxes[(i//3, j//3)]
                ):
                    return False
                if board[i][j] != ".":
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    boxes[(i//3, j//3)].add(board[i][j])
        return True
                



                
