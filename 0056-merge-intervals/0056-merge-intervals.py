class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        
        index = 0;
    
        intervals = sorted(intervals, key = lambda x: x[0])
        
        while index < len(intervals) - 1 :
          
            if intervals[index][1] >= intervals[index + 1][0] and  intervals[index][1] <= intervals[index + 1][1]:
                # [1,3],[2,6]
                intervals[index] = [intervals[index][0], intervals[index + 1 ][1]]
                del intervals[index + 1]
                
            elif intervals[index][1] <= intervals[index+1][0] and intervals[index][1] >= intervals[index + 1][1]:
                #  [1, 4][5, 1] 
                intervals[index] = [intervals[index][0], intervals[index + 1][0]]
                del intervals[index + 1]
                
            elif intervals[index][1] >= max(intervals[index + 1]):
                # [1,4][2,3]
                del intervals[index + 1]
         
            else:
                index += 1
                # overlap.append(intervals[index]) 
            
            # index += 1
        
        
        return intervals
            
