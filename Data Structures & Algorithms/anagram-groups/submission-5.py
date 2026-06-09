class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        
        for word in strs:
            frequency_array = [0]*26
            for char in word:
                frequency_array[ ord(char) - ord("a") ] += 1 
            result_dict.setdefault(tuple(frequency_array), []).append(word)
        
        return list(result_dict.values())