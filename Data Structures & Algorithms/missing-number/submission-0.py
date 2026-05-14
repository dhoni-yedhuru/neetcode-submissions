class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        for num in range(0 ,len(nums) + 1):
            count += num
        result = count - total
        return result
    

        