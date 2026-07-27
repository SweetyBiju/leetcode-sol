# Wildcard Matching

**Difficulty:** Hard  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:**   
**Memory:**   
**LeetCode Link:** https://leetcode.com/problems/wildcard-matching/

## Explanation

The solution uses a two-pointer approach with backtracking to efficiently match the string `s` against the pattern `p`. When a wildcard `'*'` is encountered, its position and the current string index are saved as checkpoint references. If a mismatch occurs later, the algorithm backtracks to the last saved `'*'` position, advances the string checkpoint by one character (effectively letting `'*'` match one more character), and continues matching from there.
