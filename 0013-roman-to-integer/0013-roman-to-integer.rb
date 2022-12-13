# @param {String} s
# @return {Integer}
def roman_to_int(s)
    roman = {'I' => 1, 'V' => 5, 'X' => 10, 'L'=>50, 'C'=>100, 'D' =>500, 'M'=>1000}
    string = s.split('')
    max = roman[string[0]]
    sum = roman[string[0]]
    index = 1
    while index < string.length
        if max >= roman[string[index]]
            sum += roman[string[index]]
            max = roman[string[index]]  
        else  
           sum -= max + max
            
            sum += roman[string[index]] 
            max = roman[string[index]] 
        end
            index += 1
      
    end
       
    sum
end

# 1 As long as MAX is >= NEXT,  add
# make NEXT the MAX
# false next might be added already, first remove added and still subtract the it again 
# Example MCMXCIV. (first value is the max)
                # SUM
# M > C -> YES = M + C     # As long as MAX is >= next add, make NEXT the MAX
# C > M -> NO = M + C - C + M - C OR  M+C-2C+M # first take out the C that was added after sub the difference of NO eg CM = M - C -> 1000 - 100 = 900;  continue the process


