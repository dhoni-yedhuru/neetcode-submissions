class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(range(len(nums) + 1))
        missing_val = sum(nums)
        return total_sum - missing_val
        