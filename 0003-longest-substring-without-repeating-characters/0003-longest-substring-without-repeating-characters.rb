# @param {String} s
# @return {Integer}

def length_of_longest_substring(s)
    seen = Set.new

    start = 0
    end_idx = 0

    longest = 0

    while end_idx < s.length
        if !seen.include?(s[end_idx])
            seen.add(s[end_idx])
            end_idx += 1

            longest = [longest, end_idx - start].max
        else
            seen.delete(s[start])
            start += 1
        end
    end

longest
end 