class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    res.append(i)
                    nums2.remove(j)
                    break

        return res