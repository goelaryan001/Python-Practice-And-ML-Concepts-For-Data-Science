#My solution is take two pointers l and r in two opposite ends and take squares of 
# associated number and see which one is bigger, the one is bigger put it in end of our 
# array which is output nd decrease or increase the pointer

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r]*nums[r])
                r-=1
        return res[::-1] 