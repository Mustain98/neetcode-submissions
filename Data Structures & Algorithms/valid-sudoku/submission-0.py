class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if (not self.checkRow(i, j, board[i][j], board) or
                    not self.checkCol(i, j, board[i][j], board) or
                    not self.checkSubBox(i, j, board[i][j], board)):
                    return False
                

        return True

    def checkRow(self,row:int,col:int,num:str,board: List[List[str]])->bool:
        for i in range(9):
            if i != row and board[i][col]==num:
                return False
        return True
                
    def checkCol(self,row:int,col:int,num:str,board:List[List[str]])->bool:
        for i in range(9):
            if i != col and board[row][i]==num:
                return False
        return True
    def checkSubBox(self, row: int, col: int, num: str, board: List[List[str]]) -> bool:
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if (i != row or j != col) and board[i][j] == num:
                    return False

        return True
