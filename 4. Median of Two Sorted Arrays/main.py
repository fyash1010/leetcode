import Solution

# Example test cases
# nums1 = [1, 3]
# nums2 = [7]

# nums1 = [1, 2, 4, 7, 17]
# nums2 = [3, 4, 19, 20]

nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [10, 11, 12]

solution = Solution.Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print("Median is:", result)