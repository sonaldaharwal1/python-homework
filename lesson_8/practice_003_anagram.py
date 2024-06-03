# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False

# def is_anagram(word1, word2):
#     # Check if the sorted forms of both words are equal
#     return sorted(word1) == sorted(word2)
#
# # Test cases
# print(is_anagram('cat', 'act'))  # Output: True
# print(is_anagram('bus', 'sub'))  # Output: True
# print(is_anagram('map', 'cap'))  # Output: Fals

str1= "cat"
str2= "act"

if len(str1) != (str2):
    print(False)
elif sorted(str2) == sorted(str2):
    print(True)
else:
    print(False)