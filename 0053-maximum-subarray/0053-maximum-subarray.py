class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        large_sum = nums[0]
        current_sum = 0
        # k
        
        for n in nums:
            current_sum += n #add what ever to current sum
            large_sum = max(current_sum,large_sum) #max btn the twoo
            
            # if adding everything give nrgative ignore all and start adding next
            if current_sum < 0: 
                
                current_sum = 0
        return large_sum