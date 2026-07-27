# Combinations

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/combinations/

## Explanation

The problem asks for all possible combinations of $k$ numbers chosen from $1$ to $n$. Python's built-in `itertools.combinations` module efficiently generates all $k$-length combinations in lexicographical order. By iterating over `range(1, n + 1)` with `combinations` and casting each resulting tuple to a list, we obtain the required list of combinations.
