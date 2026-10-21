class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # this is 
    
        # Brute Force
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1):
                    # max permimeter that can be added
                    perimeter += 4
                
                # however if it has an ajacent land block it reduces perimeter due to shared edge
                    if (r > 0 and grid[r - 1][c] == 1):
                        # removing 2 not 1 cuz shared both of them now have a shared edge so of the 4 edges both added 2 of them are invalid (double counted)
                        perimeter -= 2
                    if (c > 0 and grid[r][c - 1] == 1):
                        perimeter -=2
        
        return perimeter
        