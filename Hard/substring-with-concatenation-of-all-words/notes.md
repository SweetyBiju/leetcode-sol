# Substring with Concatenation of All Words

**Difficulty:** Hard  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 26
ms  
**Memory:** 19.97
MB  
**LeetCode Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Explanation

We use a sliding window approach with `word_len` different offset iterations (from `0` to `word_len - 1`) to ensure all possible alignments are covered. For each offset, we expand the right boundary of the window by `word_len` steps at a time, tracking word counts using a frequency map; if a word exceeds its expected frequency or is invalid, we shrink or reset the window from the left. This allows us to process the string in $O(N \cdot L)$ time complexity, where $N$ is the length of `s` and $L$ is the length of a word.
