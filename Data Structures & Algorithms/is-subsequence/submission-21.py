class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_pointer = 0
        t_pointer = 0

        if s == "":
            return True
        if t == "":
            return False
        
        while s_pointer < len(s) and t_pointer < len(t) :
            
            if s[s_pointer] == t[t_pointer]:
                s_pointer+=1    
            
            t_pointer+=1
        print(s_pointer, len(s))
        return True if s_pointer == len(s) else False
                


        