class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()

        for idx, value in enumerate(nums):
            if value in _set:
                return True
            
            _set.add(value)

        return False