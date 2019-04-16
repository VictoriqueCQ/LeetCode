class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2 == 1:
            return self.findK(nums1,m,nums2,n,(m+n)/2+1)
        else:
            return (self.findK(nums1,m,nums2,n,(m+n)/2)+self.findK(nums1,m,nums2,n,(m+n)/2+1))/2
    def findK(self,nums1,m,nums2,n,k):
        if m < n:
            return self.findK(nums2,n,nums1,m,k)
        if n == 0:
            return float(nums1[k-1])
        if k == 1:
            return float(min(nums1[0],nums2[0]))
        p2 = min(k/2,n)
        p1 = k-p2
        if nums1[p1-1]==nums2[p2-1]:
            return float(nums1[p1-1])
        if nums1[p1-1] < nums2[p2-1]:
            return self.findK(nums1[p1:],m-p1,nums2,n,k-p1)
        if nums1[p1-1] > nums2[p2-1]:
            return self.findK(nums1,m,nums2[p2:],n-p2,k-p2)