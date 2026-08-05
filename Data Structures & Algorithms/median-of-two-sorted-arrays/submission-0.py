class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       n = sorted(nums1 + nums2)

       length = len(n)
       mid_index = length // 2

       if length % 2 != 0:
        median = n[mid_index]
       else:
        median = (n[mid_index - 1] + n[mid_index]) / 2

       return median
        