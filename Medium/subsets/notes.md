# Subsets

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/subsets/

## Explanation

The approach builds the power set iteratively by starting with the empty set `[[]]`. For each number in `nums`, it generates new subsets by appending that number to all existing subsets in the result list and adding them back. This ensures that every combination is included without duplicates in $O(N \cdot 2^N)$ time complexity.
