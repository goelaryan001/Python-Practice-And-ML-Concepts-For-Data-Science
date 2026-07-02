# Brute force:
# Create a new array.
# First copy all the non-zero elements, then append all the zeroes at the end.
# Finally copy the new array back to nums.
# This takes O(N) time but requires O(N) extra space.

# Optimized idea:
# Use two pointers:
# l -> position where the next non-zero element should be placed.
# r -> traverses the array.
#
# Whenever nums[r] is non-zero:
# Swap nums[l] and nums[r], then move l forward.
#
# This keeps all non-zero elements at the beginning while pushing
# zeroes towards the end, all in-place.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1