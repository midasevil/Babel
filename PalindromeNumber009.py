class Solution:
    def isPalindrome(self, x):
        x_len = len(str(x))
        mid = x_len // 2 
        print(mid)
        
        if x < 0:
            return False
        elif x_len%2 == 0:
            a = str(x)[0:mid]
            b = str(x)[mid:][::-1]
        else:
            a = str(x)[0:mid]
            b = str(x)[mid+1:][::-1]
        print(a)
        print(b)
        return a == b


s = Solution()
print(s.isPalindrome(-23132))
            


            
