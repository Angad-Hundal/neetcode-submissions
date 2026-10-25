class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        def combine(nums1: List[int], nums2: List[int]) -> List(int):
            
            res = []
            i, j = 0, 0

            while i < len(nums1) and j <len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            
            while i < len(nums1):
                res.append(nums1[i])
                i += 1
            while j < len(nums2):
                res.append(nums2[j])
                j += 1

            return res


        combine = combine(nums1, nums2)

        print(combine)

        if len(combine) % 2 == 1:
            mid = len(combine)//2
            return combine[mid]
        
        idx1 = len(combine)//2
        idx2 = idx1-1
        print(idx1)
        print(idx2)

        return (combine[idx1] + combine[idx2])/2
