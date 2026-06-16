class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_cp = ""
        
        referential = strs[0]

        for i in range(len(referential)):
            is_the_same = True
            
            for j in range(len(strs)):
                
                if i >= len(strs[j]):    
                    return longest_cp
                if referential[i] != strs[j][i]:
                    is_the_same = False
                    return longest_cp
        
            if is_the_same:
                longest_cp += referential[i]

        return longest_cp