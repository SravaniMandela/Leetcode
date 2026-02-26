class Solution(object):
    def defangIPaddr(self, address):
            address = address.replace(".","[.]")
            return address
address = "255.100.50.0"
sol=Solution()
print(sol.defangIPaddr(address))