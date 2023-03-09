class Solution(object):
    def sortColors(self, nums):
       
        for index in range(1, len(nums) ):
            pos = index - 1
            temp = nums[index]
            
            while pos >= 0 :
                if nums[pos] > temp :
                    nums[pos + 1] = nums[pos] 
                    pos -= 1
                else:
                    break
            nums[pos + 1] = temp
            
            # return nums
