# Set Matrix Zeroes

A Python implementation that converts an entire row and column to zero whenever an element in the matrix is zero.

## Overview

The program modifies the matrix in place. Instead of immediately clearing rows and columns when a zero is found, it first records the affected rows and columns using the matrix itself.

For each zero found away from the first row and first column, the corresponding first-column and first-row positions are marked as zero. These markers are then used during a second traversal to apply the required changes.

## How It Works

### 1. Handle the Matrix Dimensions

The program first determines the number of rows:

```python
rows = len(matrix)
```

An empty matrix is returned immediately:

```python
if rows == 0:
    return
```

The number of columns is then obtained from the first row.

### 2. Track the First Row and First Column

Two flags are used to remember whether the first row or first column originally contains a zero:

```python
first_row_zero = False
first_col_zero = False
```

The first row is checked separately:

```python
for col in range(cols):
    if matrix[0][col] == 0:
        first_row_zero = True
```

The first column is handled similarly.

### 3. Mark Affected Rows and Columns

The remaining matrix is scanned:

```python
for row in range(1, rows):
    for col in range(1, cols):
```

Whenever a zero is found, its row and column are marked:

```python
matrix[row][0] = 0
matrix[0][col] = 0
```

The first column therefore acts as a record of which rows need to be cleared, while the first row records which columns need to be cleared.

### 4. Apply the Markers

The matrix is scanned again, excluding the first row and column.

If either marker is zero, the current cell becomes zero:

```python
if matrix[row][0] == 0 or matrix[0][col] == 0:
    matrix[row][col] = 0
```



### 5. Restore the First Row and Column

Finally, the saved flags determine whether the first row or first column must be completely zeroed:

```python
if first_row_zero:
    for col in range(cols):
        matrix[0][col] = 0
```

The same process is applied to the first column.

## Example

The program starts with:

```text
1   2   0   4
5   6   7   8
9   0   11  12
13  14  15  16
```

There are zeros at:

- Row 1, Column 3
- Row 3, Column 2

Therefore, their complete rows and columns become zero.

The resulting matrix is:

```text
1   0   0   0
0   0   0   8
0   0   0   0
13  0   0   16
```

The sample matrix and function call are included in `main()`.

## Algorithm

1. Identify the matrix dimensions.
2. Record whether the first row contains zero.
3. Record whether the first column contains zero.
4. Use the first row and column as markers for other zero-containing rows and columns.
5. Apply the markers to the rest of the matrix.
6. Zero the first row if required.
7. Zero the first column if required.

## Complexity

| Metric | Complexity |
|---|---|
| Time | O(M × N) |
| Auxiliary Space | O(1) |

The matrix is traversed a constant number of times, and the implementation uses the matrix itself for row and column markers rather than creating separate tracking arrays.
