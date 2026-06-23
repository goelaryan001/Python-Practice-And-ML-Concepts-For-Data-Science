#Here just checking if for a particular arr[i] and checking the whole array if we have the any 
# elemnt making it to targe:O(N^2) Brute
# Now one method is suppose we have a number lets say 2 then difference from target =7 , 
# then using. hashmap we can find if we have that number or not
#initially dont fill hash map and just iterate through array and then fill the hast map:
#  2,0 7,1 alearady got to solution as 2 was there in there:O(N) as we are guaranteed 
# that the first object is there in hash map when we reach to the next element

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} #val:index

        for i , n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
        