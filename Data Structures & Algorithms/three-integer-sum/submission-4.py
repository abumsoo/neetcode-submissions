class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        nums.sort()
        for i, t in enumerate(nums):
            if t > 0:
                break

            if i > 0 and t == nums[i-1]:
                continue

            l = i+1
            r = n-1
            while l < r:
                summand = nums[l] + nums[r] + t
                if summand == 0:
                    triplets.append([nums[l], nums[r], t])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                if summand > 0:
                    r -= 1
                if summand < 0:
                    l += 1
        return triplets
                