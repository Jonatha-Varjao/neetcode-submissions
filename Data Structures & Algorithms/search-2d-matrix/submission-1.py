class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums):
            l = 0
            r = len(nums)-1

            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    r = mid -1
                if nums[mid] < target:
                    l = mid +1
            
            return False
        
        for rows in matrix:
            l = 0
            r = len(rows)-1
            if rows[r] >= target and rows[l] <= target:
                return binary_search(rows)
            else:
                continue 
        return False