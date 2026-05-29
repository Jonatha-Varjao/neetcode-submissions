from collections import Counter
class Solution:

    def isPalindrome(self, s: str)->bool:
        l_p,r_p = 0,len(s)-1
        
        
        while l_p <= r_p:
            if s[l_p] != s[r_p]:
                return False
            l_p+=1
            r_p-=1
        return True


    def validPalindrome(self, s: str) -> bool:
        import re

        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l_p,r_p = 0,len(cleaned)-1
        
        
        while l_p <= r_p:
            if cleaned[l_p] != cleaned[r_p]:
                left_skip = cleaned.replace(cleaned[l_p], '')
                right_skip = cleaned.replace(cleaned[r_p], '')
                return self.isPalindrome(left_skip) or self.isPalindrome(right_skip)              

            
            l_p+=1
            r_p-=1

        return True