class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each number in its correct index if possible (i.e., num x at index x - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Find the first index where the number is not equal to index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1