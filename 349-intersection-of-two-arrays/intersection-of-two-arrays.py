class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        s = set()
        res = set()
        
        if(len(nums1) == 1 and len(nums2) == 1 and nums1[0] != nums2[0]):
            return []

        if(len(nums1) == 1):
            return [nums1[0]]
        
        if(len(nums2) == 1):
            return [nums2[0]]

        for i in range(len(nums1)):
            s.add(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] in s:
                res.add(nums2[i])

        return list(res)