class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_array = nums[:len(nums)]
        candidate = nums[0]
        count = 0

        for idx,value in enumerate(half_array):
            if count == 0:
                candidate = value
            if value == candidate:
                count+=1
            if value != candidate:
                count-=1
        return candidate