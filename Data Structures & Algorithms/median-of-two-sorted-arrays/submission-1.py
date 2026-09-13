class Solution:

    # let us merge the numbers
    # and then find the center

    # for merging make a resu list
    # whichever one smaller keep on appending that 
    # and whichever one left at the end
    # fully append that

    def createMerge(self, nums1: List[int], nums2: List[int]) -> list:
        res = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
            else:
                res.append(nums2[i2])
                i2 += 1
        
        res.extend(nums1[i1:])
        res.append(nums2[i2:])
        
        return res
        



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = self.createMerge(nums1, nums2)

        print(merged)

        if len(merged) % 2 == 0:
            idx = len(merged) // 2
            res = (merged[idx - 1] + merged[idx])/2
        else:
            idx = len(merged) // 2
            res = merged[idx]
        
        return float(res)




        