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