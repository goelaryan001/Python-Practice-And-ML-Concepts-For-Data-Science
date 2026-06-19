# Instead of recalculating left and right sums every time,
# compute the total sum of the array once.
#
# For any index i:
# rightSum = totalSum - nums[i] - leftSum
#
# Since:
# totalSum = leftSum + nums[i] + rightSum
#
# We maintain a running leftSum while traversing the array.
# At each index:
# 1. Compute rightSum using the formula above.
# 2. Check if leftSum == rightSum.
# 3. If yes, current index is the pivot index.
# 4. Otherwise include nums[i] in leftSum and continue.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums) #O(n)

        leftSum=0
        for i in range (len(nums)):
            rightSum=total-nums[i]-leftSum
            if leftSum==rightSum:
                return i
            leftSum+=nums[i]
        return -1
        