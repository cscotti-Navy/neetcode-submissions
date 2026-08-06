class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = {r: set() for r in range(9)}
        col_seen = {c: set() for c in range(9)}
        box_seen = {(i,j): set() for i in range(3) for j in range(3)}
        

        for r, row in enumerate(board):
            for c, val in enumerate(row):
               
                b = (r//3, c//3)

                if val == ".":
                    continue  

                
                if val in row_seen[r] or val in col_seen[c] or val in box_seen[b]:
                    return False 
                else:
                    row_seen[r].add(val)
                    col_seen[c].add(val)
                    box_seen[b].add(val)

        return True 
        