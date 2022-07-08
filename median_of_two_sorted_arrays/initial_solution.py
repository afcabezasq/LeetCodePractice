from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        totalSize = size1 +size2
        bigList = self.sortBigArray(nums1, nums2)
        if totalSize%2 == 0:
            middle = totalSize/2
            return (bigList[int(middle)] + bigList[int(middle-1)])/2
        else:
            middle = (totalSize - 1)/2
            print(middle)
            return bigList[int(middle)]     
        
        
        
    def sortBigArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
                
        if len(nums1) == 0:
            return nums2
        
        if len(nums2) == 0:
            return nums1
        
        bigList = []    
        
        while len(nums1) > 0 or len(nums2) > 0:
            
            if len(nums2) == 0:
                bigList.append(nums1[0])
                if len(nums1) > 1:
                    nums1.pop(0)
                else:
                    nums1.clear()
                continue
            if len(nums1) == 0:
                bigList.append(nums2[0])
                if len(nums2) > 1:
                    nums2.pop(0)
                else:
                    nums2.clear()
                continue
            
            if nums1[0] > nums2[0]:
                bigList.append(nums2[0])
                if len(nums2) > 1:
                    nums2.pop(0)
                else:
                    nums2.clear()
            else:
                bigList.append(nums1[0])
                if len(nums1) > 1:
                    nums1.pop(0)
                else:
                    nums1.clear()
            
            
            
        return bigList
            
            
            
            
            
            
            
        
        

        return bigList    