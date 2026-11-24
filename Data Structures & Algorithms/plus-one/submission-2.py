class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIndex = len(digits)-1
        i = 0

        if (digits[lastIndex] == 9):
            for value in digits[::-1]:
                if value == 9:
                    digits[lastIndex - i] = 0
                    i += 1
                else:
                    break
            
            if digits[0] == 0:
                return [1] + digits
            else:
                digits[lastIndex - i] += 1
                return digits

        else:
            digits[lastIndex] += 1  
            return digits



""" Best Answer
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
        if carry == 1:
            return [1] + digits
        else:
            return digits

"""
        
        

        