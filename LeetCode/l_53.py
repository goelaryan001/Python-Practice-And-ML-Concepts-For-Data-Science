#We have to take three loops one i for beginning index , one j for last index wrt to i and last k for calculation sum btw which leads to O(n^3): brute force 

#Now one thing we can do is make a curSum which stores the prev sum and just add the next number coming in array
#So two loops start and end and curSum+num[j]: O(N^2): My solution initially

#Sliding window : remove the negative prefix:going through array and removing any negative prefix:O(N)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray=nums[0]
        currSum=0

        for n in nums:
            if currSum<0:
                currSum=0
            currSum+=n
            maxSubarray=max(maxSubarray,currSum)
        
        return maxSubarray
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)

        return maxSum