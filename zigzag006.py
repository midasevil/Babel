class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ## 新生成的z字形，满足一定的周期循环模式。找出其中一个周期的pattern，能获得每个字符在这个周期
        ## 中所处的row，再将每个row视为一个桶，往每个桶里按秩序丢字符

        len_s = len(s)
        if numRows == 1 or  numRows > len_s:
            return s

        buckets = [""] * numRows

        period_pattern = list(range(numRows-1)) + list(range(numRows-1,0,-1))
        len_p = len(period_pattern)
       
        for i in range(len_s):
            buckets[period_pattern[i%len_p]] += s[i]

        return "".join(buckets)

         




st  = "PAYPALISHIRING"
r = 3

s = Solution()
print(s.convert(st,r))