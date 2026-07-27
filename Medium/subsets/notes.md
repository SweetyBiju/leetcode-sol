# Subsets

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 1
ms  
**Memory:** 19.32
MB  
**LeetCode Link:** https://leetcode.com/problems/subsets/

## Explanation

We use an iterative cascading approach to generate the power set. Starting with an empty set `[[]]`, for each number in `nums`, we iterate through all previously created subsets and create new ones by appending the current number to each. This naturally guarantees that all $2^N$ unique combinations are generated without duplicates.
