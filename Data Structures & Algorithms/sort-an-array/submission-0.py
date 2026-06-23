class Solution:
    def merge(self, left,right):
        result = []
        i=j=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # compare correctly: left[i] vs right[j]
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left_half, right_half = nums[:mid], nums[mid:]
        left_sort = self.sortArray(left_half)
        right_sort = self.sortArray(right_half)
        
        merged = self.merge(left_sort, right_sort)
        return merged
