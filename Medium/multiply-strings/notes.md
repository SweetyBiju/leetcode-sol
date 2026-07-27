# Multiply Strings

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:**   
**Memory:**   
**LeetCode Link:** https://leetcode.com/problems/multiply-strings/

## Explanation

The approach mimics traditional elementary school multiplication using an array of size `m + n` to store the intermediate sums, where `m` and `n` are the lengths of `num1` and `num2` respectively. We iterate through both strings backwards, multiplying digits at indices `i` and `j` and placing the result into positions `i + j` (carry) and `i + j + 1` (units) in the result array. Finally, we strip any leading zeros from the result array and concatenate the digits into the final answer string.
