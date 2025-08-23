class Solution(object):
    def deleteDuplicates(self, head):
        new_head=[]
        for i in range(len(head)):
            if(head[i] not in new_head):
                new_head.append(head[i])
        return new_head
                    
head = [1,1,2,3,3]        
sol=Solution()
print(sol.deleteDuplicates(head))