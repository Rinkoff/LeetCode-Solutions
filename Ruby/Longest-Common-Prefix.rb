"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

#@param {String[]} strs
#@return {Sting}

def longest_common_prefix(strs)
    return "" if strs.empty?

    prefix = ""
    strs[0] do |letter,i|
        if strs.all? {|s| s[i]==letter}
            prefix += letter
        else
            break
        end
    end
    prefix
end


strs = ["flower", "flow", "flight"]
puts longest_common_prefix(strs) 