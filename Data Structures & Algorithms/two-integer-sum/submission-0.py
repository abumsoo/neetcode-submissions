class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        n = len(nums)
        for i in range(n):
            summand = target - nums[i]
            if summand in comp:
                return ([comp[summand], i])
            comp[nums[i]] = i
        