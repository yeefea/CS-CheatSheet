class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_valid_map = {}
        col_valid_map = {}
        box_valid_map = {}

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue
                if i in row_valid_map:
                    valid = row_valid_map[i]
                else:
                    valid = set()
                    row_valid_map[i] = valid
                if n in valid:
                    return False
                valid.add(n)

                if j in col_valid_map:
                    valid = col_valid_map[j]
                else:
                    valid = set()
                    col_valid_map[j] = valid
                if n in valid:
                    return False
                valid.add(n)

                ij = (int(i / 3), int(j / 3))
                if ij in box_valid_map:
                    valid = box_valid_map[ij]
                else:
                    valid = set()
                    box_valid_map[ij] = valid
                if n in valid:
                    return False
                valid.add(n)
        return True