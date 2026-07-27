# First Missing Positive

**Difficulty:** Hard  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:**   
**Memory:**   
**LeetCode Link:** https://leetcode.com/problems/first-missing-positive/

## Explanation

The problem requires finding the smallest missing positive integer, which must lie within the range $[1, n + 1]$ for an array of size $n$. We can achieve $O(n)$ time and $O(1)$ auxiliary space by using cyclic sort to place each valid integer $x$ (where $1 \le x \le n$) at index $x - 1$ in-place. After rearranging the array, a second pass identifies the first index `i` where `nums[i] != i + 1`, returning `i + 1`, or $n + 1$ if all positions from $1$ to $n$ are correctly filled.
