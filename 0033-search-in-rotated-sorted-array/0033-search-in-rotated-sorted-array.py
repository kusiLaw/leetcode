class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
           num =  nums.index(target)
        except:
            return -1
        return num