# 36. Valid Sudoku

## 🔗 Problem

Given a `9 × 9` Sudoku board, determine whether the current board is valid.

A valid Sudoku board must satisfy the following rules:

1. Each row must not contain duplicate digits from `1-9`.
2. Each column must not contain duplicate digits from `1-9`.
3. Each `3 × 3` sub-box must not contain duplicate digits from `1-9`.

Empty cells are represented by `"."` and should be ignored.

The board does not need to be complete or solvable. We only need to check whether its current state is valid.

---

## Example 1

```text
Input:

board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output:

true
```

Explanation:

There are no duplicate digits in any row, column, or `3 × 3` sub-box.

Therefore, the board is valid.

---

## Example 2

```text
Input:

board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output:

false
```

Explanation:

The top-left `3 × 3` sub-box contains two `1`s.

Therefore, the board is invalid.

---

## Difficulty

Medium

---

## Topics

- Array
- Hash Set
- Matrix

---

## Approach

This solution uses **Hash Sets** to track the digits that have already appeared in each:

- Row
- Column
- `3 × 3` sub-box

While traversing the board, every non-empty cell is checked against all three sets.

If the value already exists in any of them, the board is invalid.

---

### Step 1 — Create Row Sets

Create nine sets, one for each row.

```python
rows = [set() for _ in range(9)]
```

For example:

```text
rows[0] → digits seen in row 0
rows[1] → digits seen in row 1
...
```

---

### Step 2 — Create Column Sets

Create nine sets for the columns.

```python
cols = [set() for _ in range(9)]
```

For example:

```text
cols[0] → digits seen in column 0
cols[1] → digits seen in column 1
...
```

---

### Step 3 — Create Sub-box Sets

Create nine sets for the `3 × 3` sub-boxes.

```python
squares = [set() for _ in range(9)]
```

The boxes are indexed as:

```text
0 1 2
3 4 5
6 7 8
```

---

### Step 4 — Traverse the Board

Visit every cell using its row and column indices.

```python
for r in range(9):
    for c in range(9):
```

Ignore empty cells:

```python
if board[r][c] == ".":
    continue
```

---

### Step 5 — Find the Sub-box

The `3 × 3` box containing `(r, c)` can be calculated with:

```python
square_index = (r // 3) * 3 + (c // 3)
```

For example:

```text
(r, c) = (4, 7)

r // 3 = 1
c // 3 = 2

square_index = 1 × 3 + 2
             = 5
```

Therefore, this cell belongs to sub-box `5`.

---

### Step 6 — Check for Duplicates

Check whether the current value has already appeared in its row, column, or box.

```python
if (
    value in rows[r]
    or value in cols[c]
    or value in squares[square_index]
):
    return False
```

---

### Step 7 — Store the Value

If no duplicate exists, add the value to all three sets.

```python
rows[r].add(value)
cols[c].add(value)
squares[square_index].add(value)
```

If every cell is processed successfully, return:

```python
True
```

---

## Alternative Solutions

### 1. Check Rows, Columns, and Boxes Separately

Perform separate passes over:

- All rows
- All columns
- All `3 × 3` boxes

This works, but requires multiple validation passes and more repeated logic.

---

### 2. Single Set with Encoded Keys

Another approach is to store unique representations such as:

```text
("row", row, value)
("column", column, value)
("box", box, value)
```

inside one Hash Set.

If a representation already exists, a duplicate has been found.

This is compact but can be less intuitive.

---

### 3. Separate Hash Sets ✅

Maintain separate sets for rows, columns, and boxes.

Each cell can then be validated during a single traversal of the board.

This approach is efficient and easy to understand.

---

## Solution

```python
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                square_index = (r // 3) * 3 + (c // 3)

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[square_index]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[square_index].add(value)

        return True
```

---

## Dry Run

Consider part of the invalid board:

```text
1 2 .
4 . .
. 9 1
```

The first `1` is added to the top-left box:

```text
squares[0] = {"1"}
```

Later, the second `1` is encountered in the same box.

The algorithm checks:

```text
"1" in squares[0]
```

Result:

```text
True
```

A duplicate exists, so:

```python
return False
```

---

## Key Idea

Each Sudoku cell belongs to exactly:

- One row
- One column
- One `3 × 3` box

Use a Hash Set for each of these groups.

Before inserting a digit, check whether it already exists in any of its corresponding sets.

The key formula for mapping a cell to its box is:

```python
(r // 3) * 3 + (c // 3)
```

---

## Time Complexity

For a fixed `9 × 9` Sudoku board:

```text
O(1)
```

because exactly 81 cells are processed.

More generally, for an `n × n` board:

```text
O(n²)
```

Each cell is visited once, and Hash Set lookup/insertion is approximately `O(1)`.

---

## Space Complexity

For a fixed Sudoku board:

```text
O(1)
```

The number of possible stored digits is bounded by the fixed `9 × 9` board size.

For a generalized `n × n` board, the auxiliary storage grows with the board structure.

---

## What I Learned

- How Hash Sets can efficiently detect duplicates.
- How to traverse a two-dimensional matrix.
- How to validate multiple constraints during a single traversal.
- How to map `(row, column)` coordinates to a `3 × 3` sub-box.
- Why integer division (`//`) is useful for grouping matrix coordinates.
- How Sudoku validation differs from actually solving a Sudoku puzzle.