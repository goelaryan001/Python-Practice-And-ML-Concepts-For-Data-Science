# Brute: we have a decision tree type like which house to rob, lets say we rob house 1 , 
# then 2 cnt be which leads to decision of choosing from subprob house 3 and 4 to get max 
# or second scenario we chose house 2 as starting then we have only option of house 4

# rob=max(array[0]+rob[2,n], rob[1,n])

#     1, 2, 3, 1
#SUM: 1 | 2| 4| 3 or 4 so 4 so here the concept is we are calculating subprob like just looking 
# the prev 2, like if 4th one is selected  then we have to look up the answer of of subprob 
# of 1 and 2 which is 2, then 1+2 is 3 whereas if we dont select house 4 then it is solution of 
# the subarray before that which is already calculated as 4
#dp[i]=max(nums[i]+dp[i-2],dp[i-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        #[rob1,rob2,n,n+1,.....]
        rob1,rob2=0,0

        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]


        