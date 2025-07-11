class Solution(object):
    def longestCommonPrefix(self, strs):
        st = ""
        for i in range(len(strs[0])): 
            j = strs[0][i]            
            for k in range(len(strs)):
                if i >= len(strs[k]) or j != strs[k][i]:
                    return st
            st = st + j
        return st

strs = ["flower", "flow", "flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
