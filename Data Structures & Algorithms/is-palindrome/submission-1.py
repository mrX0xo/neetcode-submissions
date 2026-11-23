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

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_pal = ''.join(st.lower() for st in s if st.isalnum())
        left = 0
        right = len(s_pal) - 1

        while left <= right:
            if s_pal[left] == s_pal[right]:
                left+=1
                right-=1
            else:
                return False
        return True
"""
        
        