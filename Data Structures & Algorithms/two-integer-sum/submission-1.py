class Solution:
    def twoSum(self, nums, target):
        prevVal = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevVal:
                return([prevVal[diff], i])
            prevVal[n] = i

