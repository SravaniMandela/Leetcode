#all conditions were just based on problem statement and ops[i].lstrip('-').isdigit() is for accepting negative values as digit
class Solution(object):
    def calPoints(self, ops):
        new_ops=[]
        for i in range(len(ops)):
            if ops[i].lstrip('-').isdigit():
                ops[i] = int(ops[i])
                new_ops.append(ops[i])
            if ops[i]=="C":
                new_ops.pop()
            if ops[i]=="D":
                new_ops.append(new_ops[-1] * 2)
            if ops[i]=="+":
                new_ops.append(new_ops[-1] + new_ops[-2])
        return sum(new_ops)
        
ops = ["5","-2","4","C","D","9","+","+"]
sol=Solution()
print(sol.calPoints(ops))