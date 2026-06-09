class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string

        l_l = [[] for _ in strs]
        #array_26 = list(string.ascii_lowercase)
        
        sorted_str = [''.join(sorted(char)) for char in strs]

        result = []
        _set = set()
        for i in range(0, len(sorted_str)):
            if sorted_str[i] in _set:
                continue
            group = []
            _set.add(sorted_str[i])
            for j in range(i, len(sorted_str)):
                if sorted_str[i] == sorted_str[j]:
                    group.append(strs[j])
            result.append(group)
        return result
        