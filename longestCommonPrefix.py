class Solution(object):
    def longestCommonPrefix(self, strs):
        st=""
        for i in range(len(strs[0])): 
            j=strs[0][i]            
            for k in range(len(strs)):
                if i>=len(strs[k]) or j!=strs[k][i]:
                    print(st)
                    return
            st=st+j
        print(st)
strs = ["flower","flow","flight"]
solution = Solution()
solution.longestCommonPrefix(strs)
