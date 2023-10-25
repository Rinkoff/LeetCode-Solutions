"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    
    prefix = ""
    for i,letter in enumerate(strs[0]):
        if all(s[i] == letter for s in strs):
            prefix += letter
        else:
            break
    return prefix

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))
