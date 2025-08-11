#not stack actually means stack is empty
class Solution(object):
    def isValid(self, s):
        mapping = {')': '(', '}': '{', ']': '['}
        stack=[]
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1]!= mapping[i]:
                    return False
                stack.pop()
        return not stack 

s = "(])["
sol=Solution()
print(sol.isValid(s))