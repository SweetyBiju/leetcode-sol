# Search a 2D Matrix

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/search-a-2d-matrix/

## Explanation

Since each row is sorted and the first element of any row is greater than the last element of the previous row, the 2D matrix can be treated as a single sorted 1D array of size $m \times n$. We perform a standard binary search over the range $[0, m \times n - 1]$, mapping any 1D index `mid` to its corresponding 2D position `(mid // n, mid % n)`. This achieves the required $O(\log(m \cdot n))$ time complexity using $O(1)$ extra space.
