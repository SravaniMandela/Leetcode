#local name after + has to be ignored and if dot exists the you have to remove that dot, domain should be as it is
class Solution(object):
    def numUniqueEmails(self, emails):
        new_emails=[]
        for i in emails:
            local,domain = i.split("@")
            #print(local,domain)
            if("+" in local):
                local=local.split("+")[0]
            local=local.replace(".","")
            new_emails.append(local+"@"+domain)
        new_emails=set(new_emails)
        return len(new_emails)
            
                
                
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@leetcode.com"
]
sol=Solution()
print(sol.numUniqueEmails(emails))