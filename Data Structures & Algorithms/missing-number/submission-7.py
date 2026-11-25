class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return i + 1

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n

        for i in range(n):
            xorr ^= i ^ nums[i]

        return xorr
"""