import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', "".join(s.split()).lower())

        while(len(cleaned)/2 > i):
            if cleaned[i] != cleaned[len(cleaned)-1-i]:
                return False
            i += 1
        return True
        
        