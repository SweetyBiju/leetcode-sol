# Permutations

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:**   
**Memory:**   
**LeetCode Link:** https://leetcode.com/problems/permutations/

## Explanation

The solution uses a recursive backtracking algorithm to generate all possible permutations in-place. At each step index `start`, we iterate through all elements from index `start` to the end of the array, swapping each element into position `start` and recursively building the rest of the permutation. Once `start` reaches the length of `nums`, a complete permutation is formed, so a copy of the array is added to the result list.
