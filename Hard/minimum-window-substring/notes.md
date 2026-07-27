# Minimum Window Substring

**Difficulty:** Hard  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/minimum-window-substring/

## Explanation

The solution uses a two-pointer sliding window approach to efficiently find the minimum window substring. We expand the `right` pointer to include characters in the current window until all characters from `t` (including duplicates) are matched, which we track using character frequency counts and a `formed` variable. Once a valid window is found, we shrink it from the `left` pointer to minimize its length while maintaining the required character counts, updating our result whenever a smaller valid window is identified.
