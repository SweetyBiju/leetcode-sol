# Reverse Nodes in k-Group

**Difficulty:** Hard  
**Language:** python3  
**Date Solved:** 2026-07-27  
**Runtime:** 0
ms  
**Memory:** 0.00
MB  
**LeetCode Link:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Explanation

We use a dummy node pointing to the head of the list to easily manage updates to the head pointer, along with a `groupPrev` pointer that keeps track of the node preceding the current $k$-group. In each iteration, a helper function `getKth` identifies the $k$-th node from `groupPrev`; if fewer than $k$ nodes remain, the loop terminates to leave the tail unchanged. Otherwise, we reverse the $k$ nodes in-place by updating node pointers, connect `groupPrev` to the newly reversed segment head, and update `groupPrev` for the next group.
