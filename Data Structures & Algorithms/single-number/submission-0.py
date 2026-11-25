class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()

        for value in nums:
            if value in seen:
                seen[value] = seen[value] + 1
            else:
                seen[value] = 1 

        for key, value in seen.items():
            if value == 1:
                return key
           
            
        