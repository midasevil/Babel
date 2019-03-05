class Solution:
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        num = 0
        cur = float('inf')
        pre = None
        for c in s:
            prev = cur
            cur = d[c]
            if cur > prev:
                num = num + cur - 2*prev
            else:
                num = num + cur
        return num

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("MCMXCIV"))



