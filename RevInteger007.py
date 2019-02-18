class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >= 0:
            rev = int(str(x)[::-1])
            return rev if x <= (2**31-1) and rev <= (2**31-1) else 0
        else:
            rev = int('-'+str(x)[1:][::-1])
            return rev if x >= (-2**31) and rev >= (-2**31) else 0
        

x = 1534236469

s = Solution()
print(s.reverse(x))