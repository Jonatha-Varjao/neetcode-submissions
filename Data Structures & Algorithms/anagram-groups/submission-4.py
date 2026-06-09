class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string
        
        result_dict = {}
        
        frequency_array = [0]*26
        
        for word in strs:
            for char in word:
                frequency_array[ ord(char) - ord("a") ] += 1 
            result_dict[tuple(frequency_array)] = result_dict.get(tuple(frequency_array), []) + [word]
            frequency_array = [0]*26

        result = []
        for words in result_dict.values(): 
            result.append( [ word for word in words ] )
        
        return result