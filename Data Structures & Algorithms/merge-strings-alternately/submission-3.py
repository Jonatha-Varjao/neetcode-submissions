class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""

        
        l_size = min(len(word1), len(word2))

        i=0
        
        while i < l_size:
            new_word += word1[i]
            new_word += word2[i]

            i+=1

        if len(word2) > len(word1):
            new_word += word2[i:]
        else:
            new_word += word1[i:]
        

        return new_word