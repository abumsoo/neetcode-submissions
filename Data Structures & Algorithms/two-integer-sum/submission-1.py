class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, n in enumerate(nums):
            summand = target - n
            if summand in comp:
                return ([comp[summand], i])
            comp[nums[i]] = i
        