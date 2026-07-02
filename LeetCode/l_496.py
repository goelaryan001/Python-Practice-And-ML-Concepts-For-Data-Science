# Brute force:
# For every element in nums1, first find its position in nums2.
# Then scan to the right until we find the first greater element.
# In the worst case, for every element we traverse almost the entire nums2.
# Time: O(M * N), where M = len(nums1) and N = len(nums2).

# Optimized idea:
# Traverse nums2 only once using a monotonic decreasing stack.
# The stack stores elements whose next greater element has not been found yet.
#
# Whenever we find a larger element:
# - It becomes the next greater element for all smaller elements
#   on top of the stack.
# - Pop those elements and store their mapping in a hashmap.
#
# After processing nums2, use the hashmap to answer queries for nums1.
# If an element has no greater element, return -1.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)

        return [nextGreater.get(num, -1) for num in nums1]