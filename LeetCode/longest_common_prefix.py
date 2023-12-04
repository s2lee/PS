class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
