#   File Name:           MediaofTSA004
#   Description:
#   Author:              midasevil
#   date:                2018/10/22
#

__author__ = 'midasevil'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        total = len(nums1) + len(nums2)
        
        comp = len(nums1) - len(nums2)
        if comp > 0:
            nums2 = [float("-Inf")]*comp + nums2

        elif comp < 0:
            nums1 = [float("-Inf")]*-comp + nums1

        else:
            nums1 = [float("-Inf")] + nums1
            nums2 = [float("-Inf")] + nums2

        bag = []
        mid = total // 2
        rank = 1

        while 1:
            if nums1[-1] < nums2[-1]:
                last_num = nums2.pop()
            else:
                last_num = nums1.pop()

            print(last_num)

            if rank == mid and not(total % 2):
                bag.append(last_num)

            if rank == mid + 1:
                if total % 2:
                    return last_num
                else:
                    return (last_num + bag[0])/2
            rank = rank + 1


nums1 = [1, 2]
nums2 = [3, 4]
s = Solution()
median = s.findMedianSortedArrays(nums1, nums2)

print(median)
