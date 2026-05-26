

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_set = sorted(s)
        t_set = sorted(t)
        if s_set == t_set:
            return True

        return False