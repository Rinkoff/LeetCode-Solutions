"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
def isPalindrome(number : int):
    char_list = list(str(number))
    reversed_list = char_list[::-1]

    if char_list == reversed_list:
        print("True")
    else:
        print("False")


isPalindrome(121)
