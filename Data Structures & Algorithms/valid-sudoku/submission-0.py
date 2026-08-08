class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=[]
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in seen:
                        return False
                    seen.append(board[i][j])
        for m in range(9):
            seen=[]
            for n in range(9):
                if board[n][m]!=".":
                    if board[n][m] in seen:
                        return False
                    seen.append(board[n][m])
        for w in range(9):
            x=(w%3)*3
            y=(w//3)*3
            box=[]
            for z in range(9):
                cell=board[y+(z//3)][x+(z%3)]
                if cell!=".":
                    if cell in box:
                        return False
                    box.append(cell)
        return True