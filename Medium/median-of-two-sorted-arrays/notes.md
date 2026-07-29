# Median Of Two Sorted Arrays

**Difficulty:** Medium  
**Language:** python3  
**Date Solved:** 2026-07-29  
**Runtime:** 0 ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Explanation

The approach uses binary search on the smaller array (`nums1`) to partition both arrays into left and right halves such that the total number of elements in the left partition equals the total number in the right partition (or one extra for odd total length). We adjust the partition index `i` in `nums1` (and corresponding index `j` in `nums2`) until all elements in the left partition are less than or equal to all elements in the right partition. Once a valid partition is found, the median is calculated directly using the maximum of the left elements and the minimum of the right elements, achieving $O(\log(\min(m, n)))$ time complexity.
