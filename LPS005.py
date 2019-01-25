#   File Name:           LPS005     
#   Description:
#   Author:              midasevil
#   date:                2018/11/4
#

__author__ = 'midasevil'

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        """
        start = 0
        max_len = 1
        len_s = len(s)
        if len_s == 0 :
            return 0
        dp = [[0 for i in range(len_s) ]for j in range(len_s)]

        for i in range(len_s):
            dp[i][i] = True

        for i in range(len_s - 1):
            j = i+1
            if s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_len = 2

            else :
                dp[i][j] = False

        length = 3
        while length <=len_s:
            for i in range(len_s - 2):
                j = i + (length - 1)
                if j < len_s:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        max_len = length
                        start = i

                    else:
                        dp[i][j] = False
            length += 1


        return s[start:start+max_len]


s = Solution()
l = s.longestPalindrome("addgddabbceijd")
print(l)


