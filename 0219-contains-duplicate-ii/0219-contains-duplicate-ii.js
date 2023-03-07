/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    
    
    for(let i = 0; i < nums.length; i +=1 ){
        
        for(let j =  i + 1; j < nums.length; j +=1){
              if(nums[i] == nums[j] && Math.abs(i-j) <= k){
                  return true
              }
        }   
   
    }
    
    return false
};