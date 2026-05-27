class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        _dict = {}

        for idx,value in enumerate(nums):
            difference = target - value
            print(idx,value,difference)
            if not value in _dict:
                _dict[difference] = idx
            else:
                return [_dict[value], idx  ]
        

