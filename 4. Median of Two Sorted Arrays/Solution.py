from typing import List#, Tuple

# Looked at algorithm for reference @: https://youtu.be/q6IEA26hvXc?si=kOP15q1ruGlc2pkR

# class Solution:
#     def partition(self, lst1: List[int], lst2: List[int]) -> Tuple[List[int], List[int], List[int], List[int], int]:
#         n2M = int(len(lst2) / 2)
#         n1M = int((len(lst1) + len(lst2)) / 2) - n2M

#         lp1 = lst1[:n1M]
#         rp1 = lst1[n1M:]
#         lp2 = lst2[:n2M]
#         rp2 = lst2[n2M:]

#         if(len(lp1) == 0 or len(rp2) == 0):
#             return lp1, rp1, lp2, rp2, 1
#         elif(len(lp2) == 0 or len(rp1) == 0):
#             return lp1, rp1, lp2, rp2, 2

#         return lp1, rp1, lp2, rp2, -1
    
#     def out(self, lp1: List[int], lp2: List[int], rp1: List[int], rp2: List[int]) -> float:
#         if((len(lp1 + rp1) + len(lp2 + rp2)) % 2 == 0):
#             return (max(max(lp1), max(lp2)) + min(min(rp1), min(rp2))) / 2
#         else:
#             return min(min(rp1), min(rp2))
    
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         total_elements = len(nums1) + len(nums2)
#         n1_len = len(nums1)
#         n2_len = len(nums2)

#         if(n2_len > n1_len):
#             temp = nums1
#             nums1 = nums2
#             nums2 = temp
#             n1_len = len(nums1)
#             n2_len = len(nums2)

#         lp1, rp1, lp2, rp2, infty = self.partition(nums1, nums2)

#         while(True):
#             if(infty == 1):
#                 if(max(lp2) > min(rp1)):
#                     # RERUN BIN SEARCH
#                     continue
#                 else:
#                     return self.out(lp1, lp2, rp1, rp2)
#             elif(infty == 2):
#                 if(max(lp1) > min(rp2)):
#                     # RERUN BIN SEARCH
#                     continue
#                 else:
#                     return self.out(lp1, lp2, rp1, rp2)
#             else:
#                 if(max(lp1) > min(rp2)):
#                     # RERUN BIN SEARCH
#                     continue
#                 elif(max(lp2) > min(rp1)):
#                     # RERUN BIN SEARCH
#                     continue
#                 else:
#                     return self.out(lp1, lp2, rp1, rp2)
                
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1_len, n2_len = len(nums1), len(nums2)

        if n2_len > n1_len:
            nums1, nums2 = nums2, nums1
            n1_len, n2_len = len(nums1), len(nums2)
        
        low, high = 0, n2_len

        while low <= high:
            partition2 = (low + high) // 2
            partition1 = ((n1_len + n2_len) // 2) - partition2

            if partition1 == 0:
                max_left1 = float('-inf')
            else:
                max_left1 = nums1[partition1 - 1]

            if partition1 == n1_len:
                min_right1 = float('inf')
            else:
                min_right1 = nums1[partition1]

            if partition2 == 0:
                max_left2 = float('-inf')
            else:
                max_left2 = nums2[partition2 - 1]

            if partition2 == n2_len:
                min_right2 = float('inf')
            else:
                min_right2 = nums2[partition2]

            if max_left2 <= min_right1 and max_left1 <= min_right2:
                if (n1_len + n2_len) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return min(min_right1, min_right2)
            elif max_left1 > min_right2:
                low = partition2 + 1
            else:
                high = partition2 - 1