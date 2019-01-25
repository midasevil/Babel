class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        max_len_sub = 0

        if len_s < 2:
            return len_s

        for i in range(len_s-1):
            sub = [s[i]]
            for j in range(i+1 , len_s):
                if s[j] not in sub:
                    sub.append(s[j])
                else:
                    break
            max_len_sub = max(len(sub),max_len_sub)
            
        return max_len_sub 

  
s = "au"

solution = Solution()
a = solution.lengthOfLongestSubstring(s)
print(a)