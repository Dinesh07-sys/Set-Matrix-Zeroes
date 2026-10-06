class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows: int = len(matrix)
        if rows == 0:
            return

        cols: int = len(matrix[0])
        first_row_zero: bool = False
        first_col_zero: bool = False
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0
def print_row(row: list[int]) -> None:
    print(" ".join(str(value) for value in row))
def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print_row(row)
def main() -> None:
    matrix: list[list[int]] = [
        [1, 2, 0, 4],
        [5, 6, 7, 8],
        [9, 0, 11, 12],
        [13, 14, 15, 16],
    ]
    sol: Solution = Solution()
    sol.setZeroes(matrix)
    print_matrix(matrix)
if __name__ == "__main__":
    main()