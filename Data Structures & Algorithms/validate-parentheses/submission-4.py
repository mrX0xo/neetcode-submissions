class Solution:
    def isValid(self, s: str) -> bool:
        value = {'}':'{',')':'(', ']':'['}
        closed = [']',')','}']
        temp = list()
        i = 0 

        if len(s)%2 != 0:
            return False

        if s[0] in closed:
            return False
        
        if s[len(s)-1] not in closed:
            return False

        for i in range(len(s)):
            if s[i] not in closed:
                temp.append(s[i])
            else:
                if temp[len(temp)-1] == value[s[i]]:
                    temp.pop()
                else:
                    return False
        return temp == [] 


        