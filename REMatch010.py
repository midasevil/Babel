class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(s,p)
        if len(p)>=2 and p[1]=="*":
            if not s and len(p)==2 :
                return True
                
            if p[0] != s[0] and p[0] != ".":
                return self.isMatch(s,p[2:])
            else:
                return self.isMatch(s[1:],p)

        if  not p or not s:
            return not p and not s

        if p[0] not in (s[0],"."):
            print(p[0],s[0])
            return False
        
        else:
            return self.isMatch(s[1:],p[1:])

s = Solution()  
print(s.isMatch("ab",".*c"))