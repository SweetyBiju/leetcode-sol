from collections import Counter
from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in counts:
                if counts[num] > 0:
                    counts[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counts[num] += 1

        backtrack([])
        return res