# Permutations II

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:**   
**Memory:**   
**LeetCode Link:** https://leetcode.com/problems/permutations-ii/

## Explanation

The solution uses backtracking with a frequency count map (`collections.Counter`) to handle duplicates efficiently. By iterating over the unique keys of the frequency map rather than the original list with duplicate values, we ensure that duplicate permutations are never generated. At each step of the recursion, we append an available number to the current permutation, recursively build the rest of the permutation, and then backtrack by restoring the number's count and popping it from the path.
