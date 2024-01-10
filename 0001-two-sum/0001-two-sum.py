class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       # since only two items some up to target
        # we need not to first populate the hashmap before checking, check it along side
        
        hashmap  = {
            
        }#val : index
    
        for index, value in enumerate(nums):
            #find if other half is in the hashmap and return both
            diff = target - value
            if diff in hashmap :
                return [hashmap[ diff], index]
            hashmap[value] = index
        return