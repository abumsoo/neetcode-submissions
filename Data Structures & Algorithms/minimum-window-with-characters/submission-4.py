class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        count = {}
        have, need = 0, len(t_count)

        l = 0
        min_len = float('inf')
        res = ""

        for r in range(len(s)):
            if s[r] in t_count:
                count[s[r]] = 1 + count.get(s[r], 0)

                if count[s[r]] == t_count[s[r]]:
                    have += 1

            while have == need:
                if min_len > r - l + 1:
                    res = s[l: r+1]
                    min_len = r - l + 1

                lchar = s[l]
                if lchar in t_count:
                    count[lchar] -= 1

                    if count[lchar] < t_count[lchar]:
                        have -= 1
                l += 1

        return res