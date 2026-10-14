class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row sorted ASC
        # first int in each row greater than last of las row 
        # so full ascending

        # decide which rows to search based on where target falls in relation
        if (matrix[0][0] > target):
            return False
        row = 0 # the row to search
        # find row to search
        for r in range(len(matrix)): 
            if (matrix[r][0] == target): 
                return True
            elif (matrix[r][0] < target):
                row = r
        
        # we have the row that contains target most likely
        last_ele = len(matrix[row]) - 1
        if (matrix[row][last_ele] == target):
            return True
        elif (matrix[row][last_ele] < target):
            return False
        else: 
            for num in matrix[row]: 
                if (num == target):
                    return True

        return False # is impossible for target to be in any row
        