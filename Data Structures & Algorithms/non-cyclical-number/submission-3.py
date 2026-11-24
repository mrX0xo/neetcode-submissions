class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        

        def findOut(i):
            calculate = 0

            for value in str(i):
                calculate = (int(value) * int(value)) + calculate
            
            if calculate == 1:
                return True
            else:
                if calculate in seen:
                    return False
                else:
                    seen.add(calculate)
                    return findOut(calculate)
        
        return findOut(n)
            
        