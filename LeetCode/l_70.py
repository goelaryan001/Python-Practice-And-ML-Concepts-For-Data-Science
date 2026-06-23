#Brute force: make a decision tree go down using dfs and look how many ways u reach to output target: O(2^n) as eacj time we have 2 decision and n is the roghly the height of the tree   
#One step. to simplify is that why to recalculate some parts in our tree, like for subproblems where already reached 2 , we will be calucating it all time in brute force when we reach there b any side, so rather memorization almost making it rach to O(N) 
#Use Bottom UP approach solve base case case make your way upto inital step
#example take of 5 and explain using dp table: 0,1,2,3,4,5: 8,5,3,2,1,1 like fibonacci series as for index i it depends on the sum of last two
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

        