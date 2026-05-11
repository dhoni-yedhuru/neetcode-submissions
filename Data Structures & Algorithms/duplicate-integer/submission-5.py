class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dici = {}
        for num in nums:
            if num not in dici:
                dici[num] = 1
            else:
                dici[num] += 1

        for key,value in dici.items():
            if value > 1:
                return True
        return False
        