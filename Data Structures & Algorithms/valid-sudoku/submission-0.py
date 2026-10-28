class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if len(board) == 1 and len(board[0]) == 1:
            return True 

        #Create the sets to check the numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrid = [set() for _ in range(9)]

        r = len(board)
        c = len(board[0])

        for row in range(r):
            for column in range(c):
                if board[row][column] == ".":
                    pass
                elif board[row][column] in rows[row]:
                    return False
                elif board[row][column] in cols[column]:
                    return False
                elif board[row][column] in subgrid[(row//3) *3 + (column//3)]:
                    return False   
                else: 
                    rows[row].add(board[row][column])
                    cols[column].add(board[row][column])
                    subgrid[(row//3) *3 + (column//3)].add(board[row][column])
        return True
