class Solution(object):
    def stringMatching(self, words):
        w=[]
        for i in range(len(words)):
            for j in words:
                if(words[i] in j and words[i]!=j):
                    w.append(words[i])
        return list(set(w))              # to remove duplicates and again converting to list coz we need answer in list
        

words = ["mass","as","hero","superhero"]
sol = Solution()
print(sol.stringMatching(words))



#output: ["as","hero"] coz these were substrings of other 2