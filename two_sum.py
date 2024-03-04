class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    l = [i, j]
                    return l