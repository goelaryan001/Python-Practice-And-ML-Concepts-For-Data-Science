# Brute force:
# For every number from 1 to n, scan the entire array to check whether it exists.
# If it does not exist, add it to the answer.
# This takes O(N^2) time because for each of the N numbers, we may scan N elements.
# Time: O(N)
# Space: O(1) extra space (excluding output)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark all seen numbers by making the corresponding index negative
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        # Collect indices that were never marked
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res 