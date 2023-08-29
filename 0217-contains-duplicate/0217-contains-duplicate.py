class Solution(object):
    def containsDuplicate(self, nums):
        cache = {}
        for num in nums:
            count =  cache.get(num, 0) + 1
            if count >= 2:
                return True
            cache[num] = count
            
        return False
        