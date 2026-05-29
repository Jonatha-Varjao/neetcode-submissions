class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l_p = 0 
        r_p = len(cleaned) -1
        print(s,cleaned)
        while l_p<=r_p:
            if cleaned[l_p] != cleaned[r_p]:
                return False
            l_p += 1
            r_p -= 1

        return True