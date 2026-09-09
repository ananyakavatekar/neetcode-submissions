class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are only checking to see if the incomplete board doesn't break rules abt what nums can exist where

        # index of a num in board is board[row][col]
        # to check what num it is int(board[row][col]) have conditional to skip does with "." to prevent error

        row_set = defaultdict(set)
        col_set = defaultdict(set) 
        box_set = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (int(board[i][j]) in row_set[i]):
                    return False
                elif (int(board[i][j]) in col_set[j]):
                    return False
                elif (int(board[i][j]) in box_set[(int(i/3), int(j/3))]):
                    return False
                row_set[i].add(int(board[i][j]))
                col_set[j].add(int(board[i][j]))
                box_set[(int(i/3), int(j/3))].add(int(board[i][j]))
        return True