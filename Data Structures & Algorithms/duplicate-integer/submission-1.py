class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Convert list to set and check if length is equal
        my_set = set(nums)
        if len(my_set) == len(nums):
            return False
        else:
            return True