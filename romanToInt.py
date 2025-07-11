class Solution(object):
    def romanToInt(self, s):
        d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        v=0
        for i in range(len(s)-1,-1,-1):
                 if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                    v=v-d[s[i]]
                 else:
                    v=v+d[s[i]]
        return v
# s="III"
# s="LVIII"
s="MCMXCIV"
solution = Solution()
print(solution.romanToInt(s))

        