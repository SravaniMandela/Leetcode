class Solution(object):
    def constructRectangle(self, area):
        r=[]
        s=[]
        for l in range(1,area+1):
            for w in range(1,area+1):
                if(l*w==area):
                    r.append([l,w])
                    s.append(abs(w-l))
        idx = s.index(min(s))
        print(idx)
        return r[idx]

area = 122122
sol = Solution()
print(sol.constructRectangle(area))

#got the solution but too time taking