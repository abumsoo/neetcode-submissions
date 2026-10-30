class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)

        code = [[] for i in range(len(nums)+1)]
        
        for key, val in freqs.items():
            code[val].append(key)

        ans = []
        for c in reversed(code):
            ans += c

        return ans[:k]