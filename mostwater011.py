class Solution:
    def maxArea(self, height):
        height_len = len(height)
        maxarea = 0
        for i in range(height_len-1):
            for j in range(i,height_len):
                area = min(height[i],height[j])*(j-i)
                maxarea = max(maxarea,area)

        return maxarea

    def maxArea2(self, height):
        height_len = len(height)
        maxarea = 0
        i = 0
        j = height_len-1
        while j > i:
            if height[i] > height[j]:
                area = height[j] * (j-i)
                j =j -1
            else:
                area = height[i] * (j-i)
                i = i+1
            maxarea = max(area,maxarea)
        return(maxarea)
             
    
        