class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contains = {}
        
        for idx,value in enumerate(nums):
            if value in contains and abs(contains[value]-idx) <= k:
                return True
                
            contains[value] = idx


        return False