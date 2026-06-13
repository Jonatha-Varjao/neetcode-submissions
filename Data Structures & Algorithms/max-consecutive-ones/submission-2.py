class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cc = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp >= cc:
                    cc = temp
                temp = 0
                            
        if temp > cc:
            cc = temp
        
        return cc