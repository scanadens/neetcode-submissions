class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sum of integers from one array forms a target sum, two indices are not same, just one valid answer
        #dictionary mapping...
        #whatever brute force
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [min(i, j), max(i, j)]