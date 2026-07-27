# Set Matrix Zeroes

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/set-matrix-zeroes/

## Explanation

To achieve $O(1)$ additional space complexity, we use the matrix's first row and first column as markers to record which rows and columns should be zeroed out. Since the first row and column overlap at `matrix[0][0]`, we use two separate boolean variables to track whether the original first row and column contain any zeroes. After marking the zero locations and updating the inner submatrix, we handle the first row and column based on the initial boolean flags.
